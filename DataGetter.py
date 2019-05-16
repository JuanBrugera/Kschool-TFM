from Data import Data
from DataResources import *


class DataGetter:
    Train: Data = None
    Test: Data = None

    def __init__(self):
        self.Train = Data(url=URL_TRAIN, name=TRAIN_NAME)
        self.Test = Data(url=URL_TEST, name=TEST_NAME)

    def get_data(self):
        self.Train.get_data()
        self.Test.get_data()
