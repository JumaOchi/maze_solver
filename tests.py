import unittest
from maze import Maze
from draw import Cell, Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_cell_draw_all_walls(self):
        win = Window(200, 200)
        cell = Cell(win)
        cell.draw(10, 10, 50, 50)
        self.assertEqual(cell.x1, 10)
        self.assertEqual(cell.y1, 10)
        self.assertEqual(cell.x2, 50)
        self.assertEqual(cell.y2, 50)
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_cell_instance_in_maze(self):
        m = Maze(0, 0, 5, 5, 20, 20)
        self.assertIsInstance(m._cells[0][0], Cell)

    def test_cell_with_removed_wall(self):
        win = Window(200, 200)
        cell = Cell(win)
        cell.has_left_wall = False
        cell.draw(60, 60, 100, 100)
        self.assertFalse(cell.has_left_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_break_entrance_and_exit(self):
        win = Window(200, 200)
        m = Maze(0, 0, 5, 5, 20, 20, win)
        m._break_entrance_and_exit()
        self.assertFalse(m._cells[0][0].has_top_wall)
        self.assertFalse(m._cells[m._num_cols - 1][m._num_rows - 1].has_bottom_wall)

    


if __name__ == "__main__":
    unittest.main()