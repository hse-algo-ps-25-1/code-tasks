from permutation_generator import generate_permutations
from tsp_abs_solver import AbstractTspSolver, TspSolution


class BruteForceTspSolver(AbstractTspSolver):
    """Полный перебор гамильтоновых циклов"""

    def get_tsp_solution(self) -> TspSolution:
        """Возвращает гамильтонов цикл наименьшей суммарной длины.

        Города — индексы 0, 1, ..., n - 1. Маршрут начинается и заканчивается
        в 0 и содержит каждый город один раз. При n = 1 маршрут — [0],
        расстояние 0. Отсутствующее ребро записано как None. Если цикла нет,
        результат — TspSolution(None, []). Если кратчайших маршрутов несколько,
        годится любой.

        :return: distance — длина маршрута, path — вершины маршрута
        """
        n = self.order
        if n == 1:
            return TspSolution(0, [0])

        best_distance = None
        best_path: list[int] = []

        other_cities = list(range(1, n))
        for perm in generate_permutations(other_cities):
            candidate_path = [0] + perm + [0]
            distance = self.get_distance(self._dist_matrix, candidate_path)
            if distance is not None:
                if best_distance is None or distance < best_distance:
                    best_distance = distance
                    best_path = candidate_path

        if best_distance is None:
            return TspSolution(None, [])

        return TspSolution(best_distance, best_path)
