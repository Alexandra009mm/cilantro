'''print("\n -----Welcome-----")  
print("\n Sales sistem")''' #ejercicio 1

#ejercicio 2
'''product_name = "limonada de coco"
price = 10000
quantity = 4

print(product_name)
print(price)
print(quantity)'''

#ejercicio 3

#esto es version 1 con conversion a float y mostrar decimales
'''product_name = input("please enter the product name => ")
price = float(input('please enter the price =>            '))
quantity = int(input('whant is the amount?=>              '))

total = price * float(quantity)

print('----your sales----')
print(f'your product name: {product_name}')
print(f'the price: {price:.2f}')
print(f'quantity : {quantity}')
print(f'the total of your sales is : {total}')'''

#version 2 probando sin el float y sin el :.2f de los decimales
'''product_name = input("please enter the product name => ")
price = float(input('please enter the price =>            '))
quantity = int(input('whant is the amount?=>              '))

total = price * quantity ''' #si le quito  el float es la misma vaina, python conviertepor si solo a int en float para
#hacer la multiplicacion por lo tanto no es necesario que convierta manualmete a int por float en la multiplicacion 

''''print('----your sales----')
print(f'your product name: {product_name}')
print(f'the price: {price}')
print(f'quantity : {quantity}')
print(f'the total of your sales is : {total}')'''

#ejercicio 4
general_total = []
activo = 'yes'

def show_general_balance():
    total = 0

    for i in general_total:
        total = total + i

    print(total)


sgb = show_general_balance

while activo:
    product_name = input("please enter the product name => ")
    price = float(input('please enter the price =>         '))
    quantity = int(input('what is the amount?=>            '))
    total = price * quantity 
    
    
   
    if total > 10000:
        print(f'the total of your sales is {total}')
        print("Big discount")
        

    elif total > 5000:
        print(f'the total of your sales is {total}')
        print("Discount applied")
     

    elif total <= 5000:
        print(f'the total of your sales is {total}')
        print('No discount')


    general_total.append(total)
    question =  activo = input("do you want to make another sale? yes/no ").lower() 

question == 'no'
print("\n ~Thank you for using the sales register~")
print("\nThe total sales you made are:")
sgb()
