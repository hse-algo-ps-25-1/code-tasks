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
        executor_1 = self._executor_schedule[0]
        executor_2 = self._executor_schedule[1]
        end_1 = 0
        end_2 = 0

        for task in tasks:
            time_1 = task.stage_duration(0)
            time_2 = task.stage_duration(1)

            executor_1.append(ScheduleItem(task, end_1, time_1))
            end_1 += time_1
            start_2 = max(end_1, end_2)

            if start_2 > end_2:
                executor_2.append(ScheduleItem(None, end_2, start_2 - end_2))
            executor_2.append(ScheduleItem(task, start_2, time_2))
            end_2 = start_2 + time_2

        if end_2 > end_1:
            executor_1.append(ScheduleItem(None, end_1, end_2 - end_1))

    @staticmethod
    def __sort_tasks(tasks: list[StagedTask]) -> list[StagedTask]:
        """Возвращает отсортированный список задач для применения
        алгоритма Джонсона."""
        group_a = []
        group_b = []
        for task in tasks:
            task1_time = task.stage_duration(0)
            task2_time = task.stage_duration(1)

            if task1_time <= task2_time:
                group_a.append(task)
            else:
                group_b.append(task)

        group_a.sort(key=lambda t: t.stage_duration(0))
        group_b.sort(key=lambda t: t.stage_duration(1), reverse=True)
        return group_a + group_b

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
