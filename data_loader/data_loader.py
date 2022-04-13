import pandas as pd

class DataLoader:

    def __init__(self):

        self.data = pd.DataFrame

    def get_data(self):

        self.data = pd.DataFrame([[1,2,3], [4,5,6]], columns = ['a', 'b','c'])
        return self.data