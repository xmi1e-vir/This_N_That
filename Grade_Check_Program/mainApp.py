import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk

class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo_image = PhotoImage(file="logo.png")  
        logo_label = tk.Label(self, image=logo_image)
        logo_label.image = logo_image  
        logo_label.place(x=230, y=120)
        text_label = tk.Label(self, text='고려대학교 성적조회 시스템', font=('Arial', 17))
        text_label.place(x=160, y=60)
        go_button = tk.Button(self, text='Go', command=lambda: controller.show_frame(LoginFrame))
        go_button.place(width=100, height=40, x=250, y=310)

class LoginFrame(tk.Frame):
    def validate_password(self, input_password):
        secret_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        expected_result = [16, 16, 16, 16, 4, 4, 4]

        if len(input_password) != len(secret_array):
            return False

        result_array = [ord(input_password[i]) ^ ord(secret_array[i]) for i in range(len(input_password))]

        if result_array == expected_result: 
            return True
        return False
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def show_message():
            input_username = username_entry.get()
            input_password = password_entry.get()

            if input_username == "KCTF" and self.validate_password(input_password):
              controller.show_frame(GradesFrame)  
            else:
                messagebox.showinfo("성적 확인", "안전교육을 이수하지 않아 성적확인이 불가합니다.")

        username_frame = tk.Frame(self)
        username_frame.place(x=170,y=100)
        username_label = tk.Label(username_frame, text='username :')
        username_label.pack(side=tk.LEFT, padx=10)
        username_entry = tk.Entry(username_frame)
        username_entry.pack(side=tk.LEFT, padx=10)
        password_frame = tk.Frame(self)
        password_frame.place(x=170, y=150)
        password_label = tk.Label(password_frame, text='password :')
        password_label.pack(side=tk.LEFT, padx=10)
        password_entry = tk.Entry(password_frame, show='*')
        password_entry.pack(side=tk.LEFT, padx=10)
        back_button = tk.Button(self, text='뒤로가기', command=lambda: controller.show_frame(MainFrame))
        back_button.place(width=100, height=40, x=150, y=310)
        confirm_button = tk.Button(self, text='확인', command=show_message)
        confirm_button.place(width=100, height=40, x=250, y=310)
        temp = tk.Button(self, text='flag', command=lambda: controller.show_frame(GradesFrame))
        temp.place(width=100, height=40, x=350, y=310)


class GradesFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        grades_data = [
            ("김철수", "일반미적분학및연습", "A"),
            ("이영희", "시스템보안", "B+"),
            ("박민준", "인공지능개론", "C"),
            ("최서윤", "자료구조론", "B"),
            ("정하준", "Global English1", "A+")
        ]
        tree = ttk.Treeview(self, columns=('Name', 'Subject', 'Grade'), show='headings')
        tree.heading('Name', text='담당교수')
        tree.heading('Subject', text='과목')
        tree.heading('Grade', text='성적')
        for grade in grades_data:
            tree.insert('', tk.END, values=grade)
        tree.pack(expand=True, fill='both')

        back_button = tk.Button(self, text='뒤로가기', command=lambda: controller.show_frame(LoginFrame))
        back_button.place(width=100, height=40, x=150, y=310)

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('고려대학교 성적조회 프로그램')
        self.geometry('600x400')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MainFrame, LoginFrame, GradesFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
