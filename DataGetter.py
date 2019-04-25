from DataResources import * 
from Data import Data 

class DataGetter:
    Train:Data = None
    Test:Data = None

    def __init__(self):
        self.Train = Data(url=URL_TRAIN, name=TRAIN_NAME)
        self.Test = Data(url=URL_TEST, name=TEST_NAME )
    
    def getData(self):
        self.Train.getData()
        self.Test.getData()