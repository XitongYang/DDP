def add(num1,num2):
   return num1 + num2 

def subtract(num1,num2):
   return num1 - num2 

def multipy(num1,num2):
   return num1 * num2 

def divide(num1,num2):
   return num1 / num2 

def calculator():
   while True:
        print("Select operation:")
        print("1.add")
        print("2.subtract")
        print("3.multipy")
        print("4.divide")
        print("5.exit")

        choice = input("enter choice(1/2/3/4)")
        if choice in ["1","2","3","4"]:
    
            num1=float(input("enter first number"))
            num2=float(input("enter second number"))

        if choice == "1":
            print("result:",add(num1, num2))
        elif choice == "2":
            print("result:",subtract(num1, num2))
        elif choice == "3":
            print("result:",multipy(num1, num2))
        elif choice == "4":
            print("result:",divide(num1, num2))
        elif choice=="5":
            exit()
        
        else:
             print("invalid input,try again")
       
        

calculator()         



        



