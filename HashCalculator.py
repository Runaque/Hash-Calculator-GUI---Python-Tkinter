import hashlib
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from tkinter import font
import tkinter.font as tkFont

def calculate_hash(algorithm, data):
    hash_function = getattr(hashlib, algorithm)
    return hash_function(data).hexdigest()

def calculate():
    try:
        file_path = file_path_var.get()
        if file_path:
            with open(file_path, 'rb') as file:
                data = file.read()
        else:
            data = manual_input.get("1.0", tk.END).strip().encode()

        if not data:
            messagebox.showerror("Error", "Please provide input data or select a file.")
            return

        result_display.delete("1.0", tk.END)
        for algorithm in ["md5", "sha1", "sha256", "sha512"]:
            hash_result = calculate_hash(algorithm, data)
            result_display.insert(tk.END, f"{algorithm.upper()} hash: ", "bold")
            result_display.insert(tk.END, f"{hash_result}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_var.set(file_path)

def clear_entries():
    file_path_var.set("")
    manual_input.delete("1.0", tk.END)
    result_display.delete("1.0", tk.END)

def main():
    global manual_input, result_display, file_path_var

    # Setting up the main window
    root = tk.Tk()
    root.title("Hash Calculator")
    root.geometry("1200x450")

    # Allow window resizing
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)

    # File selection
    file_path_var = tk.StringVar()
    file_frame = tk.Frame(root)
    file_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
    file_label = tk.Label(file_frame, text="Select File: ")
    file_label.pack(side=tk.LEFT)
    file_entry = tk.Entry(file_frame, textvariable=file_path_var, width=50)
    file_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    file_button = tk.Button(file_frame, text="Browse", command=open_file)
    file_button.pack(side=tk.LEFT)

    # Manual input field
    manual_label = tk.Label(root, text="Or enter data manually:")
    manual_label.grid(row=1, column=0, sticky="w", padx=10)
    manual_input = scrolledtext.ScrolledText(root, width=70, height=5)
    manual_input.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

    # Button frame for Calculate and Clear Entry buttons
    button_frame = tk.Frame(root)
    button_frame.grid(row=3, column=0, pady=10)
    
    # Calculate button
    calculate_button = tk.Button(button_frame, text="Calculate Hash", command=calculate)
    calculate_button.pack(side=tk.LEFT, padx=5)

    # Clear Entry button
    clear_button = tk.Button(button_frame, text="Clear Entry", command=clear_entries)
    clear_button.pack(side=tk.LEFT, padx=5)

    # Result display
    result_display = scrolledtext.ScrolledText(root, width=70, height=10)
    result_display.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")

    # Adding tag for bold text
    result_display.tag_configure("bold", font=font.Font(root, weight="bold"))

    # Signature label
    signature_font = tkFont.Font(root, family="Helvetica", size=10, weight="normal")
    signature_label = tk.Label(root, text="Made in Antwerp by Runaque", font=signature_font, fg="slategrey")
    signature_label.grid(row=5, column=0, pady=10, sticky="n")

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
