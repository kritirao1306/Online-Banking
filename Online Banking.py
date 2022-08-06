import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root', password='', database='bank_management' )
def OpenAcc():
    n=input("Enter the name:")
    ac=input("Enter the Account No:")
    db=input("Enter the Date of Birth: ")
    add=input("Enter your Address: ")
    cn=input("Enter the Contact Number: ")
    ob=int(input("Enter the opening Balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into Amount values(%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Account Credited Sucessfully.") 
    main()

def DepoAmo():
    amount=input("Entered The amount you want to deposit: ")
    ac=input("Enter the Account No:")
    a='select balance from Amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=int(result[0])+int(amount)
    sql=('update Amount set balance=%s where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    print("Amount Sucessfully Deposited.")
    main()

class minBalance(Exception):
    pass

def WithdrawAmount():
    amount=input("Entered The amount you want to Withdraw: ")
    ac=input("Enter the Account No:")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=int(result[0])-int(amount)
    try:
        if t<=5000:
            raise minBalance
        else:
          sql=('update amount set balance=%s where AccNo=%s')
        d=(t,ac)
        x.execute(sql, d)
        mydb.commit()
        print('Deducated in Amount')
    except minBalance:
        print('Sorry,The Minimum balance to be maintained is 5000')
    main()

def BalEnq():
    ac=input("Enter the account no: ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance for Account:",ac,"is",result[-1])
    main()

def DisDetails():
    ac=input("Enter the account no: ")
    a='select * from account where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()  

def CloseAcc():
    ac=input("Enter the account no: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()        



def main():
    print('''WELCOME TO THE BANK
            1.OPEN ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW  AMOUNT
            4.BALANCE ENQUIRY
            5.DISPLAY CUSTOMER DETAILS
            6.CLOSE AN ACCOUNT  ''' )
    choice = input("Enter The Task you want to Perform: ")
    if  (choice=='1'):
        OpenAcc()   
    elif (choice=='2'):
        DepoAmo() 
    elif (choice=='3'):
        WithdrawAmount()
    elif (choice=='4'):
        BalEnq()
    elif (choice=='5'):
        DisDetails()
    elif (choice=='6'):
        CloseAcc()
    else:
         print("Invaid Choice")
         main()
main()