#!/usr/bin/env python
# coding: utf-8

# In[ ]:


p=int(input("Enter your 4 digit pin number: "))
x = 10000
while True:
    if(p == 1234):
        print("1-Balance")
        print("2-withdrawl")
        print("3-amout add")
        print("4-return or restart")
        c = int(input("Please choose options: "))
        if (c == 1):
            print("balance is ",x)
        elif(c==2):
            a=int(input("Enter withdraw amount: "))
            x=float(x-a)
            print("amount after withdrawl is: ",x)
        elif(c==3):
            a=int(input("Enter add amount: "))
            x=float(x+a)
            print("amount after adding is: ",x)
        elif(c==4):
            a=input("card restart? yes or no: ").lower()
            if a=="no":
                print("thank you")
                break
            if a=="yes":
                print("1-Balance")
                print("2-withdrawl")
                print("3-amout add")
                c = int(input("Please choose options: "))
                if (c == 1):
                    print("balance is 10000")
                elif(c==2):
                    a=int(input("Enter withdraw amount: "))
                    x=float(x-a)
                    print("amount after withdrawl is: ",x)
                elif(c==3):
                    a=int(input("Enter add amount: "))
                    x=float(x+a)
                    print("amount after adding is: ",x)
                    break           
    else:
        print("Wrong pin")
        break

