import os  
from DataResources import *
import requests
import logging

class Data:
    """
    Gets the data from the url used in the constructor
    
        Url: url public of data to download 
        Name: file name of the download data
    """

    Url: str = "" 
    Name: str = ""
    _fileName_: str = ""
    _fileNameCompressed_: str = ""
    _fileNamePath_:str = ""
    _fileNameCompressedPath_:str = ""

    def __init__(self, url:str, name:str):
        self.Url = url
        self.Name = name
        logging.info("Init %s" % name)
        self._fileName_ = FILE_NAME % (self.Name)
        self._fileNameCompressed_ = FILE_NAME_COMPRESSED % (self._fileName_)

        self._fileNamePath_ = FILE_PATH % (DATA_PATH, self._fileName_)
        self._fileNameCompressedPath_ = FILE_PATH % (DATA_PATH, self._fileNameCompressed_)

    def getData(self):
        """
        Manage the  data: download and place it on local folder
        """
        self._existName()
        self._existUrl()
        logging.info("getData for %s " % self.Name)
        if not (self._existData()):
            self._existDataCompressed()

    def _existData(self):
        logging.info("_existData for %s " % self._fileNamePath_)
        return os.path.exists(self._fileNamePath_)    

    def _existDataCompressed(self):
        logging.info("_existDataCompressed for %s " % self._fileNameCompressedPath_)
        if not (os.path.exists(self._fileNameCompressedPath_)):
            if not (os.path.exists(DATA_PATH)):
                os.mkdir(DATA_PATH)
            self._downloadData()

    def _downloadData(self): 
        logging.info("_downloadData for %s " % self._fileNameCompressedPath_)
        fileDownloaded = requests.get(self.Url)
        fileInLocalDescription =  os.open(self._fileNameCompressedPath_, os.O_RDWR | os.O_CREAT )
        os.write(fileInLocalDescription, fileDownloaded.content)
        os.close(fileInLocalDescription)
        return True

    def _existName(self):
        if ( self.Name.isspace() ):
            raise Exception("A name for the data is needed") 

    def _existUrl(self):
        if ( self.Url.isspace() ):
            raise Exception("A url for the download is needed") 