#Enter the price of the House you wish to Buy
print("Enter the house price: ")
price = int(input())
#Enter the credit score
print("Enter the credit score: ")
CreditScore = int(input())
#Enter the first name
print("Enter the first name: ")
first_name = input()
#Enter the last name
print("Enter the last name: ")
last_name = input()
fullnames = first_name + " & " + last_name
#Enter the email
print("Enter the email address")
email = input()
#Enter the phone number
print("Enter the phone number")
phone = input()
#Enter the mailing
print("Enter the mailing address")
mailing = input()
#Enter the mailing
print("Enter the City")
city = input()
print("Enter state")
state = input()
#Enter the mailing
print("Enter the zip code")
zipcode = input()
#Qualify for loans with the best interest rates
if CreditScore >= 780 and 850:
    CreditStatus = "Excent Credit"
    print("Zero Down Payment")
    downPayment = 0.0 * price
#Usually qualify for loans with the best interest rates
elif CreditScore >= 740 and 779:
    CreditStatus = "Very Good"
    downPayment = 0.2 * price
    #May face slightly higher loan Interest rates
elif CreditScore >= 720 and 739:
    CreditStatus ="Above Average"
    downPayment = 0.3 * price
    #May qualify for most loans of higher interest rates
elif CreditScore >= 680 and 719:
    CreditStatus = "Average"
    downPayment = 0.6 * price
    #May qualify for most loans at significant higher Interest rates
elif CreditScore >= 620 and 679:
    CreditStatus ="Below Average"
    downPayment = 0.18 * price
    #Usually has some credit issues; will probably not qualify for most loans
elif CreditScore >= 580 and 619:
    CreditStatus = "Poor Credit Score"
    downPayment = 0.20 * price
    #Facing extreme credit issue
elif CreditScore < 520:
    CreditStatus = "Poor Credit Score"
    downPayment = 0.25 * price

print("First Name:", first_name)
print("physical Address:",mailing)
print("City:",city,"State:",state,"zipcode:",zipcode)
print()
print("New House price:",price)
print("Down Payment:",downPayment)
print("Credit Score:",CreditScore)
print("Credit Status:",CreditStatus)
print()
#print("CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME -",first_name,"&",last_name)
print("CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME -",fullnames)
