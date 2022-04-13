import unittest
import pandas as pd
from data_loader.data_loader import DataLoader


def test_data_loader():

    data_loader = DataLoader()
    df = data_loader.get_data()
    df_test_result = pd.DataFrame([[1,2,3], [4,5,6]], columns = ['a', 'b','c'])
    assert df.mean().mean() == df_test_result.mean().mean()