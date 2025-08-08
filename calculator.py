def calc():
 op = input("Choose option --> \n Addition[1] \n Subtraction[2] \n Multiplication[3] \n Divison[4] \n Enter you option :")
 num1 = float(input("Enter you first number :"))
 num2 = float(input("Enter you second number :"))
 if op == '1':
    print("The sum is ",num1 + num2)
 elif op == '2':
    print("The sum is ",num1 - num2)
 elif op == '3':
    print("The sum is ",num1 * num2)
 elif op == '4':
    print("The sum is ",num1 / num2)
 else:
    print("can't find the option")
 
calc()

reuse = input("Do you want to reuse the calculator [yes,no] :")

if calc(reuse) == 'yes':
   calc()
elif calc(reuse) == 'no':
   print("Thanks for usong the calculator")


