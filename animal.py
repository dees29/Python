print("In animal.py from "+ __name__)

def printanimal(animalname):
    print("in PRINTANIMAL FUNCTION when called from " + __name__)
    print("Animal is/are : ", animalname)
   

if __name__ == "__main__":
    printanimal("All Animals")
    print ("animal.py is directly run")
    
if __name__ == "animal":
    print ("animal.py is imported")