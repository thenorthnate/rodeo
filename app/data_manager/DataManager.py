# Manage Data Class Methods
# Nathan North


from app.data_manager.FileManager import FileManager
from app.data_manager.DataLoader import DataLoader


class DataManager():
    def __init__(self, pwd):
        self.pwd = pwd
        # {"filename.csv":{"data":{"1":{"data":[data, data, data, ...]}, "properties":{"uniqueEntries":12, "type":"float", "name":"xxx"}, "fileProperties":{"features":10, "length":1234}}, ...}
        self.data = {"files": []}
        self.tmpData = {}
        self.operations = {}  # {"projectName":[{"task":1, "type":"importData", "filename":"abc.csv"}, {"task":2, "type":"newFeature", "operation":"date1 - date2", "operationName":"timeDiff"},...]}
        self.fm = FileManager(pwd)

    def upload_file(self, request):
        self.fm.upload_file(request)

    def import_new_file(self, requestFiles):
        DL = DataLoader(self.datadir)
        newData = DL.load(requestFiles)  # {"header":[data, data, ...]}
        self.data["files"].append(DL.filename)
        self.data[DL.filename] = {"features": {}, "fileProperties": {}}
        i = 0
        for item in newData:
            self.data[DL.filename]["features"][str(i)] = {
                "data": newData[item],
                "properties": {"type": DL.datattributes[item]["type"]},
                "name": item
            }
            i += 1

    def load_data(self):
        pass

    def clear_all_data(self):
        self.data = {}
        self.tmpData = {}

    def test_plot(self):
        for fileItem in self.data:
            if fileItem != "files":
                data = self.data[fileItem]["features"]
                i = 0
                for header in data:
                    if data[header]["properties"]["type"] in ["float", "int"]:
                        self.tmpData[str(i)] = data[header]["data"]
                        i += 1
