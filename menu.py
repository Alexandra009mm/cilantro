from mm import register
from mm import general_total
from mm import show_general_balance as sgb
from mm import info_sales

def menuu():
    print("\n---------𝐌𝐞𝐧𝐮----------")
    print("1. Enter register a sales => ")
    print("2. show total sales =>  ")
    print("3. show history => ")
    option = input("enter your option: ")

    try:
        if option == "1":
            register()

        elif option == "2":
            general_total
            sgb()

        elif option == "3":
            print(info_sales)

    except TypeError: 
        option = input("Enter: 1, 2 or 3. Try again =>    ")

