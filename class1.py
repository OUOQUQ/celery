class car:
    def __init__(self,color,ck) -> None:
        self.cor = color
        self.ck = ck
    def check(self):
        print(f"This car is {self.cor} and, driver is {self.ck} wear ck")

mazda = car('yellow','yes')
mazda.check()
chdict={
    'people':5,
    'yearp':'',
    'ucc':30
}
if 'yearp' in chdict:
    print(chdict['ucc'])