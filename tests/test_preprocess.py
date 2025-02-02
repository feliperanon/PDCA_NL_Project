# G:\Meu Drive\Programação\PDCA_NL\PDCA_NL_Project\tests\test_preprocess.py

import unittest
import pandas as pd
from src.data_preprocessing.preprocess import preprocess_data

class TestPreprocessData(unittest.TestCase):
    def test_fillna(self):
        data = {'col1': [1, None, 3], 'col2': [None, 2, 3]}
        df = pd.DataFrame(data)
        result = preprocess_data(df)
        self.assertFalse(result.isnull().values.any())

if __name__ == '__main__':
    unittest.main()