import tkinter as tk

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x500")

# Heading
heading_label = tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

subheading_label = tk.Label(root, text="Fill in this form to register", font=("Arial", 10))
subheading_label.grid(row=1, column=0, columnspan=2, pady=5)

# First Name
first_name_label = tk.Label(root, text="First Name")
first_name_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

first_name_entry = tk.Entry(root)
first_name_entry.grid(row=2, column=1, padx=10, pady=5)

# Last Name
last_name_label = tk.Label(root, text="Last Name")
last_name_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

last_name_entry = tk.Entry(root)
last_name_entry.grid(row=3, column=1, padx=10, pady=5)

# Email
email_label = tk.Label(root, text="E-mail")
email_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, padx=10, pady=5)

# Date of Birth
dob_label = tk.Label(root, text="Date of Birth")
dob_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

dob_entry = tk.Entry(root)
dob_entry.grid(row=5, column=1, padx=10, pady=5)

# Username
username_label = tk.Label(root, text="Set Username")
username_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=6, column=1, padx=10, pady=5)

# Password
password_label = tk.Label(root, text="Set Password")
password_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=7, column=1, padx=10, pady=5)

# Gender
gender_label = tk.Label(root, text="Gender")
gender_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)

male_radio = tk.Radiobutton(root, text="Male", value="Male")
male_radio.grid(row=8, column=1, sticky="w")

female_radio = tk.Radiobutton(root, text="Female", value="Female")
female_radio.grid(row=9, column=1, sticky="w")

others_radio = tk.Radiobutton(root, text="Others", value="Others")
others_radio.grid(row=10, column=1, sticky="w")

# Course (as Entry)
course_label = tk.Label(root, text="Course")
course_label.grid(row=11, column=0, sticky="w", padx=10, pady=10)

course_entry = tk.Entry(root)
course_entry.grid(row=11, column=1, padx=10, pady=10)

root.mainloop()
