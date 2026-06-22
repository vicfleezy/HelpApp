#setting user input
hours = int(input("KW hours used "))

#if & else statements
if hours <= 1000 :
   amount = .07633*hours
else:
   amount = (.09259*(hours-1000)) + (.07633*1000)
#print the result
print("Amount owed is $", amount)