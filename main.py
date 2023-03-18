print("*****BANK TRANSACTION*****")
import mysql.connector
import datetime
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
mycursor.execute("create table if not exists banktrans(acno char(4),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()
while(True):
    
    print("1--> Create account")
    print("2--> Deposit money")
    print("3--> Withdraw money")
    print("4--> Display particular account")
    print("5--> Display all accounts")
    print("6--> Display All Transaction")
    print("7--> Display Transaction of Particular Account")
    print("8--> Delete account")
    print("9--> Exit")
    ch=int(input("Enter your choice:"))


    
    if(ch==1):
        try: 
            print("All information prompted are mandatory to be filled")
            acno=str(input("Enter account number:"))
            name=input("Enter name(limit 35 characters):")
            city=str(input("Enter city name:"))
            mn=str(input("Enter mobile no.:"))
            balance=float(input("Enter initial balance:"))
            mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
            mydb.commit()
            print("Account is successfully created!!!")
        
        except: 
            print(""" 
                  Error in creating account...
                  """)




    elif(ch==2):
        try: 
            
            acno=str(input("Enter account number:"))
            dp=int(input("Enter amount to be deposited:"))
            now=datetime.datetime.now()
            print("Current Date and Time :",end=" ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print()
            dot=str(input("Enter date of Transaction: YYYY-MM-DD "))
            ttype="d"
            mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
            mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
            mydb.commit()
            print("Money has been deposited successully!!!")
        
        except: 
            print(""" 
                  Error in depositing money...
                  """)
            


    elif(ch==3):
        
        try: 
            acno=str(input("Enter account number:"))
            wd=int(input("Enter amount to be withdrawn:"))
            now=datetime.datetime.now()
            print("Current Date and Time :",end=" ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print()
            dot=str(input("Enter date of Transaction: YYYY-MM-DD "))
            ttype="w"
            mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
            mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
            mydb.commit()
            print("Money has been withdrawn successully!!!")
        except: 
            print(""" 
                  Error in withdrawl money...
                  """)
            
            
            
    elif(ch==4):
        
        try:
            acno=str(input("Enter account number:"))
            mycursor.execute("select * from bank_master where acno='"+acno+"'")
            for i in mycursor:
                print(i)
            
        except: 
            print(""" 
                  Error in displaying account information...
                  """) 
            
            
    elif(ch==5):
        
        try: 
            mycursor.execute("select * from bank_master")
            rec=mycursor.fetchall()
            print(tabulate(rec,headers=["acno","name","city","mobileno","balance"],tablefmt="fancy_grid"))
        except:
            print("Error in Displaying record")
            
            
            
    elif(ch==6):
        
        try:
            mycursor.execute("select * from banktrans")
            rec=mycursor.fetchall()
            print(tabulate(rec,headers=["acno","amount","dot","ttype"],tablefmt="fancy_grid"))
            
        except:
             print(""" 
                  Error in displaying transactions...
                  """)
             
             
             
    elif(ch==7):
        
        try:
            acno=str(input("Enter account number:"))
            mycursor.execute("select * from banktrans where acno='"+acno+"'")
            for i in mycursor:
                print(i)
            
        except:
             print(""" 
                  Error in displaying transactions...
                  """) 
        
    
    
    elif(ch==8):
        try:
            acno=str(input("Enter account number:"))
            mycursor.execute("delete from bank_master where acno=' "+acno+" '")
            mycursor.execute("delete from banktrans where acno=' "+acno+" '")
            mydb.commit()
            print("Account has been deleted successully!!!")
        except: 
            print(""" 
                  Error in deleting account...
                  """)
    elif(ch==9):
        print("Thank You For Visiting. Visit Again")
        break
        
    else:
        print("""
              Enter Valid Choice...
              """)
        
        
