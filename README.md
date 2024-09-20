
<img width="362" alt="Screenshot 2024-09-19 at 9 00 06 PM" src="https://github.com/user-attachments/assets/1e25fb5b-c347-49fb-987d-ce0843449978">

Overview
This Python script provides an easy-to-use graphical interface that allows users to:
- Select a directory and list all `.cpp`, `.h`, `.txt`, and `.json` files.
- Check and preview file contents.
- Batch export selected files to a `.txt` file with neat formatting.
- Copy the selected file contents directly to the clipboard.
- Quick export files into `/Users/Shared`, with files automatically named as `CodeSnippet X.txt`.

Features
- Mouse Scrollable File List: Scroll through a list of files in a directory using the mouse wheel.
- Select All / Deselect All: Quickly select or deselect all files in the list.
- Create Formatted Text File: Export the selected files to a `.txt` file with clear labels and formatting.
- Copy to Clipboard: Copy selected file contents to the clipboard for quick sharing.
- Quick Export: Automatically saves the selected files to `/Users/Shared` as `CodeSnippet X.txt`.
- File Preview: Preview the contents of any selected file in a pop-up window.
- Supports Multiple File Types: The script handles `.cpp`, `.h`, `.txt`, and `.json` files.

Installation
1. Clone or Download the script to your local machine.
2. Install the required Python packages:
   pip install pyperclip

Note: `tkinter` is part of the standard Python library, no additional installation is needed for the GUI components.

Usage
1. Run the Script:
   python file_selector.py

2. Select Directory:
   Click "Select Directory" and choose a folder. The files (.cpp, .h, .txt, .json) will be listed with checkboxes.

3. Select Files:
   Check the files you want to work with, or use "Select All" / "Deselect All" for faster selection.

4. File Operations:
   - Create .txt File: Creates a formatted text file with the selected files' contents.
   - Copy to Clipboard: Copies the selected files' contents to your clipboard.
   - Quick Export: Automatically saves the selected files to `/Users/Shared` as `CodeSnippet X.txt`.
   - Display Code: Preview the contents of a selected file in a pop-up window.

License
This script is available for free use under the MIT License.

