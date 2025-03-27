# CODE:

import tkinter as tk
from tkinter import messagebox
import os
import base64


# Define the main class for the project
class PythonScriptingProject:
    def __init__(self):
        # Initialize filename as an empty string
        self.filename = ""

    # Function to select or create a file
    def select_create_file(self):
        self.filename = input("Enter the filename (without .txt extension): ") + ".txt"
        try:
            # Create the file it does not exist
            with open(self.filename, 'a'):
                pass
            messagebox.showinfo("File Created", f"{self.filename} created successfully!")
        except Exception as e:
            # Show error message if any exception occurs
            messagebox.showerror("Error", str(e))

    # Function to display all numbers, their total and average
    def display_all(self):
        # Check if file exists
        if os.path.exists(self.filename):
            # Open file in read mode
            with open(self.filename, 'r') as file:
                # Read numbers from file
                numbers = [int(line.strip()) for line in file]
                # Calculate total
                total = sum(numbers)
                # Calculate average
                average = total / len(numbers) if numbers else 0
                # Show numbers, total and average
                tk.messagebox.showinfo("File Content", f"Numbers: {numbers}\nTotal: {total}\nAverage: {average:.2f}")
        else:
            # Show error message if file does not exist
            messagebox.showerror("File Not Found", "Please select/create a data file first.")

    # Function to display all numbers sorted
    def display_sorted(self):
        # Check if filename is not empty
        if not self.filename:
            # Show error message if filename is empty
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        try:
            # Open file in read mode
            with open(self.filename, 'r') as file:
                # Read and sort numbers from file
                numbers = sorted([float(line.strip()) for line in file.readlines()])
                # Show sorted numbers
                messagebox.showinfo("Sorted Numbers", ", ".join(map(str, numbers)))
        except Exception as e:
            # Show error message if any exception occurs
            messagebox.showerror("Error", str(e))

    # Function to search for a number and display its occurrences
    def search_occurs(self):
        # Check if filename is not empty
        if not self.filename:
            # Show error message if filename is empty
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        try:
            # Get the number to search
            target = float(input("Enter the number to search: "))
            # Open file in read mode
            with open(self.filename, 'r') as file:
                # Count occurrences of the number
                occurrences = sum(1 for line in file if float(line.strip()) == target)
                # Show search result
                messagebox.showinfo("Search Result", f"{target} occurs {occurrences} times.")
        except Exception as e:
            # Show error message if any exception occurs
            messagebox.showerror("Error", str(e))

    # Function to display the largest number
    def largest(self):
        # Check if filename is not empty
        if not self.filename:
            # Show error message if filename is empty
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        try:
            # Open file in read mode
            with open(self.filename, 'r') as file:
                # Find the largest number
                largest = max(float(line.strip()) for line in file.readlines())
                # Show the largest number
                messagebox.showinfo("Largest Number", f"The largest number is: {largest}")
        except Exception as e:
            # Show error message if any exception occurs
            messagebox.showerror("Error", str(e))

    # Function to append a number to the file
    def append_number(self):
        # Check if filename is not empty
        if not self.filename:
            # Show error message if filename is empty
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        try:
            # Get the number(s) to append
            number = input("Enter number(s) to append (comma-separated for multiple): ")
            # Open file in append mode
            with open(self.filename, 'a') as file:
                # Append the number(s) to the file
                file.write('\n'.join(number.split(',')) + '\n')
            messagebox.showinfo("Append Success", "Number(s) appended successfully.")
        except Exception as e:
            # Show error message if any exception occurs
            messagebox.showerror("Error", str(e))

    # Function to encrypt the file
    def encrypt(self):
        # Check if filename is not empty
        if not self.filename:
            # Show error message if filename is empty
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        # Open file in read mode
        with open(self.filename, 'r') as file:
            # Read content from file
            content = file.read()
        # Encrypt the content
        encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        # Open file in write mode
        with open(self.filename, 'w') as file:
            # Write the encrypted content to the file
            file.write(encoded_content)
        # Show success message
        tk.messagebox.showinfo("Encrypt", "File encrypted successfully.")

    # Function to decrypt the file
    def decrypt(self):
        # Check if filename is not empty
        if not self.filename:
            # Show error message if filename is empty
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        # Open file in read mode
        with open(self.filename, 'r') as file:
            content = file.read()

        try:
            # Decrypt the content
            decoded_content = base64.b64decode(content.encode('utf-8')).decode('utf-8')
        except ValueError:
            # Show error message if decryption fails
            tk.messagebox.showerror("Error", "Decryption failed. The file might not be encrypted or is corrupted.")
            return
        # Open file in write mode
        with open(self.filename, 'w') as file:
            # Write the decrypted content to the file
            file.write(decoded_content)
        # Show success message
        tk.messagebox.showinfo("Decrypt", "File decrypted successfully.")

    # Function to exit the program
    @staticmethod
    def exit_program(root):
        # Close the tkinter window
        root.destroy()


def main():
    # Create a tkinter window
    root = tk.Tk()
    # Set the title of the window
    root.title("UNH Scripting w/Python")
    # Set scaling to improve widget appearance
    root.tk.call('tk', 'scaling', 1.5)
    # Create an instance of the PythonScriptingProject class
    processor = PythonScriptingProject()

    # Create a label
    label = tk.Label(root, text="UNH Scripting w/Python", fg='Yellow', bg='Blue')
    # Add the label to the window
    label.pack()

    # Create a label for the filename
    filename_label = tk.Label(root, text="Current data file being processed: None")
    # Add the filename label to the window
    filename_label.pack()

    # Define functions to update the filename label and call the methods of the PythonScriptingProject class
    def update_filename_label():
        filename_label.config(text=f"Current data file being processed: {processor.filename}")

    def select_create_file():
        processor.select_create_file()
        update_filename_label()

    def display_all():
        processor.display_all()

    def display_sorted():
        processor.display_sorted()

    def search_occurs():
        processor.search_occurs()

    def display_largest():
        processor.largest()

    def append_number():
        processor.append_number()

    def encrypt():
        processor.encrypt()

    def decrypt():
        processor.decrypt()

    def exit_program():
        processor.exit_program(root)

    # Create buttons and add them to the window
    btn_select_create = tk.Button(root, text="Select/Create File", fg='Green',
                                  bg='Yellow', command=select_create_file)
    btn_select_create.pack()

    btn_display_all = tk.Button(root, text="Display All", fg='Black',
                                bg='BlueViolet', command=display_all)
    btn_display_all.pack()

    btn_display_sorted = tk.Button(root, text="Display Sorted", fg='Black', bg='Lime',
                                   command=display_sorted)
    btn_display_sorted.pack()

    btn_search_occurs = tk.Button(root, text="Search/Occurs", fg='Black', bg='Orange', command=search_occurs)
    btn_search_occurs.pack()

    btn_display_largest = tk.Button(root, text="Display Largest", fg='Black', bg='Grey', command=display_largest)
    btn_display_largest.pack()

    btn_append_number = tk.Button(root, text="Append Number", fg='Black', bg='Aquamarine', command=append_number)
    btn_append_number.pack()

    btn_encrypt = tk.Button(root, text="Encrypt", fg='Black', bg='CornflowerBlue', command=encrypt)
    btn_encrypt.pack()

    btn_decrypt = tk.Button(root, text="Decrypt", fg='Black', bg='BurlyWood', command=decrypt)
    btn_decrypt.pack()

    btn_exit = tk.Button(root, text="Exit", fg='Black', bg='Red', command=exit_program)
    btn_exit.pack()

    # Start the tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    # Call the main function
    main()
