from tkinter import *
#-----------------------UI design-----------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canavs = Canvas(width=200,height=200,highlightthickness=0,)
photo = PhotoImage(file="logo.png")
canavs.create_image(100,100,image=photo)
canavs.grid(row=0,column=1)




window.mainloop()