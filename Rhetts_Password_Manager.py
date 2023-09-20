from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import string
import os
from tkinter import simpledialog
from PIL import Image, ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    if not os.path.exists("data.json"):
        print("Error: File 'data.json' was not created.")

# ---------------------------- CHANGE PASSWORD ------------------------------- #
def change_password():
    website = website_entry.get().lower()
    current_password = password_entry.get()

    if len(website) == 0 or len(current_password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill in the Password field to change the password.")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                new_password = simpledialog.askstring("Change Password", f"Enter a new password for {website} or leave blank to generate one:")

                if new_password is not None:
                    if len(new_password) == 0:
                        # Generate a new password
                        new_password = generate_password()

                    confirm = messagebox.askyesno("Confirm Password Change", f"Are you sure you want to change the password for {website}?")

                    if confirm:
                        data[website]["password"] = new_password
                        with open("data.json", "w") as updated_data_file:
                            json.dump(data, updated_data_file, indent=4)
                            messagebox.showinfo("Success", f"Password for {website} updated successfully!")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            message = f"Email: {email}\nPassword: {password}\n\nDo you want to copy the password to the clipboard?"
            user_response = messagebox.askyesno(title=website, message=message)

            if user_response:
                pyperclip.copy(password)  # Copy the password to the clipboard

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
def on_entry_change(event):
    # Enable the "Change Password" button when user enters data into website and email fields
    if len(website_var.get()) > 0 and len(email_var.get()) > 0:
        change_password_button["state"] = "normal"
    else:
        change_password_button["state"] = "disabled"

window = Tk()
window.title("Rhett's Password Manager")
window.config(padx=50, pady=50)
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, 'RPM.ico')
window.iconbitmap(icon_path)

canvas = Canvas(width=500, height=500)
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, 'logo.png')
logo_img = Image.open(logo_path)
logo_img = ImageTk.PhotoImage(logo_img)
canvas.create_image(250, 250, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_var = StringVar()
website_entry = Entry(width=35, textvariable=website_var)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_var = StringVar()
email_entry = Entry(width=35, textvariable=email_var)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, " ")
email_entry.focus()

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_entry.bind("<KeyRelease>", on_entry_change)  # Bind to entry change event

generate_password_button = Button(text="Generate Password", command=lambda: password_entry.insert(0, generate_password()))
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Creating a button
change_password_button = Button(text="Change Password", width=36, command=change_password)
change_password_button.grid(column=1, row=5, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

# Keeping the window open
window.mainloop()
