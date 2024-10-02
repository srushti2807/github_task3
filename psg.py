import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(password_length_entry.get())
        if length < 6:
            messagebox.showwarning("Weak Password", "Password length should be at least 6 characters.")
            return
        
        # Define character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure password includes at least one of each type of character
        all_characters = lower + upper + digits + symbols
        password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(symbols)

        # Fill the rest of the password length with random characters from all sets
        password += ''.join(random.choice(all_characters) for i in range(length - 4))

        # Shuffle to avoid predictable patterns
        password_list = list(password)
        random.shuffle(password_list)
        final_password = ''.join(password_list)

        # Display password in the result label
        result_label.config(text=f"Generated Password: {final_password}", font=("Courier", 14, "bold"), fg="#27ae60")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = result_label.cget("text").replace("Generated Password: ", "")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("🔐 Professional Password Generator")
root.geometry("500x350")
root.config(bg="#34495e")

# Title label with better font and color
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), fg="#ecf0f1", bg="#34495e")
title_label.pack(pady=10)

# Subtitle with instructions
instruction_label = tk.Label(root, text="Enter desired password length (minimum 6):", font=("Arial", 12), fg="#bdc3c7", bg="#34495e")
instruction_label.pack(pady=5)

# Entry box for password length
password_length_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=10, relief="solid", bd=2)
password_length_entry.pack(pady=5)

# Generate button with appealing color
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#1abc9c", fg="white", width=20, command=generate_password, relief="raised", bd=3)
generate_button.pack(pady=10)

# Display generated password
result_label = tk.Label(root, text="", font=("Arial", 12), fg="#2ecc71", bg="#34495e")
result_label.pack(pady=10)

# Copy button with professional color scheme
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), bg="#3498db", fg="white", width=20, command=copy_to_clipboard, relief="raised", bd=3)
copy_button.pack(pady=10)

# Footer label
footer_label = tk.Label(root, text="Professional Password Generator - Secure Your Accounts!", font=("Arial", 10, "italic"), fg="#95a5a6", bg="#34495e")
footer_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
