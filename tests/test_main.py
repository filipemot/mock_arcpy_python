import unittest
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):
    @patch('main.arcpy.da.SearchCursor')
    def test_get_results(self, spy_search_cursor):
        spy_search_cursor.return_value = [['Teste1'], ['Teste2']]
        return_values = main.search_results("feature_class")
        self.assertEqual(len(return_values), 2)
        self.assertEqual(return_values[0], 'Teste1')
        self.assertEqual(return_values[1], 'Teste2')

