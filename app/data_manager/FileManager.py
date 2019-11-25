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
import json


class FileManager:
    def __init__(self, pwd):
        self.pwd = pwd
        self.datadir = pwd + "/data/"
        self.dataFiles = []
        self.otherFiles = []
        self.fileProperties = {}
        self.nextFileNum = 0

        self.read_file_properties()

    def read_file_properties(self):
        try:
            with open(self.pwd + "/app/settings/fileproperties.json", "r") as inputFile:
                self.fileProperties = json.load(inputFile)
        except FileNotFoundError:
            pass
        maxFileNum = -1
        for item in self.fileProperties:
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

    def clean_data_directory(self):
        # should move all file numbers down to the lowest they can be, update the file properties
        # and delete any files that aren't in the file properties

        # Also deletes from file properties if file not found but is in the properties file
        pass

    def write_file_properties(self):
        with open(self.pwd + "/app/settings/fileproperties.json", "w") as outputFile:
            json.dump(self.fileProperties, outputFile)

    def upload_file(self, request):
        '''Uploads a file from the users computer to the working directory of the app'''
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
                f1.save(os.path.join(self.pwd + "/data/", filename))
                self.write_file_properties()

    def read_file(self, filename):
        '''Reads a file into memory'''
        data = pandas.read_csv(self.pwd + "/data/" + filename, skipinitialspace=True)
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
