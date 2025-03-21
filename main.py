import tkinter as tk
import re


def get_input():
    user_text = entry.get()
    number_list = re.findall(r'\d+', user_text)
    return number_list


def print_result(text):
    label_output.config(state="normal")
    label_output.delete()
    label_output.insert(tk.END, text)
    label_output.see(tk.END)


def add_list_button():
    print_result(get_input())


def filter_odd(number_list):
    filtered_number_list = []
    for i in number_list:
        if int(i) % 2 != 0:
            filtered_number_list.append(i)
    return filtered_number_list


def filter_odd_button():
    print_result(filter_odd(get_input()))


root = tk.Tk()
root.title("Tkinter thingy ")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=100)
entry.grid(row=0, column=0, padx=5)

button = tk.Button(frame, text="Add list", command=add_list_button)
button.grid(row=0, column=1, padx=5)

button = tk.Button(frame, text="Filter odd", command=filter_odd_button)
button.grid(row=1, column=1, padx=5)

label_output = tk.Text(root)
label_output.pack(pady=10)

root.mainloop()
