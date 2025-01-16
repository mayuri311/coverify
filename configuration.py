import configparser


class configuration:
    def __init__(self, configFile):
        self.configFile = configFile
        self.parser = configparser.ConfigParser()

    def readSection(self, sectionName):
        self.parser.read(self.configFile)
        cfg = self.parser[sectionName]
        return cfg
