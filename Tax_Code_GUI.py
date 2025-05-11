import tkinter as tk
from tkinter import messagebox
import Tax_code as tc
from datetime import datetime
import os
from DatabaseConnection import DatabaseConnection

class Tax_Code_GUI:
    
    def __init__(self, root):
        try:
            # get the absolute path of the current directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # get the path of the gi_comuni.csv file in the current directory
            self.filename = os.path.join(current_dir, "gi_comuni.csv")
            
            # check if the file exists
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"File {self.filename} non trovato. Assicurati che il file gi_comuni.csv sia nella stessa cartella del programma.")
            
            self.root = root
            self.center_window(self.root, 600, 450)
            self.root.resizable(False, False)
            self.root.configure(bg="lightblue")
            self.root.title("Tax Code Generator")
            
            # Create a frame to hold all widgets
            main_frame = tk.Frame(root, bg="lightblue")
            main_frame.pack(pady=20)
            
            # Name widgets
            tk.Label(main_frame, text="Name:", bg="lightblue").pack()
            self.name = tk.Entry(main_frame)
            self.name.pack(pady=(0, 10))

            # Surname widgets
            tk.Label(main_frame, text="Surname:", bg="lightblue").pack()
            self.surname = tk.Entry(main_frame)
            self.surname.pack(pady=(0, 10))

            # Date of Birth widgets
            tk.Label(main_frame, text="Date of Birth (dd-mm-yyyy):", bg="lightblue").pack()
            self.date_of_birth = tk.Entry(main_frame)
            self.date_of_birth.pack(pady=(0, 10))

            # Gender widgets
            tk.Label(main_frame, text="Gender (M/F):", bg="lightblue").pack()
            self.gender = tk.Entry(main_frame)
            self.gender.pack(pady=(0, 10))

            # Municipality widgets
            tk.Label(main_frame, text="Municipality:", bg="lightblue").pack()
            self.municipality = tk.Entry(main_frame)
            self.municipality.pack(pady=(0, 10))

            # Generate button
            tk.Button(main_frame, text="GENERATE", command=self.generate_tax_code).pack(pady=20)
            
            #Save button
            tk.Button(main_frame, text = "SAVE", command = self.save_data).pack(pady=20)
            
        except Exception as e:
            messagebox.showerror("Errore", str(e))
        
    def generate_tax_code(self):
        name = self.name.get()
        if not name:
            messagebox.showerror("Input Error", "fill in all the fields.")
            return
        
        surname = self.surname.get()
        if not surname:
            messagebox.showerror("Input Error", "fill in all the fields.")
            return
        date_of_birth = self.date_of_birth.get()
        if not date_of_birth:
            messagebox.showerror("Input Error", "fill in all the fields.")
            return
        try:
            datetime.strptime(date_of_birth, "%d-%m-%Y")  # Validate date format
        except ValueError:
            messagebox.showerror("Input Error", "Date format not valid enter: dd-mm-yyyy.")
            return
        
        gender = self.gender.get()
        if not gender:
            messagebox.showerror("Input Error", "fill in all the fields.")
        municipality = self.municipality.get()
        if gender not in(['M', 'F', 'm', 'f']):
            messagebox.showerror("Input error", "fill in all the fields.")
        
        name_code = tc.calculateName(name)
        surname_code = tc.calculateSurname(surname)
        date_gender_code = tc.add_data_gender(date_of_birth, gender)
        
        municipality_code = tc.calculate_cadastral_code(self.filename, municipality)
        if municipality_code is None:
            messagebox.showerror("Error", "can't read the file gi_comuni.csv")
            return
        elif municipality_code == "Municipality not found":
            messagebox.showerror("Error", "Municipality not found.")
            return
        
        try:
            partial_tax_code = surname_code + name_code + date_gender_code + municipality_code
            control_code = tc.calculate_control_code(partial_tax_code)
            tax_code = partial_tax_code + control_code
            messagebox.showinfo("Tax Code", f" Tax Code: {tax_code}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def save_data(self):
        #save the data into the database
        name = self.name.get()
        surname = self.surname.get()
        birth_date = self.date_of_birth.get()
        gender = self.gender.get()
        municipality = self.municipality.get()
        
        #show error message if one or more fields are empty
        if not name or not surname or not birth_date or not gender or not municipality:
            messagebox.showerror("Input Error", "fill in all the fields.")
            return
        
        #format birth_date from dd-mm-yyyy to yyyy-mm-dd:
        try:
            birth_date_formatted = datetime.strptime(birth_date, "%d-%m-%Y")
            birth_date = birth_date_formatted.strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Input Error", "Date format not valid enter: dd-mm-yyyy.")
            return
        
        """
        calculates the tax code when the Save button is clicked
        even if the Generate button has not been clicked yet
        """ 
        name_code = tc.calculateName(name)
        surname_code = tc.calculateSurname(surname)
        date_gender_code = tc.add_data_gender(birth_date, gender)
        
        municipality_code = tc.calculate_cadastral_code(self.filename, municipality)
        if municipality_code is None:
            messagebox.showerror("Error", "can't read the file gi_comuni.csv")
            return
        elif municipality_code == "Municipality not found":
            messagebox.showerror("Error", "Municipality not found.")
            return
        
        try:
            partial_tax_code = name_code + surname_code + date_gender_code + municipality_code
            control_code = tc.calculate_control_code(partial_tax_code)
            tax_code = partial_tax_code + control_code
            messagebox.showinfo("Tax Code", f" Tax Code: {tax_code}")
            
        #save all the data into the database
            db = DatabaseConnection()
            db.insert_tax_code(name, surname, birth_date,gender, municipality_code,tax_code)
            
            messagebox.showinfo("Success", "Data included tax id code saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
    @staticmethod
    def center_window(root, width, height):
        #center the GUI in the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
        
        
        
        
