from registro import register, general_total, show_general_balance, inventory

def menu():

    act = True
    while act:
        print(" ")
        print("\n---------𝐌ENU----------")
        print(" ")
        print("1. Add product => ")
        print("2. Calculate statistics =>")
        print("3. Show inventory => ")
        print("4. Exit => ")
        print(" ")
        option = input("enter your option: ")
        if option == "1":
                register()

        elif option == "2":
            general_total
            show_general_balance()

        elif option == "3":
            if inventory== None:
                  print("The inventory is empty")
            
            else:
                print("\n ===============𝐈𝐍𝐕𝐄𝐍𝐓𝐎𝐑𝐘=============== \n")
                for i in inventory:
                    print(f"Product name: {i['product_name']} | price: {i['price']} |   quantity: {i['quantity']}")
                    print("\n" + "=" * 41)
            
        elif option == "4":
             act = False
             print("Thanks you for use \n ----The register sales----\n")
    
        else:
            print("Enter: 1, 2, 3 or 4. Try again =>    ")
            continue


