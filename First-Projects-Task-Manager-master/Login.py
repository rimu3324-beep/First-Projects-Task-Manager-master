import json
import customtkinter
from tkinter import messagebox

class Login(customtkinter.CTk):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        #Loggin window
        self.geometry("400x350")
        self.title("TaskLoggin")
        self.resizable(False, False)

        #Fonts For login Window
        self.font_italic_bold = customtkinter.CTkFont(family="Arial", size=18, weight="bold", slant="italic")
        self.font_for_entry_text = customtkinter.CTkFont("Arial", size=13, weight="bold", slant="roman")

        self.deiconify()

        self.create_login_window()
        self.deiconify()  
        self.grab_set()
        self.focus()
        
    def create_login_window(self):
        
        def registr_window():
            #Hide window
            self.withdraw()
            
            #Show new(regist) window
            regist_wind = customtkinter.CTkToplevel()
            regist_wind.title("Regist Window")
            regist_wind.geometry("400x350")
            
            #Regist Form

            #login username
            customtkinter.CTkLabel(regist_wind, text="Create Username", font=self.font_italic_bold).pack(pady=(10,5))
            self.create_username_entry = customtkinter.CTkEntry(regist_wind, font=self.font_for_entry_text)
            self.create_username_entry.pack(pady = 10)

            #Login password
            customtkinter.CTkLabel(regist_wind, text="Password", font=self.font_italic_bold).pack(pady=(10,5))
            self.create_password_entry = customtkinter.CTkEntry(regist_wind, show="*", font=self.font_for_entry_text)
            self.create_password_entry.pack(pady = 10)

            #Ask question (WILL YOU ENJOY MY APP)
            check_box_ask = customtkinter.CTkCheckBox(regist_wind, text="Will you enjoy in my app?")
            check_box_ask.pack(pady = 5)

            #Regist button
            regist_button = customtkinter.CTkButton(
                regist_wind,
                text="Registration",
                font=self.font_italic_bold,
                command=save_data
            )
            regist_button.pack(pady = 5)


        #Functions for read data
        def log_in_with_data():
            #read data.json
            with open("data.json", "r") as login_info:
                data = json.load(login_info)
            
            username_data = data["username"]
            password_data = data["password"]
            
            #Check if its true
            if username_data == self.create_login_window(self.username_entry) and password_data == self.create_login_window(self.password_entry):
                self.on_login_success(True)
                messagebox.showinfo("Congrats","You logged in successful")
                self.destroy()
            elif username_data == "" or password_data == "":
                messagebox.showerror("Error", "You didnt write anything")
            else:
                messagebox.showerror("Error", "You wrote wrong information")    
        
            #Function for save data
        def save_data():
            #Main things
            username = self.create_username_entry.get()
            password = self.create_password_entry.get()


            #Pattern data
            data = {
                "username": username,
                "password": password
            }

            #Save data in pattern
            with open("data.json", 'w') as file_save:
                json.dump(data, file_save, indent=4)


            #Inform that user Regist acc successfully 
            messagebox.showinfo("INFO", "You successfully register, pls restart app and log in")
                
            #Show again Loggin window
            self.create_login_window()
            
        
        #login username
        customtkinter.CTkLabel(self, text="Username", font=self.font_italic_bold).pack(pady=(10,5))
        self.username_entry = customtkinter.CTkEntry(self, font=self.font_for_entry_text)
        self.username_entry.pack(pady = 10)

        #Login password
        customtkinter.CTkLabel(self, text="Password", font=self.font_italic_bold).pack(pady=(10,5))
        self.password_entry = customtkinter.CTkEntry(self, show="*", font=self.font_for_entry_text)
        self.password_entry.pack(pady = 10)

        #login btn
        self.login_btn = customtkinter.CTkButton(
            self,
            text="Login",
            font=self.font_italic_bold,
            command=log_in_with_data
        )
        self.login_btn.pack(pady = 10)

        #For Regist button 
        self.register_button = customtkinter.CTkButton(
            self,
            text="Registration",
            font=self.font_italic_bold,
            command=registr_window
        )
        self.register_button.pack(pady = 10)

