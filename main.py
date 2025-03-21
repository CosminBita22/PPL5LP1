import tkinter as tk
import re


def get_input():
    user_text = entry.get()
    number_list = re.findall(r'\d+', user_text)
    label_output.config(text=f"Result: {number_list}")
    return number_list


root = tk.Tk()
root.title("Tkinter thingy ")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=25)
entry.grid(row=0, column=0, padx=5)

button = tk.Button(frame, text="Add list", command=get_input)
button.grid(row=0, column=1, padx=5)

label_output = tk.Label(root, text="")
label_output.pack(pady=10)

root.mainloop()
