class person :
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome",self.firstname,self.lastname,
              "to the class of ",self.graduationyear)
play1=person('Bill','Gates')
play1.printname()

play2=student('Elon','Musk',2019)
play2.welcome()

