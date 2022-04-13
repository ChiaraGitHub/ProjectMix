import unittest
import pandas as pd
from data_loader.data_loader import DataLoader


class DataLoaderTest(unittest.TestCase):

    def test_data_loader(self):

        data_loader = DataLoader()
        df = data_loader.get_data()
        df_test_result = pd.DataFrame([[1,2,3], [4,5,6]], columns = ['a', 'b','c'])
        self.assertEqual(df.mean().mean(), df_test_result.mean().mean())