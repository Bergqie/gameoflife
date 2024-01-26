import unittest
import pygame
import numpy as np
import time
from gameoflife import initialize_grid, update_grid, GRID_WIDTH, GRID_HEIGHT, FPS, main
from unittest.mock import patch

class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()


    def test_initalize_grid(self):
        # Check if the grid is initialized with random values
        grid = initialize_grid()
        self.assertTrue(np.any(grid == 1), "Grid should be initialized with random values.")

    
    def test_update_grid(self):
        # Check if the grid evolves over multiple updates
        initial_grid = initialize_grid()
        for _ in range(5):
            updated_grid = update_grid(initial_grid.copy())
            self.assertNotEqual(updated_grid.tolist(), initial_grid.tolist(), "Grid should evolve over updates.")
            initial_grid = updated_grid
        
    def test_update_grid_edges(self):
        # Check if the grid evolves over multiple updates
        initial_grid = initialize_grid()
        for _ in range(5):
            updated_grid = update_grid(initial_grid.copy())
            self.assertNotEqual(updated_grid.tolist(), initial_grid.tolist(), "Grid should evolve over updates.")
            initial_grid = updated_grid

    
    def test_static_pattern(self):
        # Set a specific static pattern
        static_pattern = np.array([[1, 1],
                                   [1, 1]])
        initial_grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)
        initial_grid[2:4, 2:4] = static_pattern

        # After any update, the grid should remain the same
        updated_grid = update_grid(initial_grid.copy())
        np.testing.assert_array_equal(updated_grid, initial_grid, "Static pattern should remain unchanged.")

    def test_random_initialization(self):
        # Check if the grid evolves over multiple updates
        initial_grid = initialize_grid()
        for _ in range(5):
            updated_grid = update_grid(initial_grid.copy())
            self.assertNotEqual(updated_grid.tolist(), initial_grid.tolist(), "Grid should evolve over updates.")
            initial_grid = updated_grid

    def test_user_quit(self):
        # Simulate user quitting the game
        with self.assertRaises(SystemExit):
            with unittest.mock.patch('pygame.event.get', return_value=[pygame.event.Event(pygame.QUIT)]):
                main()

    def test_performance(self):
        # Measure time for a large grid with high iterations
        start_time = time.time()
        large_grid = np.random.choice([0, 1], size=(100, 100))
        for _ in range(100):
            large_grid = update_grid(large_grid.copy())
        elapsed_time = time.time() - start_time
        self.assertLess(elapsed_time, 1, "Performance test: Execution time should be reasonable.")

if __name__ == '__main__':
    unittest.main()
