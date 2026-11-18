from abstract_schedule import AbstractSchedule
from schedule_item import ScheduleItem
from task import Task


class Schedule(AbstractSchedule):
    """Класс представляет оптимальное расписание для списка задач и количества
    исполнителей. Для построения расписания используется Ленточная стратегия.

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

    def __init__(self, tasks: list[Task], executor_count: int):
        """Конструктор для инициализации объекта расписания.

        :param tasks: Список задач для составления расписания.
        :param executor_count: Количество исполнителей.
        :raise ScheduleArgumentError: Если список задач предоставлен в
        некорректном формате.
        """
        super().__init__(tasks, executor_count)

        # Рассчитывается и сохраняется в приватном поле класса минимальная
        # продолжительность расписания
        self._duration = self.__calculate_duration()

        # Процедура заполняет пустую заготовку расписания для каждого
        # исполнителя объектами ScheduleItem.
        self.__fill_schedule_for_each_executor()

    @property
    def duration(self) -> float:
        """Возвращает общую продолжительность расписания."""
        return self._duration

    def __calculate_duration(self) -> float:
        """Вычисляет и возвращает минимальную продолжительность расписания"""
        total_duration = sum(task.duration for task in self.tasks)
        longest_task = max(task.duration for task in self.tasks)
        average_duration = total_duration / self.executor_count

        return max(average_duration, longest_task)

    def __fill_schedule_for_each_executor(self) -> None:
        """Процедура составляет расписание из элементов ScheduleItem для каждого
        исполнителя, на основе исходного списка задач и общей продолжительности
        расписания."""
        epsilon = 1e-9 * max(1.0, self._duration)

        executor_idx = 0
        time = 0

        for task in self._tasks:
            remaining = task.duration

            while remaining > 0:
                free_time = self._duration - time

                if remaining - free_time <= epsilon:
                    part = remaining
                else:
                    part = free_time

                self._executor_schedule[executor_idx].append(
                    ScheduleItem(task, time, part)
                )
                time += part
                remaining -= part

                if self._duration - time <= epsilon:
                    executor_idx += 1
                    time = 0
                    if executor_idx >= self.executor_count:
                        break

            if executor_idx >= self.executor_count:
                break

        for executor_idx in range(self.executor_count):
            executor_schedule = self._executor_schedule[executor_idx]
            used_time = executor_schedule[-1].end if executor_schedule else 0
            if self._duration - used_time > epsilon:
                executor_schedule.append(
                    ScheduleItem(None, used_time, self._duration - used_time)
                )
