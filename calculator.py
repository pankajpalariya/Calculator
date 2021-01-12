i = 'Y'
while i.upper()=='Y':
   calculator = input("enter the calculation\n")
   print(str(eval(calculator)))
   print("if you want to calculate more Press y")
   i = input().strip()
