import hashlib


class FR_Report:
    def __init__(self):
        self.classification = ""
        self.serial_number = ""
        self.title = ""
        self.date_report = ""
        self.date_event = ""
        self.date_saved = ""
        self.url_source = ""
        self.url_saved = ""
        self.urls_referred = []
        self.dm_capabilities = []
        self.dm_infrastructure = []
        self.dm_victim = []
        self.dm_attacker = []
        self.words_cloud = []
        self.named_entities = []
        self.analytical_notes = ""
        self.product_id = ""

    def loadFromList(self, row):
        dicVars = vars(self)

        i = 0
        for key, value in dicVars:
            vars(self)[key] = row[i]
            i += 1

    def getProductID(self):
        allText = self.serial_number + self.title + self.date_report + self.url_saved
        self.product_id = hashlib.sha1(bytearray(allText.encode(encoding="utf-8"))).hexdigest()
        return self.product_id

    def getReportDatabaseDefinitionList(self) -> str:
        lstVariables = list(vars(self).keys())

        #This object will be all TEXT, so little tweak here for that, in other instance
        #where INT, are going to be used, we'll need to adjust on a case per case
        strRes = " TEXT, ".join(lstVariables)

        return strRes

    def getReportDefinitionList(self) -> list:
        return list(vars(self).keys())

    def getReportValuesList(self) -> list:
        dicVars = vars(self)

        for key, value in dicVars.items():
            if type(value) == list:
                dicVars[key] = ",".join(value)

        return list(dicVars.values())

