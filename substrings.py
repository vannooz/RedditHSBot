import json
from pprint import pprint

supportedTypes = ("Minion", "Spell", "Weapon")

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
                if card["type"] in supportedTypes and card.get("collectible") == True:
                    index[card["name"].lower()] = card
        return index

    def keys(self):
        return self.index.keys()
    
    def printAll(self):
        for key1 in self.index.keys() :
            for key2 in self.index.keys():
                if key1.find(key2) > 0:
                    print key1 + " contains " + key2
                    #pprint (self.index.get(key2))

    def printSmallNames(self):
        for key in self.index.keys() :
            if(len(key)<6):
                print key

hsDict = HearthstoneDictionary("AllSets.enUS.json")

#hsDict.printAll()

hsDict.printSmallNames()