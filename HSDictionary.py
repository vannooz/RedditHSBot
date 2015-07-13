import json
from pprint import pprint

supportedTypes = ("Minion", "Spell", "Weapon")
unsupportedCards = ("bite","sap","brawl","slam","snipe","claw") #unsupported cards as they are or are subsets of common words

class HearthstoneDictionary:
    def __init__(self, filePath) :
        with open(filePath) as data_file:
            self.index = self.createIndex(json.load(data_file))
        #pprint(self.index)
        self.jsonFilePath = filePath
    
    def getCard(self, name):
        return self.index[name.lower()]

    def createIndex(self, data) :
        index = {}
        for cartType in data.iterkeys():
            for card in data[cartType]:
                if card["type"] in supportedTypes :
                    key = card["name"].lower()
                    if key not in unsupportedCards:
                        index[key] = card
        return index

    def keys(self):
        return self.index.keys()
