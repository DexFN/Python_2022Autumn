class Cars: #創立類別
    #建構式
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat
    
    def move(self, meter):
        print("My car can move "+str(meter)+" meters as long as I have enough gas")
    def printAttritbute(self):
        print("My car's color is "+self.color)
        print("My car has "+str(self.seat)+" seats")

audi = Cars("blue", 4)
audi.move("∞") #呼叫方法
audi.printAttritbute()

# audi = Cars() #創立物件
# #print(isinstance(audi, Cars)) #判斷類別與物件的關係

# #建立屬性
# audi.color = "blue" 
# audi.seat = 4 

# #呼叫屬性
# print(audi.color)
# print(audi.seat)

class FullName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printName(self):
        print("My name is "+self.firstname+", "+self.lastname)

Name1 = FullName("Andy", "Wang")
Name2 = FullName("Lulu", "Cheng")
Name1.printName()
Name2.printName()

# print(Name1.firstname, Name1.lastname)
# print(Name2.firstname, Name2.lastname)

