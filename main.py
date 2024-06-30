from tkinter import *
from tkinter import messagebox
from pass_gen import pass_generator
import pyperclip
import json


# -----------------------------SEARCH PASSWORDS-----------------------------#
def search_pass():
    website = website_input.get()

    if len(website.strip()) == 0:
        messagebox.showwarning(title="Error", message="Please enter a website name.")
    else:
        try:
            with open("password.json", "r"):
                pass

        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="You have no passwords saved.")

        else:
            with open("password.json", "r") as json_file:
                data_dict = json.load(json_file)
                if website in data_dict:
                    email = data_dict[website]["Email"]
                    password = data_dict[website]["Password"]

                    messagebox.showinfo(title=website, message=f"The username and password for {website} is\n\n"
                                                               f"Username: {email}\n"
                                                               f"Password: {password}")

                    pyperclip.copy(password)

                else:
                    messagebox.showwarning(title="Error", message=f"No passwords saved for {website}.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def input_pass():
    pass_input.delete(0, END)
    ran_pass = pass_generator()
    pass_input.insert(0, ran_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = email_input.get()
    password = pass_input.get()

    new_dict = {
        website: {
            "Email": username,
            "Password": password,
        }
    }

    is_ok = False

    try:
        with open("password.json", "r"):
            pass

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="You have no passwords saved.")

    else:
        with open("password.json", "r") as json_file:
            data_dict = json.load(json_file)
            if website in data_dict:
                email = data_dict[website]["Email"]
                password = data_dict[website]["Password"]

                is_ok = messagebox.askokcancel(title="Existing details found",
                                               message=f"Existing details for {website} is found.\n\n"
                                                       f"Username: {email}\n"
                                                       f"Password: {password}\n\n"
                                                       f"Update details for {website}?")
            else:
                is_ok = True

    if len(website.strip()) != 0 and len(username.strip()) != 0 and len(password.strip()) != 0:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered.\n\nUsername: {username}"
                                               f"\nPassword: {password}\n\nProceed?")
    else:
        messagebox.showwarning(title="Error", message="One or more fields left blank.")

    if is_ok:
        try:
            with open("password.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("password.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)

        else:
            data.update(new_dict)

            with open("password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        pyperclip.copy(password)
        website_input.delete(0, END)
        pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file=r"C:\Users\karth\OneDrive\Documents\NITC\RIG\Python\pass word manager\logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

website_input = Entry()
website_input.config(width=30)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry()
email_input.config(width=49)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "abcd@email.com")

pass_input = Entry()
pass_input.config(width=30)
pass_input.grid(row=3, column=1)

search_button = Button(text="Search", command=search_pass)
search_button.config(width=15)
search_button.grid(row=1, column=2)

gen_pass = Button(text="Generate Password", command=input_pass)
gen_pass.config(width=15)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", command=save_password)
add_button.config(width=43)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
