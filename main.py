from tkinter import *
#-----------------------UI design-----------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canavs = Canvas(width=200,height=200,highlightthickness=0,)
photo = PhotoImage(file="logo.png")
canavs.create_image(100,100,image=photo)
canavs.grid(row=0,column=1)

#Web
web_label = Label(text="Website:",padx=20,pady=20)
web_label.grid(row=1,column=0)
web_entry = Entry(width=35,)
web_entry.grid(row=1,column=1, columnspan=2)

#Username
email_label = Label(text="Email/Username:", padx=20,pady=20)
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)

#Password
password_label = Label(text="Password", padx=20,pady=20)
password_label.grid(row=3,column=0)
password_entry = Entry(width=18)
password_entry.grid(row=3,column=1)

password_btn = Button(text="Generate Password",bg="white",bd=1)
password_btn.grid(row=3,column=2)

add_btn =Button(text="Add", bg="white", width=36,bd=1)
add_btn.grid(row=4,column=1,columnspan=2)


window.mainloop()