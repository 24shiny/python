from random import randint

class Die:
    def __init__(self,side):
        self.side = side
        self.rand_num = 0

    def roll_die(self):
        return randint(1,self.side)
    
dice6 = Die(6)
dice6_record = []
for i in range(10):
    dice6_record.append(dice6.roll_die())
print(dice6_record)

dice10 = Die(10)
dice10_record = []
for i in range(10):
    dice10_record.append(dice10.roll_die())
print(dice10_record)

dice20 = Die(20)
dice20_record = []
for i in range(10):
    dice20_record.append(dice20.roll_die())
print(dice20_record)
