from abstract_schedule import AbstractSchedule
from errors import (
    ErrorMessages,
    ErrorTemplates,
    ScheduleArgumentError,
)
from schedule_item import ScheduleItem
from staged_task import StagedTask


class ConveyorSchedule(AbstractSchedule):
    """Класс представляет оптимальное расписание для списка задач, состоящих
     из двух этапов и двух исполнителей. Для построения расписания используется
     алгоритм Джонсона.

    Properties
    ----------
    tasks(self) -> tuple[Task]:
        Возвращает исходный список задач для составления расписания.

    task_count(self) -> int:
        Возвращает количество задач для составления расписания.

    executor_count(self) -> int:
        Возвращает количество исполнителей.

    duration(self) -> float:
        Возвращает общую продолжительность расписания.

    Methods
    -------
    get_schedule_for_executor(self, executor_idx: int) -> tuple[ScheduleRow]:
        Возвращает расписание для указанного исполнителя.
    """

    def __init__(self, tasks: list[StagedTask]):
        """Конструктор для инициализации объекта расписания.

        :param tasks: Список задач для составления расписания.
        :raise ScheduleArgumentError: Если список задач предоставлен в
        некорректном формате или количество этапов для какой-либо задачи не
        равно двум.
        """
        ConveyorSchedule.__validate_params(tasks)
        super().__init__(tasks, 2)

        # Процедура заполняет пустую заготовку расписания для каждого
        # исполнителя объектами ScheduleItem.
        self.__fill_schedule(ConveyorSchedule.__sort_tasks(tasks))

    @property
    def duration(self) -> float:
        """Возвращает общую продолжительность расписания."""
        return self._executor_schedule[0][-1].end

    def __fill_schedule(self, tasks: list[StagedTask]) -> None:
        """Процедура составляет расписание из элементов ScheduleItem для каждого
        исполнителя, согласно алгоритму Джонсона."""
        first_schedule, second_schedule = self._executor_schedule
        first_end = 0
        second_end = 0

        for task in tasks:
            first_duration, second_duration = task.stage_durations
            first_schedule.append(ScheduleItem(task, first_end, first_duration))
            first_end += first_duration

            second_start = max(first_end, second_end)
            if second_start > second_end:
                second_schedule.append(
                    ScheduleItem(None, second_end, second_start - second_end)
                )
            second_schedule.append(ScheduleItem(task, second_start, second_duration))
            second_end = second_start + second_duration

        if first_end < second_end:
            first_schedule.append(ScheduleItem(None, first_end, second_end - first_end))

    @staticmethod
    def __sort_tasks(tasks: list[StagedTask]) -> list[StagedTask]:
        """Возвращает отсортированный список задач для применения
        алгоритма Джонсона."""
        first_group = []
        second_group = []
        for task in tasks:
            first_duration, second_duration = task.stage_durations
            if first_duration <= second_duration:
                first_group.append(task)
            else:
                second_group.append(task)

        first_group.sort(key=lambda task: task.stage_duration(0))
        second_group.sort(key=lambda task: task.stage_duration(1), reverse=True)
        return first_group + second_group

    @staticmethod
    def __validate_params(tasks: list[StagedTask]) -> None:
        """Проводит валидацию входящих параметров для инициализации объекта
        класса ConveyorSchedule."""
        if not isinstance(tasks, list):
            raise ScheduleArgumentError(ErrorMessages.TASKS_NOT_LIST)
        if len(tasks) < 1:
            raise ScheduleArgumentError(ErrorMessages.TASKS_EMPTY_LIST)
        for idx, value in enumerate(tasks):
            if not isinstance(value, StagedTask):
                raise ScheduleArgumentError(ErrorTemplates.INVALID_TASK.format(idx))
            if value.stage_count != 2:
                raise ScheduleArgumentError(
                    ErrorTemplates.INVALID_STAGE_CNT.format(idx)
                )
