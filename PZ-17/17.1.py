import tkinter as tk
from tkinter import ttk

def send_form():
    name = name_entry.get()
    email = email_entry.get()
    message = message_entry.get("1.0", "end-1c")
    inquiry = inquiry_var.get()

    if name and email and message and inquiry:
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)
        print("Inquiry:", inquiry)
    else:
        status_label.config(text="Please fill all entries.", fg="red")

root = tk.Tk()
root.title("Contact Form")
root.geometry("400x300")

form_title_label = tk.Label(root, text="Contact Form", font=("Helvetica", 16, "bold"))
form_title_label.grid(row=0, column=0, columnspan=2, sticky="w")

separator = ttk.Separator(root, orient="horizontal")
separator.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=3, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=3, column=1, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=4, column=0, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, pady=5)

message_label = tk.Label(root, text="Message:")
message_label.grid(row=5, column=0, sticky="w")
message_entry = tk.Text(root, height=5, width=30)
message_entry.grid(row=5, column=1, pady=5)

inquiry_label = tk.Label(root, text="Subject:")
inquiry_label.grid(row=6, column=0, sticky="w")
inquiry_var = tk.StringVar()
inquiry_dropdown = ttk.Combobox(root, textvariable=inquiry_var, values=["Product Inquiry", "Product Inquiry2", "Product Inquiry3"])
inquiry_dropdown.grid(row=6, column=1, pady=5)

send_button = tk.Button(root, text="Send", command=send_form, bg="gray", fg="white")
send_button.grid(row=7, column=0, columnspan=2, pady=5)

status_label = tk.Label(root, text="Please fill all entries.")
status_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

root.mainloop()
