

def mario():
    
    while True:
        height = input("Input height of pyramid as a positive integer")
        if int(height) >= 0 and height.isdigit():
            break
        
        print("Invalid input, please try again")


    n = int(height)
    if int(height) <= 0:
        return
    for i in range(1,(n+1)):
        print("#"*i)
    print("\n")



mario()