import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
import pyperclip

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Selector")
        self.root.geometry("250x550")  # Adjusted window size
        
        # Button to select directory
        self.select_dir_button = tk.Button(self.root, text="Select Directory", command=self.select_directory)
        self.select_dir_button.pack(pady=10)
        
        # Buttons for Select All / Deselect All
        self.select_all_button = tk.Button(self.root, text="Select All", command=self.select_all)
        self.select_all_button.pack(pady=5)
        
        self.deselect_all_button = tk.Button(self.root, text="Deselect All", command=self.deselect_all)
        self.deselect_all_button.pack(pady=5)
        
        # Frame to hold checkboxes
        self.checkboxes_frame = tk.Frame(self.root)
        self.checkboxes_frame.pack(pady=10, fill="both", expand=True)
        
        # Scrollable list for checkboxes
        self.canvas = tk.Canvas(self.checkboxes_frame)
        self.scrollbar = ttk.Scrollbar(self.checkboxes_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        self.file_vars = []  # List to hold the variables associated with each file checkbox
        
        # Button to create .txt file
        self.create_txt_button = tk.Button(self.root, text="Create .txt File", command=self.create_txt_file)
        self.create_txt_button.pack(pady=5)
        
        # Button to copy to clipboard
        self.copy_clipboard_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_clipboard_button.pack(pady=5)
        
        # Button for quick export
        self.quick_export_button = tk.Button(self.root, text="Quick Export", command=self.quick_export)
        self.quick_export_button.pack(pady=5)
        
        # Button for displaying code
        self.display_code_button = tk.Button(self.root, text="Display Code", command=self.display_code_window)
        self.display_code_button.pack(pady=5)
        
        # Enable mouse scrolling
        self.root.bind_all("<MouseWheel>", self.on_mouse_scroll)

    def on_mouse_scroll(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    def select_directory(self):
        directory = filedialog.askdirectory()
        if not directory:
            return
        self.directory = directory
        self.populate_files()

    def populate_files(self):
        # Clear current checkboxes
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Get .cpp, .h, .txt, and .json files from the directory
        self.file_vars.clear()
        for filename in os.listdir(self.directory):
            if filename.endswith((".cpp", ".h", ".txt", ".json")):
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(self.scrollable_frame, text=filename, variable=var)
                checkbox.pack(anchor='w')
                self.file_vars.append((filename, var))

    def format_file_content(self, filename):
        file_type = {
            ".cpp": "CPP File",
            ".h": "Header File",
            ".txt": "Text File",
            ".json": "JSON File"
        }.get(os.path.splitext(filename)[1], "File")
        
        label = f"--- {filename} ({file_type}) ---"
        with open(os.path.join(self.directory, filename), 'r') as file_content:
            content = file_content.read()
        formatted_content = f"{label}\n{content}\n{'-' * 50}\n\n"
        return formatted_content

    def create_txt_file(self):
        selected_files = [filename for filename, var in self.file_vars if var.get()]
        if not selected_files:
            messagebox.showwarning("No files selected", "Please select at least one file.")
            return
        
        output_filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not output_filename:
            return
        
        with open(output_filename, 'w') as f:
            for filename in selected_files:
                f.write(self.format_file_content(filename))
        
        messagebox.showinfo("Success", f"Text file created: {output_filename}")

    def copy_to_clipboard(self):
        selected_files = [filename for filename, var in self.file_vars if var.get()]
        if not selected_files:
            messagebox.showwarning("No files selected", "Please select at least one file.")
            return
        
        combined_content = ""
        for filename in selected_files:
            combined_content += self.format_file_content(filename)
        
        pyperclip.copy(combined_content)
        messagebox.showinfo("Success", "Files copied to clipboard!")

    def quick_export(self):
        selected_files = [filename for filename, var in self.file_vars if var.get()]
        if not selected_files:
            messagebox.showwarning("No files selected", "Please select at least one file.")
            return
        
        # Save to /Users/Shared
        shared_folder = "/Users/Shared"
        if not os.path.exists(shared_folder):
            os.makedirs(shared_folder)
        
        # Find the next available CodeSnippet number
        count = 1
        while os.path.exists(os.path.join(shared_folder, f"CodeSnippet {count}.txt")):
            count += 1
        
        quick_export_file = os.path.join(shared_folder, f"CodeSnippet {count}.txt")
        
        with open(quick_export_file, 'w') as f:
            for filename in selected_files:
                f.write(self.format_file_content(filename))
        
        messagebox.showinfo("Success", f"Quick export saved: {quick_export_file}")

    def select_all(self):
        for _, var in self.file_vars:
            var.set(True)

    def deselect_all(self):
        for _, var in self.file_vars:
            var.set(False)

    def display_code_window(self):
        selected_files = [filename for filename, var in self.file_vars if var.get()]
        if len(selected_files) != 1:
            messagebox.showwarning("Select One File", "Please select exactly one file to display its contents.")
            return
        
        display_window = tk.Toplevel(self.root)
        display_window.title(f"Displaying: {selected_files[0]}")
        display_window.geometry("600x400")
        
        text_area = scrolledtext.ScrolledText(display_window, wrap=tk.WORD)
        text_area.pack(fill="both", expand=True)
        
        with open(os.path.join(self.directory, selected_files[0]), 'r') as file_content:
            content = file_content.read()
        
        text_area.insert(tk.END, content)
        text_area.configure(state='disabled')  # Make it read-only

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()
