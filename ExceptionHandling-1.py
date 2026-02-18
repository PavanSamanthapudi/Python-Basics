
val_1 = input("Enter the value : ")

def add(a,val):
    print("Starting the Try block")
    try:
       print(a+val)
    except:
        print("Error in calculation, handling it through type casting")
        print(a+float(val))

add(100, val_1)