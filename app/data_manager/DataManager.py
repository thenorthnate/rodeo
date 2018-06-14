# Import Data Class Methods
# Nathan North


from app.main.Main import Main
from app.data_manager.DataLoader import DataLoader


class DataManager(Main):
    data = {}
    datattributes = {}
    showData = {}

    def __init__(self):
        Main.__init__(self)

    def import_new_file(self, requestFiles):
        DL = DataLoader(Main.datadir)
        [newData, self.showData] = DL.load(requestFiles)
        for item in newData:
            if item not in self.data:
                self.data[item] = newData[item]
            else:
                for entry in newData[item]:
                    self.data[item].append(entry)

    def get_data_properties(self):
        featureCount = 0
        for item in self.data:
            tmp = {}
            for entry in self.data[item]:
                tmp[str(entry)] = 0
            self.datattributes[item] = {"uniqueEntries": len(tmp)}
            featureCount += 1

        self.datattributes["all"] = {"featureCount": featureCount}

    def clear_all_data(self):
        self.data = {}
