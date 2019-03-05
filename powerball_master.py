import random

fsn = []
ots = []

fsn = [i for i in range(1, 70)]
ots = [i for i in range(1, 27)]

def drawing(n=1):
    i = 1
    while i < n + 1:
         print(random.sample(fsn, 5), random.sample(ots, 1))
         i += 1
    
if __name__=="__main__":
    try:
        repeat = int(input("How many drawings would you like? "))
        if repeat > 0:
            drawing(repeat)
        else:
            print("You need to provide positive number")
    except:
        pass
