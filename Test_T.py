import tkinter as tk
from main import *


root = tk.Tk()
root.title("Perico's Banking System")

title_label = tk.Label(root, text="Login")
username_Label = tk.Label(root, text="Username")
username_entry = tk.Entry(root)
password_Label = tk.Label(root, text="Password")
password_entry = tk.Entry(root, show="*")
login_button = tk.Button(root, text="Login")

title_label.grid(row=0,column=0, columnspan=2)
username_Label.grid(row=1,column=0)
username_entry.grid(row=1,column=1)
password_Label.grid(row=2,column=0)
password_entry.grid(row=2,column=1)
login_button.grid(row=3,column=0, columnspan=2)

root.mainloop()