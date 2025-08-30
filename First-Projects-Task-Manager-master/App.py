import customtkinter
from tkinter import messagebox
import Login

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #Login window
        self.login = Login.Login(self.check_login_info)
        
    def check_login_info(self, success):
        if success:
            import MainWindow
            MainWindow.main_Window()

if __name__ == "__main__":
    app = App()
    app.withdraw()
    app.mainloop()