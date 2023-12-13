#TASK 3 PASSWORD GENERATOR
import tkinter as tk                                 ##Using TKINTER
from tkinter import messagebox
import string
import random
import os

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # VARIABLES
        self.password_length_var = tk.StringVar(value="12")
        self.generated_password_var = tk.StringVar(value="")

        # Labels
        tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        tk.Label(root, text="Generated Password:").grid(row=1, column=0, padx=10, pady=5, sticky='w')

        # ENTRY WIDGETS
        self.password_length_entry = tk.Entry(root, textvariable=self.password_length_var)
        self.generated_password_entry = tk.Entry(root, textvariable=self.generated_password_var, state='readonly')

        self.password_length_entry.grid(row=0, column=1, padx=10, pady=5)
        self.generated_password_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        # ACCESSING BUTTONS
        tk.Button(root, text="Generate Password", command=self.generate_password).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Save to Desktop", command=self.save_to_file).grid(row=4, column=0, columnspan=2, pady=10)
   
    #THIS FUNCTION GENERATES PASSWORD
    def generate_password(self):
        try:
            password_length = int(self.password_length_var.get())
            if password_length <= 0:
                raise ValueError("Password length must be greater than 0.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid positive integer for password length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.generated_password_var.set(generated_password)
        
    #THIS FUNCTION ADDS THE PASSWORD TO CLIPBOARD
    def copy_to_clipboard(self):
        generated_password = self.generated_password_var.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(generated_password)
        self.root.update()
        messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard.")
        
    #THIS FUNCTION ALLOWS TO SAVE THE PASSWORD IN TEXT FILE ON DESKTOP
    def save_to_file(self):
        generated_password = self.generated_password_var.get()
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "generated_password.txt")

        with open(file_path, "w") as file:
            file.write(generated_password)

        messagebox.showinfo("Password Saved", f"Password saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

