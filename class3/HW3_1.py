Info = input("Who's info do you want to see? ")
class People:
    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight 
        self.age = age
    def printInfo(self):
        print(Info+"'s "+" height is "+self.height+", weight is "+self.weight+", age is "+self.age)

Dad = People("175cm", "65kg", "52 years-old")
Mom = People("154cm", "58kg", "52 years-old")
Sister = People("164cm", "56kg", "18 years-old")
Me = People("152cm", "41kg", "12 years-old")

if Info == "Jason":  
    Dad.printInfo()
if Info == "Judy":
    Mom.printInfo()
if Info == "Lulu":
    Sister.printInfo()
if Info == "Louie":
    Me.printInfo()