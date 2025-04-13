def cash():

    change = int(input("Insert amount of change expected"))

    cents = [25,10,5,1]
    denomination = ["Quarters", "Dime", "Nickels", "Pennies"]
    count = 0
    coins_count =[]

    for i in range(len(cents)):
        count = change // cents[i]
        change = change % cents[i]
        coins_count.append(count)
        print(f"Number of {denomination[i]}: {count}")

    total = sum(coins_count)
    print("Number of coins: ",total)

cash()
