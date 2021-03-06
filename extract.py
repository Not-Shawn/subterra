import json
import random
import importlib

class Extract():
    def __init__(self, pkgs: list):
        self.data = {}

        self.tile = {}

        self.tilestack = []
        self.cardstack = []
        self.itemstack = []

        self.basactions = {}
        self.hazactions = {}

        self.characters = {}

        self.horrors = {}

        
        contents = ['actions', 'characters', 'items', 'tiles']

        for i in pkgs:
            self.JsonOpen(i)
            ac_pkg = importlib.import_module('packages.' + i + '.actions')
            ch_pkg = importlib.import_module('packages.' + i + '.characters')
            it_pkg = importlib.import_module('packages.' + i + '.items')
            ti_pkg = importlib.import_module('packages.' + i + '.tiles')
            self.basactions = {**self.basactions, **ac_pkg.BasicActions}
            self.hazactions = {**self.hazactions, **ac_pkg.HazardActions}
            self.characters = {**self.characters, **ch_pkg.Characters}
            self.horrors = {**self.horrors, **ch_pkg.HorrorType}
            self.tile = {**self.tile, **ti_pkg.TileType}
            

    def JsonOpen(self, x):
        with open("packages/"+ x + "/data.json", "r") as r:
            tempdata = json.load(r)
        if self.data == {}:
            self.data = tempdata
        else:
            for i in tempdata.keys():
                for j in tempdata[i].keys():
                    if j in self.data[i].keys():
                        for k in tempdata[i][j].keys():
                            if k in self.data[i][j].keys():
                                self.data[i][j][k] += tempdata[i][j][k]
                            else:
                                self.data[i][j][k] = tempdata[i][j][k]
                    else:
                        self.data[i][j] = tempdata[i][j]
    
    def StackSetUp(self, plyr, diff):
        shuf = 10
        
        if plyr == 4 :tempcard = 25
        elif plyr == 5: tempcard = 22
        elif plyr == 6: tempcard = 20
        else: raise Exception("Error")
        
        tempcard -= (2 * diff)

        for i in self.data["CaveTile"].keys(): #Normal
            if i not in ["StartTile", "ExitTile"]:
                for j in self.data["CaveTile"][i].keys(): #2s
                    for _ in range(int(self.data["CaveTile"][i][j])):
                        self.tilestack.append((i, j))

        for i in range(shuf):
            random.shuffle(self.tilestack)
        self.tilestack.insert(len(self.tilestack) - random.randint(0,4), ("Exit","4"))

        adv = [x for x in self.data["HazardCard"].keys() if "2" in x]

        for i in self.data["HazardCard"].keys(): 
            if i not in (adv + ["OutOfTimeCard"]):
                for j in range(int(self.data["HazardCard"][i])):
                    self.cardstack.append(i)

        if diff > 0:
            for i in random.sample(adv,(2 * diff) + 1):
                self.cardstack.append(i)
                
        for i in range(shuf):
            random.shuffle(self.cardstack)
        del self.cardstack[0:len(self.cardstack) - tempcard]
        self.cardstack.append("OutOfTimeCard")

    def Stack(self):
        return (self.tilestack, self.cardstack, self.itemstack)

if __name__ == "__main__":
    test = Extract(['Core'])
    test.basactions

        
                    
            



    

