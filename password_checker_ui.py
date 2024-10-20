import re
import tkinter as tk

def password_complexity_checker(password):
    # Minimum length of the password
    min_length = 8  # Updated minimum length to 8
    very_strong_length = 16  # Minimum length for "Very Strong"
    
    # Define regex patterns for complexity checks
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Password length condition
    if len(password) < min_length:
        return "Password is too short. Must be at least 8 characters."
    
    # Check for "Very Strong" password first
    if len(password) >= very_strong_length and has_upper and has_lower and has_digit and has_special:
        return "Very Strong"
    
    # Check for "Strong" password
    if (has_lower or has_upper) and has_digit and has_special:
        return "Strong"
    
    # Check for "Medium" password
    if (has_lower or has_upper) and has_digit and not has_special:
        return "Medium"
    
    # If none of the above, return "Weak"
    if password.isdigit() or password.isalpha() or re.match(r'^[!@#$%^&*(),.?":{}|<>]+$', password):
        return "Weak"

    return "Weak"  # Default to "Weak" if no other conditions are met

# Function to check password complexity and update the UI in real-time
def check_password_real_time(event):
    password = password_entry.get()
    result = password_complexity_checker(password)
    
    # Update the result label based on the complexity level
    if "too short" in result.lower():
        result_label.config(text=result, bg="red", fg="white")
    elif result == "Weak":
        result_label.config(text="Password is Weak", bg="red", fg="white")
    elif result == "Medium":
        result_label.config(text="Password is Medium", bg="orange", fg="black")
    elif result == "Strong":
        result_label.config(text="Password is Strong", bg="green", fg="white")
    elif result == "Very Strong":
        result_label.config(text="Password is Very Strong", bg="blue", fg="white")

# Create the main window
window = tk.Tk()
window.title("Real-Time Password Complexity Checker")
window.geometry("400x300")
window.config(bg="lightgrey")

# Add a label and input field for the password
password_label = tk.Label(window, text="Enter your password:", font=("Arial", 14), bg="lightgrey")
password_label.pack(pady=10)

password_entry = tk.Entry(window, show="*", width=30, font=("Arial", 12))
password_entry.pack(pady=5)

# Bind the password entry to the key release event for real-time update
password_entry.bind("<KeyRelease>", check_password_real_time)

# Add a label to display the result, which will change color
result_label = tk.Label(window, text="", font=("Arial", 14), width=30, height=2)
result_label.pack(pady=20)

# Start the main event loop
window.mainloop()
