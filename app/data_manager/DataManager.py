# Import Data Class Methods
# Nathan North


from app.main.Main import Main
from app.data_manager.DataLoader import DataLoader


class DataManager(Main):
    def __init__(self):
        Main.__init__(self)
        # {"filename.csv":{"data":{"header":{"data":[data, data, data, ...]}, "properties":{"uniqueEntries":12, "type":"float"}, "fileProperties":{"features":10, "length":1234}}, ...}
        self.data = {"files": []}
        self.tmpData = {}
        self.operations = {}  # {"projectName":[{"task":1, "type":"importData", "filename":"abc.csv"}, {"task":2, "type":"newFeature", "operation":"date1 - date2", "operationName":"timeDiff"},...]}

    def import_new_file(self, requestFiles):
        DL = DataLoader(Main.datadir)
        newData = DL.load(requestFiles)  # {"header":[data, data, ...]}
        self.data["files"].append(DL.filename)
        self.data[DL.filename] = {"data": {}, "fileProperties": {}}
        for item in newData:
            self.data[DL.filename]["data"][item] = {"data": newData[item], "properties": {"type": DL.datattributes[item]["type"]}}

    def import_old_file(self):
        pass

    def get_data_properties(self):
        featureCount = 0
        for item in self.data:
            tmp = {}
            for entry in self.data[item]:
                tmp[str(entry)] = 0
            # self.datattributes[item] = {"uniqueEntries": len(tmp)}
            featureCount += 1

        self.datattributes["all"] = {"featureCount": featureCount}

    def clear_all_data(self):
        self.data = {}
        self.tmpData = {}

    def test_plot(self):
        data = self.data[self.data["files"][0]]["data"]
        i = 0
        for header in data:
            print(data[header]["properties"]["type"])
            if data[header]["properties"]["type"] in ["float", "int"]:
                self.tmpData[str(i)] = data[header]["data"]
                i += 1
