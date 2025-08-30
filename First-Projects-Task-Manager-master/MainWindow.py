import customtkinter
from tkinter import messagebox
import os
import sys
from PIL import Image, ImageTk

class main_Window(customtkinter.CTk): 
    def __init__(self):
        super().__init__()
        #Name of the app and base geometry
        #Window
        self.title("TaskApp")
        self.geometry("1250x850")
        self.tasks = []


        self.show_main_window()
        self.deiconify()


    
    def show_main_window(self):
            
            #Fonts
            font_bold = customtkinter.CTkFont(family="Arial", size=20, weight="bold")
            font_bold_for_information = customtkinter.CTkFont(family="Arial", size=15, weight="bold")


            self.deiconify()
            self.focus()
            
            #FUNCTIONS


            #Function create new task
            def create_new_task():
                task_text = nameOfTask.get()
                if task_text != "":
                    self.tasks.append(task_text)
                    nameOfTask.delete(0, 'end')
                    update_task_display()

            def update_task_display():
                for widget in self.tasks_frame.winfo_children():
                    widget.destroy()
                
                for i, task in enumerate(self.tasks, 1):
                    task_label = customtkinter.CTkLabel(self.tasks_frame, text=f"{i}. {task}")
                    task_label.pack(fill="x", pady=2)

            def exit():
                sys.exit()

            def main_window_show_frame():
                pass
            
            def information_window():
                info_window = customtkinter.CTkToplevel()
                info_window.title("Information")
                info_window.geometry("450x800")
                info_window.resizable(False,False)

                image_frame = customtkinter.CTkFrame(info_window)
                image_frame.pack(pady=15)
                
                # Загружаем и отображаем изображение
                try:
                    image_path = "Images/anime-girl-playing-chess-focusing-strategy-with-thoughtful-expression_1282444-174923.avif"
                    if os.path.exists(image_path):
                        # Открываем изображение с PIL
                        pil_image = Image.open(image_path)
                        
                        # Изменяем размер
                        pil_image = pil_image.resize((400, 250), Image.Resampling.LANCZOS)
                        
                        # Конвертируем для CTk
                        ct_image = customtkinter.CTkImage(
                            light_image=pil_image,
                            dark_image=pil_image,
                            size=(400, 250)
                        )
                        
                        # Создаем метку с изображением
                        image_label = customtkinter.CTkLabel(image_frame, image=ct_image, text="")
                        image_label.pack(pady = 5)
                    else:
                        messagebox.showwarning("Warning", "Image file not found")
                except Exception as e:
                    messagebox.showerror("Error", f"Cannot load image: {str(e)}")

                info_text = """
                    [Name]
                    TaskAppApplication - Your personal Task Manager
                    
                    [Features]
                    -Create For Free Your Own Tasks And
                    --->Complete Them
                    -Mark Task as Completed and Uncompleted and
                    --->see how progress change(Isnt done)
                    -More Features later


                    [ABOUT APP UDATE]
                    App_version = [1.0.0]
                    App_stability = unstable


                """

                info_text_for_window = customtkinter.CTkLabel(info_window, text=info_text, font=font_bold_for_information, justify = "left")
                info_text_for_window.pack(pady=2, padx=2, side = "bottom")

                
            #Sidebar create
            self.sidebar = customtkinter.CTkFrame(self)
            self.sidebar.pack(side = "left", padx = 10, pady = 10)

            #Panel to manage
            customtkinter.CTkLabel(self.sidebar, text="Panel to change frame", font=font_bold).pack(pady = 5)

            #Buttons
            button_main_window = customtkinter.CTkButton(self.sidebar,text="Main", font=font_bold, command=main_window_show_frame).pack(pady=5)
            infotmation_button = customtkinter.CTkButton(self.sidebar,text="Information", font=font_bold, command=information_window)
            infotmation_button.pack(pady=5)
            customtkinter.CTkButton(self.sidebar,text="Exit",font=font_bold, command=exit).pack(pady=5)

            #Main Frame
            self.information_about_task = customtkinter.CTkFrame(self)
            self.information_about_task.pack(side = "right", padx = 15, pady=15)

            customtkinter.CTkLabel(self.information_about_task, text="Your Progress", font=font_bold).pack(pady=10)
            progress_bar = customtkinter.CTkProgressBar(self.information_about_task)
            progress_bar.pack(pady=10)
            progress_bar.set(0)
            
            #List of tasks

            #View Task
            self.TabView = customtkinter.CTkTabview(self.information_about_task)
            self.TabView.pack(pady = 10, padx = 10, expand=True, fill = "both")

            #Tabs
            tab_tasks = self.TabView.add("Tasks")
            self.tasks_frame = customtkinter.CTkScrollableFrame(tab_tasks)
            self.tasks_frame.pack(fill="both", expand=True, padx=10, pady=10)
            completed_tasks = self.TabView.add("Completed Tasks")
            
            #Create new task
            nameOfTaskLabel = customtkinter.CTkLabel(self.information_about_task, text="Write which task do you wanna do", font=font_bold_for_information).pack(pady=5)
            nameOfTask = customtkinter.CTkEntry(self.information_about_task)
            nameOfTask.pack(pady=5)

            #Button for create task
            ButtonCreateTaSk = customtkinter.CTkButton(self.information_about_task, text="Create new Task", command=create_new_task, font=font_bold).pack(pady = 10)


            #Center window 
            self.main_window = customtkinter.CTkFrame(self)
            self.main_window.pack(fill = "both", expand = True, padx = 15, pady = 15)
            
            #Main Window Texts
            self.main_label = customtkinter.CTkLabel(self.main_window, text="Main Panel", font=font_bold).pack(pady = 5)

