#Enter Full Names
print("Enter First and Last Name:")
fname = input("fname :") #First Name
lname = input("lname :") #last Name
fullnames = fname + " " + lname

#Enter phone, email
print("Enter Customer's Phone Number: ")
phone = input("phone :")
print("Enter Customer's email address: ")
email = input("email :")

#price of a used car
price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = float(0.1 * price)
else:
    down_payment =float( 0.2 * price)

print(f"Down Payment: {down_payment}")
print()
print("Full Names:", fullnames)
print("Phone: " ,phone)
print("Email: " , email)
print("Down Payment: " ,down_payment)
