from abstract_schedule import AbstractSchedule
from schedule_item import ScheduleItem
from errors import (
    ScheduleArgumentError,
    ErrorMessages,
    ErrorTemplates,
)
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
        time_0 = 0
        time_1 = 0
        sched_0, sched_1 = self._executor_schedule

        for task in tasks:
            d0 = task.stage_duration(0)
            d1 = task.stage_duration(1)

            item_0 = ScheduleItem(task, time_0, d0)
            sched_0.append(item_0)
            time_0 = item_0.end

            if time_0 > time_1:
                sched_1.append(ScheduleItem(None, time_1, time_0 - time_1))
                time_1 = time_0

            item_1 = ScheduleItem(task, time_1, d1)
            sched_1.append(item_1)
            time_1 = item_1.end

        if time_1 > time_0:
            sched_0.append(ScheduleItem(None, time_0, time_1 - time_0))

    @staticmethod
    def __sort_tasks(tasks: list[StagedTask]) -> list[StagedTask]:
        """Возвращает отсортированный список задач для применения
        алгоритма Джонсона."""
        left = []
        right = []

        ordered = sorted(
            tasks,
            key=lambda t: min(t.stage_duration(0), t.stage_duration(1))
        )

        for task in ordered:
            if task.stage_duration(0) <= task.stage_duration(1):
                left.append(task)
            else:
                right.append(task)

        return left + right[::-1]

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
