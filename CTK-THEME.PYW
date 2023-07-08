# Made By k.2oop
# Discord : ux11
# Discord Server : https://discord.gg/KfjE3jhhQw

import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("System")

app = customtkinter.CTk()
app.geometry("400x300")
app.title("k.2oop")

def theme(choice):
    if choice == "Dark":
        customtkinter.set_appearance_mode("Dark")
    elif choice == "Light":
        customtkinter.set_appearance_mode("Light")


themedropdwn = customtkinter.CTkComboBox(master=app,
                                     values=["Dark", "Light"],
                                     command=theme)
themedropdwn.pack()
themedropdwn.set("Theme")

app.resizable(False, False)
app.mainloop()
