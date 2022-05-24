import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand=True)
        container.grid_rowconfigure(0, weight =1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in(StartPage, MenuPage, NewPage, CoursePage, SmallPage):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name]=frame

            frame.grid(row = 0, column = 0, sticky="nsew")

            self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="light green") #color generator for hex
        self.controller = controller
        self.controller.title("TRAINING CENTER")
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text = "TRAINING CENTER", font = ('Castellar', 50, 'bold'), fg= "blue", bg="light green")
        big_lable.pack(pady=30)

        login_lable = tk.Label(self, text = "ENTER YOUR LOGIN", font = ('Arial', 15, 'bold'), fg= "blue", bg="light green")
        login_lable.pack(pady=30)

        my_login = tk.StringVar()
        login_entry = tk.Entry(self, textvariable=my_login, font=('Arial', 15, 'bold'), fg="blue", bg="light green")
        login_entry.pack(pady=30)

        password_lable = tk.Label(self, text="ENTER YOUR PASSWORD", font=('Arial', 15, 'bold'), fg= "blue", bg="light green")
        password_lable.pack()

        my_password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=my_password, font =('Arial', 15, 'bold'), fg= "blue", bg="light green")
        password_entry.pack(pady=30)

        def check_password():
            if my_password.get()=="1141" and my_login.get()=="malika" or my_password.get()=="5555" and my_login.get()=="ticher":
                controller.show_frame('MenuPage')

                #right_lable = tk.Label(self, text="right answer")
                #right_lable.pack()

            else:
                right_lable['text']="Wrong Password or login"

        password_button = tk.Button(self, text="Check you password and login", command=check_password, font=('Arial', 15, 'bold'), fg= "blue", bg="light green", width='25')
        password_button.pack()
        right_lable = tk.Label(self, font=('Arial', 15, 'bold'), fg= "blue", bg="light green")
        right_lable.pack(pady=30)

        def page_registration():
            controller.show_frame('NewPage')
        registration_button = tk.Button(self, text="Create an account", command=page_registration, font=('Arial', 20, 'bold'), fg="blue", bg="light green")
        registration_button.pack(pady=30)

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#883198")
        self.controller = controller
        big_lable = tk.Label(self, text="WELCOME TO TRAINING CENTER", font=('Bernard MT Condensed', 50, 'bold'), fg= "pink", bg="#883198")
        big_lable.pack(pady=30)

        search_lable = tk.Label(self, text="About the training center", font=('Arial', 15, 'bold'), fg= "pink", bg="#883198")
        search_lable.pack()
        search_lable.place(x=1050, y=150)

        my_search = tk.StringVar()
        search_entry = tk.Entry(self, textvariable=my_search, font=('Arial', 15, 'bold'), fg= "pink", bg="#883198")
        search_entry.pack(pady=20)
        search_entry.place(x=800, y=150)

        info_lable = tk.Label(self, text="About the training center", font=('Arial', 15, 'bold'), fg= "pink", bg="#883198")
        info_lable.pack(pady=20)
        info_lable.place(x=170, y=200)

        def return_page():
            controller.show_frame('CoursePage')
        courses_button = tk.Button(self, text="About courses", command=return_page, font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        courses_button.pack(pady=30)
        courses_button.place(x=430, y=200)

        pro_lable = tk.Label(self, text="Become a pro", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        pro_lable.pack(pady=20)
        pro_lable.place(x=600, y=200)

        personal_lable = tk.Label(self, text="Personal account", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        personal_lable.pack(pady=20)
        personal_lable.place(x=760, y=200)

        reviews_lable = tk.Label(self, text="REVIEWS", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        reviews_lable.pack(pady=20)
        reviews_lable.place(x=970, y=200)

        help_lable = tk.Label(self, text="HELP", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        help_lable.pack(pady=20)
        help_lable.place(x=1100, y=200)

        group_lable = tk.Label(self, text="Groups", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        group_lable.pack(pady=20)
        group_lable.place(x=300, y=300)

        lectures_lable = tk.Label(self, text="Lectures", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        lectures_lable.pack(pady=20)
        lectures_lable.place(x=300, y=350)

        seminars_lable = tk.Label(self, text="Seminars", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        seminars_lable.pack(pady=20)
        seminars_lable.place(x=300, y=400)

        video_lable = tk.Label(self, text="Watch video tutorials", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        video_lable.pack(pady=20)
        video_lable.place(x=300, y=450)

        material_lable = tk.Label(self, text="Educational materials", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        material_lable.pack(pady=20)
        material_lable.place(x=600, y=300)

        ratings_lable = tk.Label(self, text="Ratings", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        ratings_lable.pack(pady=20)
        ratings_lable.place(x=600, y=350)

        missed_lable = tk.Label(self, text="Missed classes", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        missed_lable.pack(pady=20)
        missed_lable.place(x=600, y=400)

        payment_lable = tk.Label(self, text="View payment", font=('Arial', 15, 'bold'), fg="pink", bg="#883198")
        payment_lable.pack(pady=20)
        payment_lable.place(x=300, y=500)

        def return_page():
            controller.show_frame('StartPage')
        return_button = tk.Button(self, text="return to main page", command=return_page, font=('Bernard MT Condensed', 15, 'bold'), fg= "pink", bg="#883198")
        return_button.pack(pady=30)
        return_button.place(x=600, y=600)

class NewPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#Ff9a00")
        self.controller = controller

        big_lable = tk.Label(self, text="CREATE AN ACCOUNT", font=('Perpetua Titling MT', 50, 'bold'), fg= "black", bg="#Ff9a00")
        big_lable.pack(pady=30)

        name_lable = tk.Label(self, text="ENTER YOUR NAME", font=('Arial', 15, 'bold'), fg="black", bg="orange")
        name_lable.pack(pady=20, side='left')
        name_lable.place(x=400, y=170)

        my_name = tk.StringVar()
        name_entry = tk.Entry(self, textvariable=my_name, font=('Arial', 15, 'bold'), fg="black", bg="orange")
        name_entry.pack(pady=20, side='left')
        name_entry.place(x=400, y=210)

        surname_lable = tk.Label(self, text="ENTER YOUR SURNAME", font=('Arial', 15, 'bold'), fg="black", bg="orange")
        surname_lable.pack(pady=20, side='left')
        surname_lable.place(x=400, y=250)

        my_surname = tk.StringVar()
        surname_entry = tk.Entry(self, textvariable=my_surname, font=('Arial', 15, 'bold'), fg="black", bg="orange")
        surname_entry.pack(pady=20, side='left')
        surname_entry.place(x=400, y=290)

        email_lable = tk.Label(self, text="ENTER YOUR EMAIL", font=('Arial', 15, 'bold'), fg="black", bg="orange")
        email_lable.pack(pady=30, side='right')
        email_lable.place(x=800, y=170)

        my_email = tk.StringVar()
        email_entry = tk.Entry(self, textvariable=my_email, font=('Arial', 15, 'bold'), fg="black", bg="orange")
        email_entry.pack(pady=30, side='right')
        email_entry.place(x=800, y=210)

        phone_lable = tk.Label(self, text="ENTER YOUR PHONE NUMBER", font=('Arial', 15, 'bold'), fg="black", bg="orange")
        phone_lable.pack(pady=30, side='right')
        phone_lable.place(x=800, y=250)

        my_phone = tk.StringVar()
        phone_entry = tk.Entry(self, textvariable=my_phone, font=('Arial', 15, 'bold'), fg="black", bg="orange")
        phone_entry.pack(pady=30, side='right')
        phone_entry.place(x=800, y=290)

        login_lable = tk.Label(self, text="THINK UP AND WRITE A NEW LOGIN", font=('Arial', 15, 'bold'), fg="black", bg="orange")
        login_lable.pack(pady=20, side='left')
        login_lable.place(x=400, y=340)

        my_login = tk.StringVar()
        login_entry = tk.Entry(self, textvariable=my_login, font=('Arial', 15, 'bold'), fg="black", bg="orange")
        login_entry.pack(pady=20, side='left')
        login_entry.place(x=400, y=380)

        password_lable = tk.Label(self, text="THINK UP AND WRITE A NEW PASSWORD", font=('Arial', 15, 'bold'), fg="black", bg="orange")
        password_lable.pack(pady=30, side='right')
        password_lable.place(x=800, y=340)

        my_password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=my_password, font=('Arial', 15, 'bold'), fg="black", bg="orange")
        password_entry.pack(pady=30, side='right')
        password_entry.place(x=800, y=380)

        def my_data():
            if my_login.get()=="" and my_password.get()=="":
                return_data_lable = tk.Label(self, text="Wrong password or login", font=('Arial', 15, 'bold'), fg="black", bg="orange")
                return_data_lable.pack()
                return_data_lable.place(x=600, y=600)
            else:
                return_data_button['text']="Your information has been received"

        return_data_button = tk.Button(self, text="Check you password and login", command=my_data, font=('Arial', 15, 'bold'), fg="black", bg="orange", width='25')
        return_data_button.pack()
        return_data_button.place(x=600, y=500)
        return_data_button = tk.Button(self, font=('Arial', 15, 'bold'), fg="black", bg="orange")
        return_data_button.pack(pady=30)
        return_data_button.place(x=600, y=440)

        def return_page():
            controller.show_frame('MenuPage')
        return_button = tk.Button(self, text="return to main page", command=return_page, font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="orange")
        return_button.pack(pady=30, side='top')
        return_button.place(x=600, y=550)

class CoursePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="DarkTurquoise")
        self.controller = controller

        big_lable = tk.Label(self, text="COURSES", font=('Perpetua Titling MT', 50, 'bold'), fg= "black", bg="DarkTurquoise")
        big_lable.pack(pady=30)

        teachers_lable = tk.Label(self, text="Choose the teacher you like", font=('Arial', 15, 'bold'), fg="black", bg="DarkTurquoise")
        teachers_lable.pack(pady=20, side='left')
        teachers_lable.place(x=200, y=150)

        teachers = tk.StringVar()
        label1_radiobutton = tk.Radiobutton(self, text="Mariya Sharipova", variable=teachers, value="Mariya Sharipova", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label1_radiobutton.place(anchor='w', x=200, y=200)
        label2_radiobutton = tk.Radiobutton(self, text="Aleksandr Kim", variable=teachers, value="Aleksandr Kim", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label2_radiobutton.place(anchor='w', x=200, y=250)
        label3_radiobutton = tk.Radiobutton(self, text="Yuliya Kim", variable=teachers, value="Yuliya Kim", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label3_radiobutton.place(anchor='w', x=200, y=300)
        label4_radiobutton = tk.Radiobutton(self, text="Viktor", variable=teachers, value="Viktor", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label4_radiobutton.place(anchor='w', x=200, y=350)

        selection_lable = tk.Label(self, textvariable=teachers, font=('Arial', 15, 'bold'), fg="black",  bg="DarkTurquoise", width='25')
        selection_lable.place(anchor='w', x=200, y=400)


        field_lable = tk.Label(self, text="Choose your field of study", font=('Arial', 15, 'bold'), fg="black",  bg="DarkTurquoise")
        field_lable.pack(pady=20, side='left')
        field_lable.place(x=500, y=150)

        fields = tk.StringVar()
        label1_radiobutton = tk.Radiobutton(self, text="Information technology", variable=fields, value="Information technology", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label1_radiobutton.place(anchor='w', x=500, y=200)
        label2_radiobutton = tk.Radiobutton(self, text="Basics of accounting", variable=fields, value="Basics of accounting", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label2_radiobutton.place(anchor='w', x=500, y=250)
        label3_radiobutton = tk.Radiobutton(self, text="1 C", variable=fields, value="1 C", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label3_radiobutton.place(anchor='w', x=500, y=300)
        label4_radiobutton = tk.Radiobutton(self, text="Basics of computer", variable=fields, value="Basics of computer", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label4_radiobutton.place(anchor='w', x=500, y=350)

        selection_lable = tk.Label(self, textvariable=fields, font=('Arial', 15, 'bold'), fg="black", bg="DarkTurquoise", width='25')
        selection_lable.place(anchor='w', x=500, y=400)

        language_lable = tk.Label(self, text="Select the reading language", font=('Arial', 15, 'bold'), fg="black", bg="DarkTurquoise")
        language_lable.pack(pady=20, side='left')
        language_lable.place(x=800, y=150)

        language = tk.StringVar()
        label1_radiobutton = tk.Radiobutton(self, text="Russian", variable=language, value="Russian", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label1_radiobutton.place(anchor='w', x=800, y=200)
        label2_radiobutton = tk.Radiobutton(self, text="Uzbek", variable=language, value="Uzbek", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label2_radiobutton.place(anchor='w', x=800, y=250)
        label3_radiobutton = tk.Radiobutton(self, text="English", variable=language, value="English", font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        label3_radiobutton.place(anchor='w', x=800, y=300)

        selection_lable = tk.Label(self, textvariable=language, font=('Arial', 15, 'bold'), fg="black", bg="DarkTurquoise", width='25')
        selection_lable.place(anchor='w', x=800, y=400)

        def return_page():
            controller.show_frame('MenuPage')
        return_button = tk.Button(self, text="return to main page", command=return_page, font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        return_button.pack(pady=30, side='top')
        return_button.place(x=600, y=600)

        def save_page():
            controller.show_frame('SmallPage')
        return_button = tk.Button(self, text="SAVE", command=save_page, font=('Bernard MT Condensed', 15, 'bold'), fg="black", bg="DarkTurquoise")
        return_button.pack(pady=30, side='top')
        return_button.place(x=600, y=500)

class SmallPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#0307fc")
        self.controller = controller

        big_lable = tk.Label(self, text="Congratulations", font=('Times New Roman', 50, 'bold'), fg="white", bg="#0307fc")
        big_lable.pack(pady=30)

        big_lable1 = tk.Label(self, text="your application", font=('Times New Roman', 50, 'bold'), fg="white", bg="#0307fc")
        big_lable1.pack(pady=30)

        big_lable2 = tk.Label(self, text="has been accepted", font=('Times New Roman', 50, 'bold'), fg="white", bg="#0307fc")
        big_lable2.pack(pady=30)

        big_lable3 = tk.Label(self, text="Don't forget to pay", font=('Times New Roman', 50, 'bold'), fg="white", bg="#0307fc")
        big_lable3.pack(pady=30)

        def return_page():
            controller.show_frame('MenuPage')
        return_button = tk.Button(self, text="return to main page", command=return_page, font=('Times New Roman', 15, 'bold'), fg="white", bg="#0307fc")
        return_button.pack(pady=30, side='top')
        return_button.place(x=600, y=600)

if __name__ =="__main__":
    app = SampleApp()
    app.mainloop()

