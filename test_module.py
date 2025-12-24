import unittest
import sea_level_predictor
import matplotlib


class SeaLevelPredictorTestCase(unittest.TestCase):

    def test_plot_exists(self):
        ax = sea_level_predictor.draw_plot()
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_plot_labels(self):
        ax = sea_level_predictor.draw_plot()
        self.assertEqual(ax.get_xlabel(), "Year")
        self.assertEqual(ax.get_ylabel(), "Sea Level (inches)")
        self.assertEqual(ax.get_title(), "Rise in Sea Level")


if __name__ == "__main__":
    unittest.main()
