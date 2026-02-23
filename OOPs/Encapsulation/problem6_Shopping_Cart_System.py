class Cart:
    def __init__(self):
        self.__cart={}
    def Add_item(self,name,price):
        self.__cart.update({name:price})

    def Show_items(self):
        for k,v in self.__cart.items():
            print(k,":",v)
    def Remove_items(self,name):
        self.__cart.pop(name)
    def Show_total(self):
        total=0
        for values in self.__cart.values():
            total+=values
        return total
sp1=Cart()

sp1.Add_item("chips",10)
sp1.Add_item("cake",20)
sp1.Show_items()
print(sp1.Show_total())
print("After Remove item")
sp1.Remove_items("chips")
sp1.Show_items()
print(sp1.Show_total())