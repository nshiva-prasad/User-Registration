import sqlite3 as sq
import tkinter as tk
import random
import smtplib

# Making sqlite database used for storing the Uername and Password

db = sq.connect("email_login.db")
cursor = db.cursor()
cmd1 = ('''CREATE TABLE IF NOT EXISTS COMPANY
(NAME TEXT,PASSWORD TEXT,EMAIL TEXT)
''')

cursor.execute(cmd1)

#Creating a login function

def login(self):

    username_input = usernameEntry.get()
    password_input = passwordEntry.get()

    if len(username_input) == 0 and len(password_input) == 0:
        Output.config(text = "Please enter the username and password")

    elif len(username_input) == 0 and len(password_input) != 0 :
        Output.config(text = "Please Enter a Username")

    elif len(username_input) != 0 and len(password_input) == 0:
        Output.config(text = "Please enter a Password")

    elif len(username_input) != 0 and len(password_input) != 0:

        #code for authentication of password with username

        sql_data = cursor.execute('''SELECT NAME FROM COMPANY WHERE NAME = (?)''', (username_input,))
        sql_data = cursor.fetchone()
        if sql_data is None :       
            Output.config(text = "username does not exist, please register")
        elif sql_data[0] == username_input:
            sql_data = cursor.execute('''SELECT PASSWORD FROM COMPANY WHERE NAME = (?)''', (username_input,))
            sql_data = cursor.fetchone()
            if sql_data is None :
                Output.config(text = "Password cannot be empty")
            elif sql_data[0] != password_input:
                Output.config(text = "Incorrect Password")
            elif sql_data[0] == password_input:
                Output.config(text = "Login successful")
        else:
            pass
    else:
        pass

#creating the OTP generation

def otp(self):

    otp.username_input = usernameEntry.get()
    otp.password_input = passwordEntry.get()
    otp.email_input    = Email_Entry.get()


    if len(otp.username_input) != 0 and len(otp.password_input) != 0 and len(otp.email_input) != 0 :
        # checking for duplicate username
        sql_data = cursor.execute('''SELECT NAME FROM COMPANY WHERE NAME = (?)''', (otp.username_input,))
        sql_data = cursor.fetchone()
        if sql_data is None :
            otp.random_otp = random.randint(100000,999999)

            FROM = "email address" #put email address from which otp should be sent
            pwd = "password" #put your mail password here
            TO = otp.email_input
            SUBJECT = "OTP mail"
            TEXT = f"here is the otp for completing  the registartion: {otp.random_otp}"

            message = "Subject: %s \n\n%s" % (SUBJECT, TEXT)
            print(message)

            server = smtplib.SMTP("smtp.gmail.com",587)
            server.ehlo()
            server.starttls()
            server.login(FROM,pwd)
            server.sendmail(FROM,TO,message)
            server.close()
            Output.config(text = "email sent successfully")
            print("email sent successfully")
        elif sql_data[0] == otp.username_input:
            Output.config(text = "Username alredy exists, please login")
        else:
            pass
    else:
        if len(otp.username_input) == 0 and len(otp.password_input) == 0 and len(otp.email_input) == 0 :
            Output.config(text = "Please fill in the email, username and password")
        elif len(otp.username_input) == 0 and len(otp.password_input) == 0 and len(otp.email_input) != 0 :
            Output.config(text = "Please Enter  Username and Password")
        elif len(otp.username_input) == 0 and len(otp.password_input) != 0 and len(otp.email_input) == 0 :
            Output.config(text = "Please Enter  Username and Email")
        elif len(otp.username_input) == 0 and len(otp.password_input) != 0 and len(otp.email_input) != 0 :
            Output.config(text = "Please Enter  Username")   
        elif len(otp.username_input) != 0 : 

            # checking for duplicate username in the datebase

            sql_data = cursor.execute('''SELECT NAME FROM COMPANY WHERE NAME = (?)''', (otp.username_input,))
            sql_data = cursor.fetchone()
            if sql_data is None:
                if len(otp.password_input) == 0 and len(otp.email_input) == 0 :
                    Output.config(text = "Please Enter Email and Password")
                elif len(otp.password_input) != 0 and len(otp.email_input) == 0 :
                    Output.config(text = "Please Enter Email")
                elif len(otp.password_input) == 0 and len(otp.email_input) != 0 :
                    Output.config(text = "Please Enter Password")
                else:
                    pass
            elif sql_data[0] == otp.username_input:
                    Output.config(text = "Username alredy exists, please login with password")
            else:
                pass
        else:
            pass

# Making the registration function

def register(self):

    OTP_input = OTP_passEntry.get()

    print(OTP_input)

    print(otp.random_otp)

    if str(otp.random_otp) == str(OTP_input) :
        cursor.execute(f'''INSERT INTO COMPANY (NAME,PASSWORD,email) VALUES("{otp.username_input}","{otp.password_input}","{otp.email_input}")''')
        db.commit()
        print(otp.username_input)
        print(otp.password_input)
        print(otp.email_input)
        Output.config(text = "registration successful")
    else:
        Output.config(text = "invalid otp, try again")
                
    
root = tk.Tk() # Defining the main app
root.title("Login or Register")
root.geometry("800x400+50+50")


frame1 = tk.Frame(root) #Creating a Frame for root app

userameLabel=tk.Label(text="Username:",font=("arial",15,"bold")).place(x=350,y=50,height=20,width=200)  #Username label creation
usernameEntry=tk.Entry() # taking username
usernameEntry.config(font=("arial",15,"bold"))
usernameEntry.place(x=500,y=50,height=25,width=200)

passwordLabel=tk.Label(text="Password:",font=("arial",15,"bold")).place(x=350,y=90,height=20,width=200) #Password label creation
passwordEntry=tk.Entry(show="*") #taking password by hiding the credentials
passwordEntry.config(font=("arial",15,"bold"))
passwordEntry.place(x=500,y=90,height=25,width=200)


Email_Label=tk.Label(text="Enter Email:",font=("arial",15,"bold")).place(x=10,y=60,height=20,width=200) #OTP_password label
Email_Entry=tk.Entry() #Taking Email
Email_Entry.config(font=("arial",15,"bold"))
Email_Entry.place(x=50,y=90,height=25,width=250)


OTP_passLabel=tk.Label(text="Enter OTP:",font=("arial",15,"bold")).place(x=5,y=220,height=20,width=200) #OTP_password label
OTP_passEntry=tk.Entry() #Taking OTP
OTP_passEntry.config(font=("arial",15,"bold"))
OTP_passEntry.place(x=50,y=250,height=25,width=200)


b1 = tk.Button(text ="LOGIN") #Creating login button
b1.config(bg="yellow", fg="blue",font=("arial",15,"bold"))
b1.bind("<Button-1>",login)
b1.place(x=550,y=120,height=30,width=75)


b2 = tk.Button(text ="Get OTP") #Creating OTP generate button
b2.config(bg="yellow", fg="blue",font=("arial",15,"bold"))
b2.bind("<Button-1>",otp)
b2.place(x=75,y=120,height=25,width=120)


b3 = tk.Button(text ="REGISTER") #Creating register button
b3.config(bg="yellow", fg="blue",font=("arial",15,"bold"))
b3.bind("<Button-1>",register)
b3.place(x=75,y=280,height=25,width=120)


OutputLabel=tk.Label(text="Output:",font=("arial",15,"bold")).place(x=290,y=220,height=20,width=200) #Creating output label
Output = tk.Label(frame1,text = "     ") #displaying the output
Output.config(bg="white",fg="black",font=("arial",10,"bold"))
Output.place(x=350,y=250,height=100,width=400)

frame1.place(x=0,y=0,height=800,width=1000)
root.mainloop()
db.close()
