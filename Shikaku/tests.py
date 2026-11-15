import unittest
from generate import generate_cell_map, generate_full_map
from validate import validate
from find_objects import find_regions
from solve_task import solve

class Tests(unittest.TestCase):

    def test_generate_cell_map_size_2(self):
        map_cells = generate_cell_map(2)
        self.assertEqual(len(map_cells), 7)
        self.assertIn((0, 0), map_cells)

    def test_generate_cell_map_size_3(self):
        map_cells = generate_cell_map(3)
        self.assertEqual(len(map_cells), 19)
        self.assertIn((0, 0), map_cells)

    def test_generate_cell_map_size_4(self):
        map_cells = generate_cell_map(4)
        self.assertEqual(len(map_cells), 37)
        self.assertIn((0, 0), map_cells)

    def test_validate_correct(self):
        map_cells, numbers = generate_full_map(2)
        valid, error = validate(map_cells, numbers)
        self.assertTrue(valid)
        self.assertIsNone(error)

    def test_validate_incorrect(self):
        map_cells, numbers = generate_full_map(2)
        key = list(numbers.keys())[0]
        numbers_copy = numbers.copy()
        numbers_copy.pop(key)
        valid, error = validate(map_cells, numbers_copy)
        self.assertFalse(valid)
        self.assertEqual(error, "сумма чисел не равна количеству шестиугольников!")

    def test_find_regions_size(self):
        map_cells, numbers = generate_full_map(2)
        for cell, size in numbers.items():
            regions = find_regions(cell, size, map_cells)
            flag = False
            for region in regions:
                if len(region) == size:
                    flag = True
                    break
            self.assertTrue(flag)

    def test_solve_basic(self):
        map_cells, numbers = generate_full_map(2)
        all_solves = solve(map_cells.copy(), numbers.copy(), 2)
        self.assertTrue(len(all_solves) >= 1)
        for solution in all_solves:
            cells_in_all_region = set()
            for region in solution.values():
                cells_in_all_region.update(region)
            self.assertEqual(cells_in_all_region, set(map_cells))
