Name = input("What is your gamertag? ")
class FortniteStats:
    def __init__(self, Platform, Level, Wins):
        self.Platform = Platform
        self.Level = Level
        self.Wins = Wins
    def printStats(self):
        print(Name+"'s "+"Platform: "+self.Platform+" ,Level: "+self.Level+" ,Wins this season: "+self.Wins)

Dex = FortniteStats("Xbox Series S", "Level 16", "3 Wins")
Patient = FortniteStats("Playstation 5", "Level 5", "1 Wins")
Kramer = FortniteStats("Playstation 5", "Level 30", "1 Wins")

if Name == "p4nda":
    Dex.printStats()
if Name == "Patient":
    Patient.printStats()
if Name == "Kramer":
    Kramer.printStats()