# import os 
# os.remove("practic.txt")
def finding():
    with open("practice.txt","r") as f:
        data=f.read()
        i=0
        if "mango" in data:
            print("Found")
        else:
            print("Element not Found")

finding()
    