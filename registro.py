info_sales = []
general_total = []  #ejercicio 4


def show_general_balance():
    total = 0

    for i in general_total:
        total = total + i

    print(total)
 
def register():
    activo = "yes"
    while activo == "yes":

        print("--------------------------------------------------")
        product_name = input("please enter the product name =>   ")
        print("--------------------------------------------------")
        price = float(input('please enter the price =>           '))
        print("--------------------------------------------------")
        quantity = int(input('what is the amount?=>              '))
        total = price * quantity 

        diccionario = {
            "product name": product_name,
            "price": price,
           "quantity": quantity
        } 

        info_sales.append(diccionario)
       

        if total > 10000:
            print("--------------------------------------------------")
            print(f'the total of your sales is {total}')
            print("--------------------------------------------------")
            print("Big discount")
            print("--------------------------------------------------")

        elif total > 5000:
            print("--------------------------------------------------")
            print(f'the total of your sales is {total}')
            print("--------------------------------------------------")
            print("Discount applied")
            print("--------------------------------------------------")
        

        elif total <= 5000:
            print("--------------------------------------------------")
            print(f'the total of your sales is {total}')
            print("--------------------------------------------------")
            print('No discount')
            print("--------------------------------------------------")


        general_total.append(total)
        activo = input("do you want to make another sale? yes/no ").lower() 
    