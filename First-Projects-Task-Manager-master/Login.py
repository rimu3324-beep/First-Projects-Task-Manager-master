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
        self.deiconify()  # ← Автоматически показать
        self.grab_set()
        self.focus()
        
    
    def create_login_window(self):
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
            command=self.check_status_of_loggin
        )
        self.login_btn.pack(pady = 10)

    def check_status_of_loggin(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "123":
            self.on_login_success(True)
            messagebox.showinfo("Congrats","You logged in successful")
            self.destroy()
        elif username == "" or password == "":
            messagebox.showerror("Error", "You didnt write anything")
        else:
            messagebox.showerror("Error", "You wrote wrong information")

