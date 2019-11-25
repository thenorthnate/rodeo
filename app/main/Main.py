# Generic Methods
# Nathan North

import os
from app.data_manager.DataManager import DataManager


class Main:
    def __init__(self):
        self.pwd = os.getcwd()
        self.extensions = set(['csv'])

        # Application Object Initializations
        self.dm = DataManager(self.pwd)
