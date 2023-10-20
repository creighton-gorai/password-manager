from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_account():
    if not website_input.get() or not password_input.get():
        messagebox.showinfo(title="Warning: Missing fields", message="Fields must have information in it.")
    # Confirmation of information
    elif messagebox.askokcancel(title=website_input.get(), message=f"There are the details entered:"
                                                                   f"\nEmail: {eusername_input.get()}"
                                                                   f"\nPassword: {password_input.get()}"
                                                                   f"\nIs it okay to save?"):
        # Save information into a pipe delimited file
        save_user_info = open("saved_passwords.txt", "a")
        save_user_info.write(website_input.get() + " | " + eusername_input.get() + " | " + password_input.get() + "\n")
        save_user_info.close()

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
website_input = Entry(width=45)
website_input.focus()
website_input.grid(sticky=W, column=1, row=1, columnspan=2)

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
