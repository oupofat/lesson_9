'''Price of the Ride
A carnival ride costs $12.00 for adults; $6 for kids (12 or under); $7 for senior citizens (60 or older). You have to be at least 48 inches to ride.

Write a function price_of_the_ride(age, height). It has two parameters:

age - a number representing the age of the person
height - a number representing the height of the person
Its return value depends:

If they qualify to ride, it should return the cost of the ride as a number. If they do not qualify to ride, the function should return None.

Write some extra code to test this function and verify that it works properly.'''

def price_of_the_ride(age, height):
    if height <="48":
        print ("You are to short!")
    elif age >= "60":
        print ("Your cost is $7.00.")
    elif age >="12":
        print ("Your cost is $12.00.")
    elif age <="12":
        Print ("Your cost is $6.00.")
        
age = input("How old are you?(age)")
height = input("How tall are you? (height)")
price_of_the_ride(age, height)