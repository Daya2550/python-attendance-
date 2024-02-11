import tkinter as tk
import datetime
import name

def save_attendance():
    current_date = datetime.datetime.now().strftime('%d-%m-%Y')
    formatted_time = datetime.datetime.now().strftime('%H:%M')
    file_name = f"sy2024_{current_date}.txt"
    subject = subject_entry.get()

    with open(file_name, "w") as file:
        file.write(f"Subject: {subject}\n")
        file.write(f"Date: {current_date}\n")
        file.write(f"Time: {formatted_time}\n")

    for i in range(1, 5):
        present = present_vars[i].get()
        if present == 1:
            present_students.append(i)
        else:
            absent_students.append(i)

    with open(file_name, "a") as file:
        file.write("Present Students:\n")
        for student in present_students:
            file.write(f"{student}: {name.stuname(student)}\n")
        file.write("Absent Students:\n")
        for student in absent_students:
            file.write(f"{student}: {name.stuname(student)}\n")
    
    present_label.config(text=f"Total present: {len(present_students)}")
    absent_label.config(text=f"Total absent: {4 - len(present_students)}")
    success_label.config(text="Attendance saved successfully!")

root = tk.Tk()
root.title("Attendance Management")

present_vars = {i: tk.IntVar() for i in range(1, 5)}
present_students = []
absent_students = []

subject_label = tk.Label(root, text="Enter subject:")
subject_label.grid(row=0, column=0)
subject_entry = tk.Entry(root)
subject_entry.grid(row=0, column=1)

save_button = tk.Button(root, text="Save Attendance", command=save_attendance)
save_button.grid(row=0, column=2)

for i in range(1, 5):
    label = tk.Label(root, text=f"Roll No {i}")
    label.grid(row=i, column=0)
    present_checkbox = tk.Checkbutton(root, variable=present_vars[i], onvalue=1, offvalue=0)
    present_checkbox.grid(row=i, column=1)

present_label = tk.Label(root, text="Total present: 0")
present_label.grid(row=5, column=0)

absent_label = tk.Label(root, text="Total absent: 0")
absent_label.grid(row=5, column=1)

success_label = tk.Label(root, text="")
success_label.grid(row=6, columnspan=2)

root.mainloop()
