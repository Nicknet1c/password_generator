import random
import tkinter as tk
import pyperclip

root = tk.Tk()
root.geometry("400x400")
root.title("PyPassword Generator")
root.configure(bg='#36454F')

# Password criteria lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# GUI functions
def generate_password():
    try:
        nr_letters = int(letters_entry.get())
        nr_symbols = int(symbols_entry.get())
        nr_numbers = int(numbers_entry.get())
    except ValueError:
        password_result.config(text="Invalid input. Please enter a valid number.", fg="red")
    else:
        # Random password for letters
        password = ""

        for letter in range(nr_letters):
            password += random.choice(letters)

        # Random password for symbols
        for symbol in range(nr_symbols):
            password += random.choice(symbols)

        # Random password for numbers
        for number in range(nr_numbers):
            password += random.choice(numbers)

        # Shuffle password characters
        password = list(password)
        random.shuffle(password)
        final_result = "".join(password)
        pyperclip.copy(final_result)
        password_result.config(text=f"Your generated password lenght is: {len(final_result)} \n The password is:  {final_result}", fg="white", bg="#36454F")

# GUI elements
password_criteria = tk.Label(root, text="Password Criteria", font=("Arial", 18), fg="white", bg="#36454F", pady=10)
password_criteria.pack()

letters_label = tk.Label(root, text="Number of letters:", font=("Arial", 12), fg="white", bg="#36454F", pady=10)
letters_label.pack()
letters_entry = tk.Entry(root, width=10)
letters_entry.pack()

symbols_label = tk.Label(root, text="Number of symbols:", font=("Arial", 10), fg="white", bg="#36454F", pady=10)
symbols_label.pack()
symbols_entry = tk.Entry(root, width=10)
symbols_entry.pack()

numbers_label = tk.Label(root, text="Number of numbers:", font=("Arial", 10), fg="white", bg="#36454F", pady=10)
numbers_label.pack()
numbers_entry = tk.Entry(root, width=10)
numbers_entry.pack()


generate_button = tk.Button(root, text="Generate Password and copy", font=("Arial", 10), bg="#36454F", fg="white", pady=0, command=generate_password)
generate_button.pack()

def press_button(event=None):
    generate_button.invoke()
    generate_password()
root.bind("<Return>", press_button)


password_result = tk.Label(root, text="", font=("Arial", 12), bg="#36454F")
password_result.pack()


root.mainloop()
