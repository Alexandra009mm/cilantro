from registro import register, general_total, show_general_balance, info_sales

def menu():

    act = True
    while act:
        print(" ")
        print("\n---------𝐌ENU----------")
        print(" ")
        print("1. Enter register a sales => ")
        print("2. show total sales =>  ")
        print("3. show history => ")
        print("4. Exit => ")
        print(" ")
        option = input("enter your option: ")
        if option == "1":
                register()

        elif option == "2":
            general_total
            show_general_balance()

        elif option == "3":
             print(info_sales)
            
        elif option == "4":
             act = False
             print("Thanks you for use \n ----The register sales----\n")
    
        elif option != "1" or "2" or "3" or "4": 
            print("Enter: 1, 2 or 3. Try again =>    ")
            continue

