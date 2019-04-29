import logging
import os

import requests

from DataResources import *


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
    _fileNamePath_: str = ""
    _fileNameCompressedPath_: str = ""

    def __init__(self, url: str, name: str):
        self.Url = url
        self.Name = name
        logging.info("Init %s" % name)
        self._fileName_ = FILE_NAME % self.Name
        self._fileNameCompressed_ = FILE_NAME_COMPRESSED % self._fileName_

        self._fileNamePath_ = FILE_PATH % (DATA_PATH, self._fileName_)
        self._fileNameCompressedPath_ = FILE_PATH % (DATA_PATH, self._fileNameCompressed_)

    def get_data(self):
        """
        Manage the  data: download and place it on local folder
        """
        self._exist_name()
        self._exist_url()
        logging.info("get_data for %s " % self.Name)
        if not (self._exist_data()):
            self._exist_data_compressed()

    def _exist_data(self):
        logging.info("_exist_data for %s " % self._fileNamePath_)
        return os.path.exists(self._fileNamePath_)

    def _exist_data_compressed(self):
        logging.info("_exist_data_compressed for %s " % self._fileNameCompressedPath_)
        if not (os.path.exists(self._fileNameCompressedPath_)):
            if not (os.path.exists(DATA_PATH)):
                os.mkdir(DATA_PATH)
            self._download_data()

    def _download_data(self):
        logging.info("_download_data for %s " % self._fileNameCompressedPath_)
        file_downloaded = requests.get(self.Url)
        file_in_local_description = os.open(self._fileNameCompressedPath_, os.O_RDWR | os.O_CREAT)
        os.write(file_in_local_description, file_downloaded.content)
        os.close(file_in_local_description)
        return True

    def _exist_name(self):
        if self.Name.isspace():
            raise Exception("A name for the data is needed")

    def _exist_url(self):
        if self.Url.isspace():
            raise Exception("A url for the download is needed")
