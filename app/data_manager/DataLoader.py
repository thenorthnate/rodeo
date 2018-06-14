# Data Loader Class

import datetime
import os
import time


class DataLoader:
    def __init__(self, datadir):
        self.datadir = datadir
        self.tmpDatatypes = []
        self.datattributes = {}
        self.filename = ""

        self.tmpHeader = []
        self.datetimeTypes = [
            "%Y-%m-%d %H:%M:%S",
            "%Y/%m/%d %H:%M:%S",
            "%Y-%m-%d",
            "%Y/%m/%d",
            "%m/%d/%Y",
            "%m/%d/%y",
            "%m-%d-%Y",
            "%m-%d-%y",
            "%d%b%Y %H:%M:%S %p"
        ]

        # datattributes = {'Date':{'type':'datetime', 'fmt':'%Y/%m/%d', 'index':x}}

    def generate_filename(self):
        curTime = int(time.time()*1000)
        fileStarter = "rodeoin_"
        self.filename = fileStarter + str(curTime) + ".csv"

    def process_file_upload(self, requestFiles):
        if 'datafile' not in requestFiles:
            # No Files selected to upload.
            print('No file part.')
        else:
            f1 = requestFiles['datafile']
            if f1.filename == '':
                print('No Files Selected.')
            else:
                # Upload and save the files.
                self.generate_filename()
                f1.save(os.path.join(self.datadir, self.filename))

    def format_datapoint(self, dp, index):
        dp = dp.strip(" ")
        try:
            type = self.tmpDatatypes[index]["type"]
            typefmt = self.tmpDatatypes[index]["fmt"]
            if type == "float":
                try:
                    return float(dp)
                except ValueError:
                    return dp
            elif type == "int":
                try:
                    return int(dp)
                except ValueError:
                    return dp
            elif type == "datetime":
                try:
                    return datetime.datetime.strptime(dp, typefmt)
                except ValueError:
                    return dp
            else:
                return dp
        except IndexError:
            for fmt in self.datetimeTypes:
                try:
                    out = datetime.datetime.strptime(dp, fmt)
                    self.tmpDatatypes.append({"type": "datetime", "fmt": fmt})
                    return out
                except ValueError:
                    pass
            try:
                out = int(dp)
                self.tmpDatatypes.append({"type": "int", "fmt": None})
                return out
            except ValueError:
                pass
            try:
                out = float(dp)
                self.tmpDatatypes.append({"type": "float", "fmt": None})
                return out
            except ValueError:
                pass

        self.tmpDatatypes.append({"type": "str", "fmt": None})
        return dp

    def load_file(self):
        self.tmpHeader = []
        data = {}
        with open(self.datadir + self.filename, "r") as inputFile:
            i = 0
            for line in inputFile:
                row = line.strip("\n").split(",")
                if i == 0:
                    self.tmpHeader = row
                else:
                    for j in range(len(row)):
                        datapoint = self.format_datapoint(row[j], j)
                        try:
                            data[self.tmpHeader[j]].append(datapoint)
                        except KeyError:
                            data[self.tmpHeader[j]] = [datapoint]
                i += 1
        return data

    def create_data_to_show(self, data):
        showData = {}
        for item in data:
            showData[item] = []
            for i in range(10):
                showData[item].append(str(data[item][i]))
        return showData

    def load(self, requestFiles):
        self.process_file_upload(requestFiles)
        loadedData = self.load_file()
        showData = self.create_data_to_show(loadedData)
        return [loadedData, showData]
