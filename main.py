from tkinter import *
import pandas
from tkinter import messagebox
import pyperclip
import random
#-----------------------COLORS--------------------------#
BACKGROUND_COLOR = "#ADC4CE"
BUTTON_COLOR = "#EEE0C9"
#-----------------------LOGIN -----------------------#
LOGIN_USERNAME = "NULL"
LOGIN_PASSWORD = "NULL"
def login():

    if LOGIN_PASSWORD == login_pass_entry.get() and LOGIN_USERNAME == login_user_entry.get():
        window.deiconify()
        top.destroy()
    else:
        messagebox.showerror(title="Error",message="Try agian")
#-----------------------SEARCH -----------------------#
def search():
    web = web_entry.get()
    email = email_entry.get()
    file = pandas.read_csv("data.csv")
    file_data_frame = pandas.DataFrame(file)
    web_list = file.website.to_list()
    email_list = file.email.to_list()


    for (index,row) in file_data_frame.iterrows():
        if row.website == web and row.email == email:
            password_entry.insert(0,row.password)
            pyperclip.copy(text=row.password)
    if web not in web_list:
        messagebox.showerror(title="Error", message="Not Found, Invalid website")
        web_entry.delete(0,END)
        email_entry.delete(0,END)
    elif email not in email_list:
        messagebox.showerror(title="Error", message="Not Found, Invalid email/username")
        email_entry.delete(0,END)
#-----------------------SAVE PASSWORD -----------------------#
def save():
    error = False
    file = pandas.read_csv("data.csv")
    file_data_frame = pandas.DataFrame(file)
    
    for (index, row) in file_data_frame.iterrows():
        if row.website == web_entry.get()and row.email == email_entry.get():
            error = True
            n = index

    if web_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror(title="Error", message="invalid input")
    elif error == True:
        change = messagebox.askyesno(title="Error",message="Account already exists. yes to change.")
        if change:
            file_data_frame.loc[n, "password"] = password_entry.get()
            file_data_frame.to_csv("data.csv", index=False)
        web_entry.delete(0,END)
        password_entry.delete(0,END)
        email_entry.delete(0,END)
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(),message=f'''These are the details entered\nEmail: {email_entry.get()}\n Password: {password_entry.get()}\n
    Is it okay to save?''')
    if is_ok:
        data ={
            "website": [web_entry.get()],
            "email": [email_entry.get()],
            "password" : [password_entry.get()],
        }
        df = pandas.DataFrame(data=data)
        with open("data.csv", mode="a") as f:
            df.to_csv(f, header=False,index=False)

    web_entry.delete(0,END)
    password_entry.delete(0,END)
#-----------------------PASSWORD GENERATOR-----------------------#
def password_generator():
    

    password_entry.delete(0,END)
    #Create lists contain numbers, letters and symbols
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 
            'P', 'Q', 'R''S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c','e', 'f', 'g', 'h',
            'j', 'k', 'l', 'm', 'n','p','q','r','s','t','u','v','w','x','y','z']

    numbers = ['1','2','3','4','5','6','7','8','9','0']

    symbols = ['!', '@','#', '$','%','^','&','*']
    #Choose how many of each should be in the password randomly
    number_of_letters = random.randint(5,8)
    number_of_numbers = random.randint(1,3)
    number_of_symbols = random.randint(1,3)
    length_of_password = number_of_letters + number_of_symbols + number_of_numbers

    #Create strong password randomly
    generated_password = []

    #Add random letter with random index
    for i in range(0, number_of_letters):
        j = random.choice(letters)
        k = random.randrange(0, length_of_password-1)
        generated_password.insert(k, j)

    #Add random number with random index
    for i in range(0, number_of_numbers):
        j = random.choice(numbers)
        k = random.randrange(0, length_of_password-1)
        generated_password.insert(k, j)

    #Add random symbol with random index
    for i in range(0, number_of_symbols):
        j = random.choice(symbols)
        k = random.randrange(0, length_of_password-1)
        generated_password.insert(k, j)
    
    #Convert password to a str
    result = ''.join(generated_password)
    #Put password in passward entry
    password_entry.insert(0,result)
    #Copy password automatically
    pyperclip.copy(text=result)
#-----------------------ERASE FUNCTION-----------------------#
def erase():
    #Delete all the entries
    web_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)

#-----------------------UI DESIGN-----------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)


#Login screen
top = Toplevel()
top.config(bg=BACKGROUND_COLOR,padx=20,pady=20)
top.geometry("350x200")

login_label = Label(top,text="PLEASE LOGIN",font="Arial",bg=BACKGROUND_COLOR)
login_label.grid(row=0,column=1)

login_user_label = Label(top,text="Username:",bg=BACKGROUND_COLOR,pady=10)
login_user_label.grid(row=1,column=0)
login_user_entry = Entry(top,show="*")
login_user_entry.grid(row=1,column=1,columnspan=2)

login_pass_label = Label(top,text="Password:",bg=BACKGROUND_COLOR,pady=10)
login_pass_label.grid(row=2,column=0)
login_pass_entry = Entry(top,show="*")
login_pass_entry.grid(row=2,column=1,columnspan=2)

cancel_btn = Button(top,text="Cancel",bg=BACKGROUND_COLOR,highlightthickness=0,command=cancel)
cancel_btn.grid(row=3,column=1,sticky="we")

login_btn = Button(top,text="Login",bg=BACKGROUND_COLOR,highlightthickness=0,command=login)
login_btn.grid(row=3,column=2,sticky="we")

canavs = Canvas(width=200,height=200,highlightthickness=0,bg=BACKGROUND_COLOR)
photo = PhotoImage(file="logo.png")
canavs.create_image(100,100,image=photo)


canavs.grid(row=0,column=1)

#Web
web_label = Label(text="Website:",padx=20,pady=20,bg=BACKGROUND_COLOR)
web_label.grid(row=1,column=0)
web_entry = Entry(width=19)
web_entry.grid(row=1,column=1)
search_btn = Button(text="Search", bg=BUTTON_COLOR,highlightthickness=0,bd=1,width=16,command=search)
search_btn.grid(row=1,column=2)

#Username
email_label = Label(text="Email/Username:", padx=20,pady=20,bg=BACKGROUND_COLOR)
email_label.grid(row=2, column=0)
email_entry = Entry(width=36)
email_entry.grid(row=2,column=1,columnspan=2)

#Password
password_label = Label(text="Password", padx=20,pady=20,bg=BACKGROUND_COLOR)
password_label.grid(row=3,column=0)
password_entry = Entry(width=19)
password_entry.grid(row=3,column=1)

#Generate strong password randomly
password_btn = Button(text="Generate Password",bg=BUTTON_COLOR,bd=1,command=password_generator)
password_btn.grid(row=3,column=2)

#Save info in the data file
add_btn =Button(text="Add", bg=BUTTON_COLOR, width=16,bd=1)
add_btn.grid(row=4,column=1,sticky="we")

#Erase all fields
erase_btn = Button(text="Erase", bg=BUTTON_COLOR,width=15,bd=1,command=erase)
erase_btn.grid(row=4,column=2)

window.withdraw()
window.mainloop()