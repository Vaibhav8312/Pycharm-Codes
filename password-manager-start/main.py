from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import string

WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    if len(password_entry.get()) == 0:
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    pyperclip.copy(password)

    # Alternate Password Generator

    # alphabet = string.ascii_letters + string.digits + string.punctuation
    # password = ''.join(choice(alphabet) for i in range(16))
    # password_entry.insert(0, password)
    # pyperclip.copy(password)

    # 1. Alternate Clipboard Solution

    # window.clipboard_clear()
    # window.clipboard_append(password)

    # 2. Alternate Clipboard Solution

    # password_entry.clipboard_clear()
    # password_entry.clipboard_append(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                                                              f"\nPassword: {password} \n Is it ok to save.")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                # print(f"{website} | {email} | {password}", file=data_file) This is just the another way to say .write
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg=WHITE, highlightthickness=0)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=WHITE, highlightthickness=0)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=WHITE, highlightthickness=0)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35, bg=WHITE, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35, bg=WHITE, highlightthickness=0)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "vaibhav@gmail.com")

password_entry = Entry(width=21, bg=WHITE, highlightthickness=0)
password_entry.grid(column=1, row=3, sticky="EW")


# Buttons
generate_password_button = Button(text="Generate Password", bg=WHITE, highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, bg=WHITE, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()