import tkinter as tk
import re
from sympy import isprime
from multiprocessing import Process, Queue


def get_input():
    user_text = entry.get()
    number_list = re.findall(r'\d+', user_text)
    return number_list


def print_result(text):
    label_output.config(state="normal")
    label_output.delete("1.0", tk.END)
    label_output.insert(tk.END, text)
    label_output.see(tk.END)


def add_list_button():
    print_result(get_input())


def filter_odd(number_list, queue):
    filtered_number_list = [i for i in number_list if int(i) % 2 != 0]
    queue.put(filtered_number_list)


def filter_odd_button():
    queue = Queue()
    process = Process(target=filter_odd, args=(get_input(), queue))
    process.start()
    process.join()
    result = queue.get()
    print_result(result)


def filter_prime(number_list, queue):
    filtered_number_list = [i for i in number_list if isprime(int(i))]
    queue.put(filtered_number_list)


def filter_prime_button():
    queue = Queue()
    process = Process(target=filter_prime, args=(get_input(), queue))
    process.start()
    process.join()
    result = queue.get()
    print_result(result)


def sum_list(number_list, queue):
    total = sum(int(i) for i in number_list)
    queue.put(total)


def sum_button():
    queue = Queue()
    process = Process(target=sum_list, args=(get_input(), queue))
    process.start()
    process.join()
    result = queue.get()
    print_result(result)


if __name__ == '__main__':
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

    button = tk.Button(frame, text="Filter prime", command=filter_prime_button)
    button.grid(row=2, column=1, padx=5)

    button = tk.Button(frame, text="Sum list", command=sum_button)
    button.grid(row=3, column=1, padx=5)

    label_output = tk.Text(root)
    label_output.pack(pady=10)

    root.mainloop()
