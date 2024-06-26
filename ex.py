import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import segregate

def segregate_files():
    directory = directory_var.get()
    if directory:
        segregate.segregate_files_by_extension(directory)
        result_label.config(text="Files segregated and moved successfully.")
    else:
        result_label.config(text="Please select a directory.")

def browse_directory():
    directory = filedialog.askdirectory()
    directory_var.set(directory)

def segregate_all():
    segregate_button.config(state=tk.NORMAL)
    segregate_by_type_button.config(state=tk.NORMAL)
    check_type_frame.pack_forget()

def segregate_by_type():
    segregate_button.config(state=tk.DISABLED)
    segregate_by_type_button.config(state=tk.DISABLED)
    check_type_frame.pack(fill=tk.X, padx=10, pady=5)

def segregate_selected_types():
    segregate.check_type = [image_var.get(), video_var.get(), audio_var.get(), document_var.get(), programming_var.get(), application_var.get(), setup_var.get(), others_var.get()]
    segregate_files()

# Create main window
root = tk.Tk()
root.title("File Segregator")
root.geometry("500x350")
root.resizable(False, False)

# Frame for directory selection
directory_frame = ttk.Frame(root)
directory_frame.pack(padx=10, pady=10)

# Directory label
directory_label = ttk.Label(directory_frame, text="Select Directory:")
directory_label.grid(row=0, column=0, padx=5, pady=5)

# Directory dropdown
directory_var = tk.StringVar()
directory_entry = ttk.Entry(directory_frame, textvariable=directory_var, width=40)
directory_entry.grid(row=0, column=1, padx=5, pady=5)

# Browse button
browse_button = ttk.Button(directory_frame, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Segregate button
segregate_button = ttk.Button(root, text="Segregate Files", command=segregate_files)
segregate_button.pack(pady=5)

# Segregate by type button
segregate_by_type_button = ttk.Button(root, text="Segregate by Type", command=segregate_by_type)
segregate_by_type_button.pack(pady=5)

# Result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=5)

# Menu
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Segregate All Files", command=segregate_all)
file_menu.add_command(label="Segregate by Type", command=segregate_by_type)
menubar.add_cascade(label="File Segregator", menu=file_menu)

# Checkboxes for file types
check_type_frame = ttk.Frame(root)

image_var = tk.IntVar()
image_checkbox = ttk.Checkbutton(check_type_frame, text="Images", variable=image_var)
image_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

video_var = tk.IntVar()
video_checkbox = ttk.Checkbutton(check_type_frame, text="Videos", variable=video_var)
video_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

audio_var = tk.IntVar()
audio_checkbox = ttk.Checkbutton(check_type_frame, text="Audios", variable=audio_var)
audio_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

document_var = tk.IntVar()
document_checkbox = ttk.Checkbutton(check_type_frame, text="Documents", variable=document_var)
document_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

programming_var = tk.IntVar()
programming_checkbox = ttk.Checkbutton(check_type_frame, text="Programming Files", variable=programming_var)
programming_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

application_var = tk.IntVar()
application_checkbox = ttk.Checkbutton(check_type_frame, text="Applications", variable=application_var)
application_checkbox.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

setup_var = tk.IntVar()
setup_checkbox = ttk.Checkbutton(check_type_frame, text="Setup Files", variable=setup_var)
setup_checkbox.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

others_var = tk.IntVar()
others_checkbox = ttk.Checkbutton(check_type_frame, text="Others", variable=others_var)
others_checkbox.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

segregate_types_button = ttk.Button(check_type_frame, text="Segregate Selected Types", command=segregate_selected_types)
segregate_types_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()