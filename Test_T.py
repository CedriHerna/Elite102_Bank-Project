import tkinter as tk
import main
 


def button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Sample Title")


button = tk.Button(root, text=" Click Me!", command=button_click)
button.pack(pady=10)
root.mainloop()