'''Calculate Tips
Write a calculate_tip(amount, service) function that calculates gives the amount of the tip given the amount of the bill and the quality of the service. It has two parameters:

amount - a number representing the amount of the bill
service - a string which can be one of "good", "fair", and "poor". For good service, 20% tip should be given; for fair service, 15% tip should be given; and for poor service, 10% tip should be given.
Return value: a number representing the tip amount.

After you've written this function. Write some extra code to test this function and verify that it works properly.'''

def calculate_tip(amount,service):
    if service == "20":
        tip = .20 * amount
    elif service == "15":
        tip = .15 * amount
    elif service == "10":
        tip = .10 * amount
    print ("The tip is %.2f"% tip)
    return (tip)
amount = float(input("how much did you spend on the meal"))
service = input("how was the service (20=good,15=fair,10=poor)")

calculate_tip(amount,service)


