from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, password)

    # Copy password automatically
    pyperclip.copy(password)


# ------------------------------- SEARCH ----------------------------------- #
def search():
    try:
        with open("saved_passwords.json") as data_file:
            data = json.load(data_file)
        if website_input.get() in data.keys():
            website_data = website_input.get()
            eusername_data = data[website_data]["email"]
            password_data = data[website_data]["password"]
            messagebox.showinfo(title=website_data, message=f"Email: {eusername_data}\n"
                                                                         f"Password: {password_data}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There are currently no accounts to search for."
                                                   "Please create an account first.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_account():
    new_data = {website_input.get(): {
                    "email": eusername_input.get(),
                    "password": password_input.get()
                }
                }

    if not website_input.get() or not password_input.get():
        messagebox.showinfo(title="Warning: Missing fields", message="Fields must have information in it.")
    # Confirmation of information
    else:
        try:
            with open("saved_passwords.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            print("Currently no file found. Creating a new file.")
            with open("saved_passwords.json", "w") as new_data_file:
                json.dump(new_data, new_data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("saved_passwords.json", "w") as new_data_file:
                json.dump(data, new_data_file, indent=4)
        finally:
            # Reset all information in the fields
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create and show lock Logo
canvas = Canvas(width=170, height=170)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(85, 85, image=lock_logo)
canvas.grid(column=1, row=0)

# Create website entry row
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_input = Entry(width=27)
website_input.focus()
website_input.grid(sticky=W, column=1, row=1)

search_account_button = Button(text="Search", command=search, width=14)
search_account_button.grid(sticky=E, column=1, row=1, columnspan=2)

# Create email and username entry row
eusername_label = Label(text="Email/Username: ")
eusername_label.grid(column=0, row=2)
eusername_input = Entry(width=45)
eusername_input.insert(END, "creighton@email.com")
eusername_input.grid(sticky=W, column=1, row=2, columnspan=2)

# Create password entry row
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_input = Entry(width=27)
password_input.grid(sticky=W, column=1, row=3)

# Generate password button
generate_password_button = Button(text="Generate Password", command=generate_password, width=14)
generate_password_button.grid(sticky=E, column=1, row=3, columnspan=2)

# Add button of account creation
add_button = Button(text="Add", command=save_account, width=38)
add_button.grid(sticky=W, column=1, row=4, columnspan=2)

window.mainloop()
