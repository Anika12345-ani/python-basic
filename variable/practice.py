##variable
customer_name = "aNika"
#converted = (customer_name.title())
print(customer_name.title())
print((customer_name.upper()))
print((customer_name.lower()))

##dictionary
#customer_age = {
    #'anika' : 20,
    #'aika' : 30,
    #'anik' :40,

customer_address = {
    'anika' : 'mirpur6',
   'aika' : 'mirpur2',
    'anik' : 'mirpur10',

}
for name in customer_address.keys():
    print(name.title())

#for age in customer_age.values():
    #print(age)

for address in customer_address.values():
        print(address.title())

for name, address in customer_address.items():
        print(f"hello my name is {name.title()} \n i am from {address.title()}.")

   ##if condition
cars = ['audi', 'bmw', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'
if requested_topping == 'anchovies':
         print("Hold the anchovies!")

serial_numbers = [6,9,1,2,100,120,140,101]
serial_numbers.sort()
print(serial_numbers)

serial_numbers.reverse()
print(serial_numbers)

serial_numbers.remove(100)
print(serial_numbers)

answer = 17
if answer != 45:
     print("That is not the correct answer. Please try again!")
age = 20
if age >= 18:
     print("You are old enough to vote!")

age = 20
if age >= 18:
         print("You are old enough to vote!")
         print("Have you registered to vote yet?")
else:
         print("Sorry, you are too young to vote.")
         print("Please register to vote as soon as you turn 18!")

age = 15
if age < 4:
             print("Your admission cost is $0.")
elif age < 18:
             print("Your admission cost is $25.")
else:
            print("Your admission cost is $40.")

age = 18
if age < 4:

            price = 0
elif age < 18:

            price = 25
else:

            price = 40

            print(f"Your admission cost is ${price}.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
     price = 20
print(f"Your admission cost is ${price}.")


available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
       print(f"Adding {requested_topping}.")
    else:
       print(f"Sorry, we don't have {requested_topping}.")


print("\nFinished making your pizza!")




