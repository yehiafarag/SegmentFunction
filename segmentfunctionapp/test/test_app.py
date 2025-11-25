from unittest import TestCase

from segmentfunctionapp.main.app import App


class TestApp(TestCase):
    """
Unit tests for the segment-function-app App class.

These tests verify correct computation of segment_overlap between two segment files, calculation of sample pearson correlation coefficient between two function files and calculating mean for function values based on
entries indexed by segment regions.
"""


    def setUp(self):
        """
        Initial set up for data used in the tests, the data provided by the task guid-line
        """
        self.app=App()
        self.segment_1_list = [[1, 2], [3, 6]]
        self.segment_2_list = [[0, 1], [1, 5]]
        self.function_1_list = [10.0,11.0,12.0,13.0,14.0,15.0,16.0]
        self.function_2_list = [10.5,11.5,12.0,13.0,13.5,15.0,14.0]


    def test_calculate_segment_overlap(self):
        """
          Test segment overlap when the input is 2 sigments
        """
        self.app.calculate_segment_overlap(self.segment_1_list,self.segment_2_list)
        self.assertEqual(self.app.segment_overlap_list,{1, 3, 4})

    def test_calculate_sample_pearson_correlation_coefficient(self):
        """
          Test sample pearson correlation coefficient when the input is 2 functions
        """
        pearson_correlation_coefficient=  self.app.calculate_sample_pearson_correlation_coefficient(self.function_1_list,self.function_2_list)
        print(pearson_correlation_coefficient)
        self.assertAlmostEqual(pearson_correlation_coefficient,0.9452853)


    def test_compute_function_mean_segments(self):
        """
          Test calculated function means based on segments when the input is 1 function file and 1 segment file
        """
        function_mean = self.app.compute_function_mean_segments(self.segment_1_list,self.function_2_list)
        self.assertAlmostEqual(function_mean,13.25)
