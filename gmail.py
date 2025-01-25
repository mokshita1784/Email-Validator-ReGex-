import tkinter as tk
from tkinter import messagebox
import re  # Import the regular expression module

# Function to validate the email using regex
def validate_email():
    email = email_entry.get()  # Get the input from the email entry field
    
    # Regular expression pattern for a valid email
    email_regex = r'^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Match the email with the regex pattern
    if re.match(email_regex, email):
        messagebox.showinfo("Success", "Valid Email")  # Show success message
    else:
        messagebox.showerror("Error", "Invalid Email Format")  # Show error message

# Create the main application window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x300")
root.configure(bg="light green")  # Set the background color to orange

# Create a label for the email field
email_label = tk.Label(root, text="Enter your Email:", bg="green", font=("Arial", 12, "bold"))
email_label.pack(pady=10)

# Create an entry field for email input
email_entry = tk.Entry(root, width=30, font=("Arial", 12))
email_entry.pack(pady=5)

# Create a button to validate the email
validate_button = tk.Button(root, text="Validate", command=validate_email, font=("Arial", 12), bg="green", fg="white")
validate_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
