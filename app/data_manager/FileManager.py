# File Manager Class
# Nathan North
# Handles all things to do with file management including:
# 1. Uploading files to the data directory
# 2. Reading a file into memory
# 3. Writing a file from memory
# 4. Renaming files, etc

import os
import pandas
import datetime


class FileManager:
    def __init__(self, datadir):
        self.datadir = datadir
        self.dataFiles = []
        self.otherFiles = []
        self.fileProperties = {}
        self.nextFileNum = -1

    def load_file_properties(self):
        pass

    def find_files(self):
        '''Finds all files in the datadir and loads the names'''
        allFiles = os.listdir(self.datadir)
        self.dataFiles = []
        maxFileNum = 0
        for item in allFiles:
            if item.endswith(".csv"):
                try:
                    tmpFileNum = int(item.strip(".csv"))
                    if tmpFileNum > maxFileNum:
                        maxFileNum = tmpFileNum
                    self.dataFiles.append(item)
                except ValueError:
                    self.otherFiles.append(item)
            else:
                self.otherFiles.append(item)
        self.nextFileNum = maxFileNum + 1

    def upload_file(self, request):
        '''Uploads a file from the users computer to the working directory of the app'''
        # TODO: Create JSON file with file properties in it!
        rFiles = request.files
        if 'datafile' not in rFiles:
            print('No file part.')
        else:
            f1 = rFiles['datafile']
            if f1.filename == '':
                print('No Files Selected.')
            else:
                filename = str(self.nextFileNum) + ".csv"
                self.nextFileNum += 1
                uploadDateTime = datetime.datetime.now()
                uploadDateTimeString = uploadDateTime.strftime("%Y/%m/%d %H:%M:%S")
                self.fileProperties[filename] = {"name": f1.filename, "uploadTime": uploadDateTimeString}
                f1.save(os.path.join(self.datadir, filename))

    def read_file(self, filename):
        '''Reads a file into memory'''
        data = pandas.read_csv(self.datadir + filename, skipinitialspace=True)
        for item in data:
            try:
                data[item] = pandas.to_numeric(data[item])
            except ValueError:
                try:
                    data[item] = pandas.to_datetime(data[item])
                except ValueError:
                    pass
        return data

    def write_file(self, filename):
        pass
