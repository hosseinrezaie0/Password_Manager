from tkinter import *
import pandas
#-----------------------COLORS--------------------------#
BACKGROUND_COLOR = "#ADC4CE"
BUTTON_COLOR = "#EEE0C9"
#-----------------------SEARCH FUNCTION-----------------------#
def search():
    web = web_entry.get()
    email = email_entry.get()
    file = pandas.read_csv("data.csv")
    file_data_frame = pandas.DataFrame(file)

    for (index,row) in file_data_frame.iterrows():
        if row.website == web and row.email == email:
            password_entry.insert(0,row.password)
        

#-----------------------UI DESIGN-----------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

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

password_btn = Button(text="Generate Password",bg=BUTTON_COLOR,bd=1)
password_btn.grid(row=3,column=2)

add_btn =Button(text="Add", bg=BUTTON_COLOR, width=16,bd=1)
add_btn.grid(row=4,column=1,sticky="we")

erase_btn = Button(text="Erase", bg=BUTTON_COLOR,width=15,bd=1)
erase_btn.grid(row=4,column=2)


window.mainloop()