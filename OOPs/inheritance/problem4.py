class Father:
    def skill(self):
        print("Pasinate to car!")

class Mother:
    @staticmethod  #staticmethod decorator to use avoid (self) as a argument
    def talent():
        print("Pasinate to cook!")

class Child(Father,Mother):
    def gifted(self):
        print("from the father and mother!")

c1=Child()
c1.skill()
c1.talent()