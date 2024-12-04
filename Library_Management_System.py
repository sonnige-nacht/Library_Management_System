import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import re
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror, showwarning, showinfo
from PIL import ImageTk, Image
import csv
from datetime import datetime
import pandas as pd
import csv

# related to showinfo...
options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

regex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"  

def check_username(email):   

    if(re.search(regex,email)):   
        return True   
    else:   
        return False
    

class SeaofBTCapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Sign_up_as_Student, Sign_up_as_Admin, Log_in, after_login_admin, after_login_student,
                add_and_remove, add_books, remove_books,request_books, reserve_book, accept_or_decline_requests,
                the_list_of_books_student, List_of_Requested_Books, List_of_Taken_Books, change_passwords_admin,
                change_passwords_yours_admin, change_passwords_of_students, Changed_By_Whom, change_passwords_yours_student,
                set_fine_amount, Pay_The_Fine, page_status_of_books, page_See_The_List_Of_Books,page_Find_The_Book_By_Searching_Name,
                page_status_of_books_student, return_books, profile_student, profile_admin,fine_pageee, Set_Fine_Amount):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to Library Managment System !", fg="black", font=("Times",22))
        label.pack(pady=15,padx=10)

        button = tk.Button(self, text="Sign up as Student", fg="black", font=("Times",15),
                            command=lambda: controller.show_frame(Sign_up_as_Student),width = 30)
        button.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Sign up as  Admin", fg="black", font=("Times",15),
                            command=lambda: controller.show_frame(Sign_up_as_Admin),width = 30)
        button2.pack( pady=10,padx=10)

        button3 = tk.Button(self, text="Log in", fg="black", font=("Times",15),
                            command=lambda: controller.show_frame(Log_in),width = 30)
        button3.pack(pady=10,padx=10)

        button4 = tk.Button(self, text="Exit", fg="black", font=("Times",15),
                            command = self.quit,width = 30)
        button4.pack(pady=10,padx=10)



class Sign_up_as_Student(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        email = tk.StringVar()
        
        password = tk.StringVar()
        label = tk.Label(self, text="Sign up as Student", fg="black", font=("Times",22))
        label.pack(pady=20,padx=20)

        tk.Label(self, text="E-mail", fg="black", font=("Times",15)).pack(pady=10,padx=10)
        e_1 = Entry(self, textvariable= email, font=("Times",15),justify='center')
        e_1.pack(pady=10,padx=10)
        
        tk.Label(self, text="Password", fg="black", font=("Times",15)).pack(pady=10,padx=10)
        e_2 = Entry(self, textvariable= password, font=("Times",15), show="•",justify='center')
        e_2.pack(pady=10,padx=10)
        
        def clear_text_1():
            e_1.delete(0, END)
        def clear_text_2():
            e_2.delete(0, END)

        def append_new_student():
            list_1 = [email.get(), "student", password.get(), "NO INFOS", "NO INFOS", "NO INFOS", "NO INFOS", "NO INFOS"]
            with open("one.csv", "a", newline= "") as f:
                writer = csv.writer(f)
                writer.writerow(list_1)
                f.close()
                
        def same_email_or_not():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == email.get():
                        counter +=1
            if counter!= 0:
                return True
            else:
                return False
            
        frame_login  =  Frame(self)
        frame_login.pack(padx=10,  pady=10)
        
        sign_bar  =  Frame(frame_login)
        sign_bar.pack(side='left',  padx=5,  pady=5)

        clear_bar  =  Frame(frame_login)
        clear_bar.pack(side='right', padx=5,  pady=5)

        button1 = tk.Button(sign_bar, text="Sign Up", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: 
                                            showerror(
                                            title='Error',
                                            message='Please Enter a Valid E-mail Address or Use Another E-mail')
                                            if check_username(email.get()) == False or same_email_or_not() == True
                                            else
                                            [controller.show_frame(StartPage),append_new_student(),clear_text_1(),clear_text_2()])
        button1.pack(ipadx=10)

        button2 = tk.Button(clear_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: [clear_text_1(),clear_text_2()])
        button2.pack(ipadx=10)

        button3 = tk.Button(self, text="Main Menu", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: [controller.show_frame(StartPage),clear_text_1(),clear_text_2()])
        button3.pack(ipadx=10)



class Sign_up_as_Admin(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        email = tk.StringVar()
        
        password = tk.StringVar()
        label = tk.Label(self, text="Sign up as Admin", fg="black", font=("Times",22))
        label.pack(pady=20,padx=20)

        tk.Label(self, text="E-mail", fg="black", font=("Times",15)).pack(pady=10,padx=10)
        e_1 = Entry(self, textvariable= email, font=("Times",15), justify='center')
        e_1.pack(pady=10,padx=10)
        
        tk.Label(self, text="Password", fg="black", font=("Times",15)).pack(pady=10,padx=10)
        e_2 = Entry(self, textvariable= password, font=("Times",15), show="•", justify='center')
        e_2.pack(pady=10,padx=10)
        
        def clear_text_1():
            e_1.delete(0, END)
        def clear_text_2():
            e_2.delete(0, END)

        def same_email_or_not():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == email.get():
                        counter +=1
            if counter!= 0:
                return True
            else:
                return False
            
        def append_new_admin():
            list_1 = [email.get(), "admin", password.get(), "NO INFOS", "NO INFOS", "NO INFOS", "NO INFOS", "NO INFOS"]
            with open("one.csv", "a", newline= "") as f:
                writer = csv.writer(f)
                writer.writerow(list_1)
                f.close()
            
        frame_login  =  Frame(self)
        frame_login.pack(padx=10,  pady=10)
        
        sign_bar  =  Frame(frame_login)
        sign_bar.pack(side='left',  padx=5,  pady=5)

        clear_bar  =  Frame(frame_login)
        clear_bar.pack(side='right', padx=5,  pady=5)

        button1 = tk.Button(sign_bar, text="Sign Up", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: 
                                            showerror(
                                            title='Invalid E-mail',
                                            message='Please Enter a Valid E-mail Address')
                                            if check_username(email.get()) == False or same_email_or_not() == True
                                            else [controller.show_frame(StartPage),append_new_admin(),clear_text_1(),clear_text_2()])
        button1.pack(ipadx=10)

        button2 = tk.Button(clear_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: [clear_text_1(),clear_text_2()])
        button2.pack(ipadx=10)

        button3 = tk.Button(self, text="Main Menu", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: [controller.show_frame(StartPage),clear_text_1(),clear_text_2()])
        button3.pack(ipadx=10)

class Log_in(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        email = tk.StringVar()
        password = tk.StringVar()

        label = tk.Label(self, text="Log in", fg="black", font=("Times",22))
        label.pack(pady=20,padx=20)
        
        frame_radio  =  Frame(self)
        frame_radio.pack(padx=10,  pady=10)
        admin_bar  =  Frame(frame_radio)
        admin_bar.pack(side='left',  padx=5,  pady=5)

        student_bar  =  Frame(frame_radio)
        student_bar.pack(side='right', padx=5,  pady=5)

        radio = StringVar()
        tk.Radiobutton(admin_bar, text = "Admin",font=("Times",15), variable = radio, value = "admin").pack(padx=10)
        tk.Radiobutton(student_bar, text = "Student",font=("Times",15), variable = radio, value = "student").pack(padx=10)
        
        tk.Label(self, text="E-mail", fg="black", font=("Times",15)).pack(pady=10,padx=10)
        e_1 = Entry(self, textvariable= email, font=("Times",15), justify='center')
        e_1.pack(pady=10,padx=10)
        
        tk.Label(self, text="Password", fg="black", font=("Times",15)).pack(pady=10,padx=10)
        e_2 = Entry(self, textvariable= password, font=("Times",15), show="•", justify='center')
        e_2.pack(pady=10,padx=10)
        
        def clear_text_1():
            e_1.delete(0, END)
        def clear_text_2():
            e_2.delete(0, END)
        def insert_data_to_login():
            email_label["text"] = email.get()
        def insert_data_to_login_student():
            email_label_student["text"] = email.get()
        frame_login  =  Frame(self)
        frame_login.pack(padx=10,  pady=10)
        def available_or_not():
            counter = 0
            if radio.get() == "admin":
                    with open("one.csv", 'r') as file:
                        csvreader = csv.reader(file)
                        for row in csvreader:
                            if row[1] == "admin":
                                if row[0] == email.get():
                                    if row[2] == password.get():
                                        counter +=1

                    if counter == 0:
                            showerror(
                            title='Something Went Wrong',
                            message='Incorrect E-mail address or password')
                    else:
                        counter = 0
                        df = pd.read_csv("one.csv", index_col='username_email') 
                        df.loc[email.get() , "who_is_connected"] = "CONNECTED"
                        df.to_csv("one.csv")
                        insert_data_to_login()
                        clear_text_1()
                        clear_text_2()
                        controller.show_frame(after_login_admin)
                        notification_admin()
                        
            else:
                    with open("one.csv", 'r') as file:
                        csvreader = csv.reader(file)
                        for row in csvreader:
                            if row[1] == "student":
                                if row[0] == email.get():
                                    if row[2] == password.get():
                                        counter += 1 
                                        
                        if counter == 0:
                            showerror(
                            title='Something Went Wrong',
                            message='Incorrect E-mail address or password')
                        else:
                            counter = 0
                            df = pd.read_csv("one.csv", index_col='username_email') 
                            df.loc[email.get() , "who_is_connected"] = "CONNECTED"
                            df.to_csv("one.csv")
                            insert_data_to_login_student()
                            clear_text_1()
                            clear_text_2()
                            controller.show_frame(after_login_student)
                            notification_student()
                            
        sign_bar  =  Frame(frame_login)
        sign_bar.pack(side='left',  padx=5,  pady=5)

        clear_bar  =  Frame(frame_login)
        clear_bar.pack(side='right', padx=5,  pady=5)

        button1 = tk.Button(sign_bar, text="Log in", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: available_or_not())
        button1.pack(ipadx=10)

        button2 = tk.Button(clear_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: [clear_text_1(),clear_text_2()])
        button2.pack(ipadx=10)

        button3 = tk.Button(self, text="Main Menu", fg="white",bg = "blue", font=("Times",15),width = 6,
                            command=lambda: [controller.show_frame(StartPage),clear_text_1(),clear_text_2()])
        button3.pack(ipadx=10)
        



class after_login_admin(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def log_out():
            
            df = pd.read_csv("one.csv", index_col='username_email') 
            df.loc[get_email(), "who_is_connected"] = "NO INFOS"
            df.to_csv("one.csv")

            
        def get_email():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [4] == "CONNECTED":
                        email = row[0]
                        email_var = StringVar(self,email)
                        counter += 1
                        return email_var.get()

            if counter == 0:
                email_var = StringVar(self,"Nothing")
                return email_var.get()

        def insert_data_to_admin():
            useremail_label1["text"] = get_email()

        def inset_into_profile():
            useremail_label
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [0] == get_email():
                        firstname= row[5]
                        familyname= row[6]
                        phonenumber = row[7]
                        Firstname_entery_label1.insert(0, firstname)
                        lastname_entery_label1.insert(0, familyname)
                        phonenumber_entery_label1.insert(0, phonenumber)

        global notification_admin
        def notification_admin():
            list_of_names = []
            i = 1
            first_time = True
            first_time1 = True
            with open("Books.csv", "r") as k:
                reader = csv.reader(k)
                for row1 in reader:
                    if first_time == True:
                        first_time = False
                    elif row1[7] == "Available" and row1[10] == "RESERVED":
                                stringg = " has requested a Book"
                                name1 = row1[4] 
                                name1 += stringg
                                list_of_names.append(name1)
                                i += 1
                                stringg = ""
                                name1 = ""

            with open("Books.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if first_time1 == True:
                        first_time1 = False
                    elif row[6] != "NO INFOS" and row[4] != "NO INFOS":
                        if row[9] != "CONFIRMED":
                            date = datetime.strptime(row[6], "%Y-%m-%d")
                            today = datetime.now()
                
                            if date < today:
                                string = " has to pay the Fine"
                                name = row[4] 
                                name += string
                                list_of_names.append(name)
                                i += 1
                                string = ""
                                name = ""
                            else:
                                continue
                if i == 1:
                    showinfo(title="Notification",
                        message="Nothing to Show")
                else:
                    stringgg = "\n".join(list_of_names[i] for i in range(len(list_of_names)))
                    showinfo(title="Notification",
                        message="Here is the latest News:\n\n"+ stringgg)
                    stringg = ""

        frame_upper  =  Frame(self, bg = "Grey")
        frame_upper.pack(padx=25,  pady=25)

        user_type_bar  =  Frame(frame_upper)
        user_type_bar.pack(side = "left", padx=5,  pady=5)

        email_bar  =  Frame(frame_upper)
        email_bar.pack(side = "left",padx=5,  pady=5)
        
        date_bar = Frame(frame_upper)
        date_bar.pack(side = "left", padx=5,  pady=5)

        notification_bar = Frame(frame_upper)
        notification_bar.pack(side = "left", padx=5,  pady=5)

        type_label = Label(user_type_bar, text= "Admin", fg="black", font=("Times",15),width = 18)
        type_label.pack(pady=10,padx=10)
        
        global email_label
        email_label = Label(email_bar,  text= get_email(), fg="black", font=("Times",15), width = 18)
        email_label.pack(pady=10,padx=10)

        time = Label(date_bar, text = datetime.today().strftime('%Y-%m-%d'), fg="black", font=("Times",15), width = 18)
        time.pack(pady=10,padx=10)

        notification = Button(notification_bar, text= "🔔", font=("Times",15),fg="black",bg = "yellow",width = 3, height= 1,
                            command= lambda: notification_admin())
        notification.pack()

        frame_lower_1=  Frame(self, bg = "Grey")
        frame_lower_1.pack(padx=10,  pady=10)

        add_and_remove_bar  =  Frame(frame_lower_1)
        add_and_remove_bar.pack(side = "left", padx=5,  pady=5)

        Requests_bar  =  Frame(frame_lower_1)
        Requests_bar.pack(side = "left",padx=5,  pady=5)

        Change_Passwords_bar = Frame(frame_lower_1)
        Change_Passwords_bar.pack(side = "left", padx=5,  pady=5)


        button1 = tk.Button(add_and_remove_bar, text="Add & Remove Books", fg="white",bg = "blue", font=("Times",15),
                            width = 19, command= lambda: controller.show_frame(add_and_remove))
        button1.pack(ipadx=10)

        button2 = tk.Button(Requests_bar, text="Requests", fg="white",bg = "blue", font=("Times",15),
                            width = 19, command= lambda: [controller.show_frame(accept_or_decline_requests),list_of_requests()])
        button2.pack(ipadx=10)

        button3 = tk.Button(Change_Passwords_bar, text="Change Passwords", fg="white",bg = "blue", font=("Times",15),
                            command= lambda: controller.show_frame(change_passwords_admin),width = 19)
        button3.pack(ipadx=10)     

        frame_lower_2=  Frame(self, bg = "Grey")
        frame_lower_2.pack(padx=10,  pady=10)

        add_and_remove_bar  =  Frame(frame_lower_2)
        add_and_remove_bar.pack(side = "left", padx=5,  pady=5)

        Requests_bar  =  Frame(frame_lower_2)
        Requests_bar.pack(side = "left",padx=5,  pady=5)

        Change_Passwords_bar = Frame(frame_lower_2)
        Change_Passwords_bar.pack(side = "left", padx=5,  pady=5)
        
        button4 = tk.Button(add_and_remove_bar, text="Fine", fg="white",bg = "blue", font=("Times",15),
                            width = 19, command= lambda: [controller.show_frame(fine_pageee)])
        button4.pack(ipadx=10)

        button5 = tk.Button(Requests_bar, text="Status Of Books", fg="white",bg = "blue", font=("Times",15),
                            command= lambda: controller.show_frame(page_status_of_books),width = 19)
        button5.pack(ipadx=10)

        button6 = tk.Button(Change_Passwords_bar, text="Profile", fg="white",bg = "blue", font=("Times",15),
                            command= lambda: [controller.show_frame(profile_admin),inset_into_profile(), insert_data_to_admin()],width = 19)
        button6.pack(ipadx=10) 

        frame_lower_3=  Frame(self, bg = "Grey")
        frame_lower_3.pack(padx=10,  pady=10)
        
        Exit_bar = Frame(frame_lower_3)
        Exit_bar.pack(side = "left", padx=5,  pady=5)
        
        button7 = tk.Button(Exit_bar, text="Log Out", fg="white",bg = "red", font=("Times",15),
                            width = 19, command=lambda: [controller.show_frame(StartPage),log_out()])
        button7.pack(ipadx=10) 

class add_and_remove(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        label_add_and_remove = tk.Label(self, text="Add & Remove Books", fg="black", font=("Times",22))
        label_add_and_remove.pack(pady=20,padx=20)

        button = tk.Button(self, text="Add Books", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(add_books),width = 20)
        button.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Remove Books", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(remove_books),width = 20)
        button2.pack(pady=10,padx=10)

        button3 = tk.Button(self, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(after_login_admin),width = 20)
        button3.pack(pady=10,padx=10)
        
class add_books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        titel = tk.StringVar()
        author = tk.StringVar()
        publisher = tk.StringVar()
        genre = tk.StringVar()

        label_add_books = tk.Label(self, text="Add Book", fg="black", font=("Times",22))
        label_add_books.pack(pady=20,padx=20)

        frame_add_books_upper  =  Frame(self, bg = "Grey")
        frame_add_books_upper.pack(padx=10,  pady=10)
        
        titel_bar  =  Frame(frame_add_books_upper)
        titel_bar.pack(side = "left", padx=5,  pady=5)
        
        entery_titel_bar = Frame(frame_add_books_upper)
        entery_titel_bar.pack(side = "left", padx=5,  pady=5)
        
        titel_label = Label(titel_bar, text= "Titel", fg="black", font=("Times",15),width = 18)
        titel_label.pack(pady=10,padx=10)
        
        entery_titel = Entry(entery_titel_bar, textvariable= titel, font=("Times",15),justify='center')
        entery_titel.pack(pady=10,padx=10)

        frame_add_books_lower  =  Frame(self, bg = "Grey")
        frame_add_books_lower.pack(padx=10,  pady=10)

        author_bar  =  Frame(frame_add_books_lower)
        author_bar.pack(side = "left", padx=5,  pady=5)

        entery_author_bar = Frame(frame_add_books_lower)
        entery_author_bar.pack(side = "left", padx=5,  pady=5)

        author_label = Label(author_bar, text= "Author", fg="black", font=("Times",15),width = 18)
        author_label.pack(pady=10,padx=10)
        
        entery_author = Entry(entery_author_bar, textvariable= author, font=("Times",15),justify='center')
        entery_author.pack(pady=10,padx=10)


        frame_add_books_lower_2  =  Frame(self, bg = "Grey")
        frame_add_books_lower_2.pack(padx=10,  pady=10)
        
        publisher_bar  =  Frame(frame_add_books_lower_2)
        publisher_bar.pack(side = "left", padx=5,  pady=5)
        
        entery_publisher_bar = Frame(frame_add_books_lower_2)
        entery_publisher_bar.pack(side = "left", padx=5,  pady=5)
        
        publisher_label = Label(publisher_bar, text= "Publisher", fg="black", font=("Times",15),width = 18)
        publisher_label.pack(pady=10,padx=10)
        
        entery_publisher = Entry(entery_publisher_bar, textvariable= publisher, font=("Times",15),justify='center')
        entery_publisher.pack(pady=10,padx=10)
        
        frame_add_books_lower_3  =  Frame(self, bg = "Grey")
        frame_add_books_lower_3.pack(padx=10,  pady=10)
        
        genre_bar  =  Frame(frame_add_books_lower_3)
        genre_bar.pack(side = "left", padx=5,  pady=5)
        
        entery_genre_bar = Frame(frame_add_books_lower_3)
        entery_genre_bar.pack(side = "left", padx=5,  pady=5)
        
        genre_label = Label(genre_bar, text= "Genre", fg="black", font=("Times",15),width = 18)
        genre_label.pack(pady=10,padx=10)
        
        entery_genre = Entry(entery_genre_bar, textvariable= genre, font=("Times",15),justify='center')
        entery_genre.pack(pady=10,padx=10)
        
        #save data in Books.csv
        def save_in_books():
            list_of_data = [titel.get(),author.get(),genre.get(),publisher.get()
                            ,"NO INFOS","NO INFOS","NO INFOS","Available","NO INFOS","NO INFOS","NO INFOS"]
            with open("Books.csv", "a", newline= "") as f:
                    writer = csv.writer(f)
                    writer.writerow(list_of_data)
                    f.close()
        #buttons
        def clear_entery_titel_1():
            entery_titel.delete(0, END)
            
        clear_b1_bar  =  Frame(frame_add_books_upper)
        clear_b1_bar.pack(side = "left", padx=5,  pady=5)
        clear_b1 = tk.Button(clear_b1_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_1())
        clear_b1.pack()
        
        def clear_entery_titel_2():
            entery_author.delete(0, END)
            
        clear_b2_bar  =  Frame(frame_add_books_lower)
        clear_b2_bar.pack(side = "left", padx=5,  pady=5)
        clear_b2 = tk.Button(clear_b2_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_2())
        clear_b2.pack()
        
        def clear_entery_titel_3():
            entery_publisher.delete(0, END)
            
        clear_b3_bar  =  Frame(frame_add_books_lower_2)
        clear_b3_bar.pack(side = "left", padx=5,  pady=5)
        clear_b3 = tk.Button(clear_b3_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_3())
        clear_b3.pack()
        
        def clear_entery_titel_4():
            entery_genre.delete(0, END)
            
        clear_b4_bar  =  Frame(frame_add_books_lower_3)
        clear_b4_bar.pack(side = "left", padx=5,  pady=5)
        clear_b4 = tk.Button(clear_b4_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_4())
        clear_b4.pack()
        # buttons under genre
        frame_add_books_lower_4  =  Frame(self)
        frame_add_books_lower_4.pack(padx=10,  pady=10)

        Save_bar  =  Frame(frame_add_books_lower_4)
        Save_bar.pack(side = "left", padx=5,  pady=5)

        save_button = tk.Button(Save_bar, text="Save", fg="white",bg = "green", font=("Times",15),
                            command=lambda: [showinfo(
                                                title='Saved Successfully',
                                                message='Your demand has been successfully saved!'),save_in_books(),
                                                clear_entery_titel_1(),clear_entery_titel_2(),
                                                clear_entery_titel_3(),clear_entery_titel_4()]
                                                if  titel.get() and author.get() and genre.get() and publisher.get() != None
                                                else 
                                                showwarning(
                                                title='Some sections are incomplete',
                                                message='Dear Admin, please complete all sections')
                                                , width= 15)
        save_button.pack()
        
        Previous_Page_bar  =  Frame(frame_add_books_lower_4)
        Previous_Page_bar.pack(side = "left", padx=5,  pady=5)

        Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(add_and_remove),clear_entery_titel_1(),clear_entery_titel_2(),
                                                clear_entery_titel_3(),clear_entery_titel_4()], width= 15)
        Previous_Page_button.pack()
        
        clear_all_bar  =  Frame(frame_add_books_lower_4)
        clear_all_bar.pack(side = "left", padx=5,  pady=5)

        clear_all_button = tk.Button(clear_all_bar, text="Clear All", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [clear_entery_titel_1(),clear_entery_titel_2(),
                                                clear_entery_titel_3(),clear_entery_titel_4()], width= 15)
        clear_all_button.pack()

class remove_books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        titel = tk.StringVar()
        
        label_add_books = tk.Label(self, text="Remove Book", fg="black", font=("Times",22))
        label_add_books.pack(pady=20,padx=20)

        frame_add_books_upper  =  Frame(self, bg = "Grey")
        frame_add_books_upper.pack(padx=20,  pady=20)
        
        titel_bar  =  Frame(frame_add_books_upper)
        titel_bar.pack(side = "left", padx=5,  pady=5)
        
        entery_titel_bar = Frame(frame_add_books_upper)
        entery_titel_bar.pack(side = "left", padx=5,  pady=5)

        titel_label = Label(titel_bar, text= "Titel", fg="black", font=("Times",15),width = 18)
        titel_label.pack(pady=10,padx=10)
        
        entery_titel = Entry(entery_titel_bar, textvariable= titel, font=("Times",15),justify='center')
        entery_titel.pack(pady=10,padx=10)

        def clear_entery_titel_1():
            entery_titel.delete(0, END)

        def delete_book():
            is_there = False

            with open("Books.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if titel.get() == row[0]:
                        is_there = True
                        break
                    else:
                        continue
        
            if is_there == True:        
                data = pd.read_csv("Books.csv", index_col = 0)
                data.drop([titel.get()],inplace=True)
                data.to_csv("Books.csv")
                showinfo(title='Deleted Successfully', message='Book has been successfully deleted!')
                clear_entery_titel_1()
            else:
                showwarning(title='There is no such Book in Library!', message='Dear Admin it seems, the given data are False')

        clear_b1_bar  =  Frame(frame_add_books_upper)
        clear_b1_bar.pack(side = "left", padx=5,  pady=5)
        clear_b1 = tk.Button(clear_b1_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_1())
        clear_b1.pack()

        frame_add_books_lower  =  Frame(self)
        frame_add_books_lower.pack(padx=15,  pady=15)

        delete_bar  =  Frame(frame_add_books_lower)
        delete_bar.pack(side = "left", padx=5,  pady=5)
        delete_button = tk.Button(delete_bar, text="Delete", fg="white",bg = "red", font=("Times",15),width= 15,
                                command= lambda: delete_book())
        delete_button.pack()
        
        Previous_Page_bar  =  Frame(frame_add_books_lower)
        Previous_Page_bar.pack(side = "left", padx=5,  pady=5)
        
        Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(add_and_remove),clear_entery_titel_1()], width= 15)
        Previous_Page_button.pack()




class accept_or_decline_requests(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_add_books = tk.Label(self, text="Requests", fg="black", font=("Times",22))
        label_add_books.pack(pady=20,padx=20)


        global list_of_requests
        def list_of_requests():
            frame_upper_1=  Frame(self)
            frame_upper_1.pack(padx=10,pady=10)
            
            tree_requests_bar = Frame(frame_upper_1)
            tree_requests_bar.pack(side = "left")
            scrollbar_2_bar = Frame(frame_upper_1)
            scrollbar_2_bar.pack(side = "left")

            scrollbar_numbers_2 = Scrollbar(scrollbar_2_bar)
            scrollbar_numbers_2.pack(ipady= 37,side = RIGHT,fill = Y)
            

            global tree_requests
            tree_requests = ttk.Treeview(tree_requests_bar, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
            tree_requests.column("# 1", anchor=CENTER, width= 140)
            tree_requests.heading("# 1", text="Number")
            tree_requests.column("# 2", anchor=CENTER, width= 140)
            tree_requests.heading("# 2", text="Book")
            tree_requests.column("# 3", anchor=CENTER, width= 140)
            tree_requests.heading("# 3", text="Student")
            tree_requests.column("# 4", anchor=CENTER, width= 140)
            tree_requests.heading("# 4", text="Date To Take")
            tree_requests.column("# 5", anchor=CENTER, width= 140)
            tree_requests.heading("# 5", text="Date To Give")


            with open("Books.csv", "r") as k:
                i = 1
                first_time = True
                reader = csv.reader(k)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    elif row[4] != "NO INFOS" and row[6] != "NO INFOS":
                        if row[8] != "ACCEPTED":
                            tree_requests.insert('', 'end', values=(i, row[0], row[4], row[5],row[6]))
                            i +=1

            tree_requests.pack()
            tree_requests.config(yscrollcommand = scrollbar_numbers_2.set)
            scrollbar_numbers_2.config(command = tree_requests.yview)
            

            def get_data_book():
                selected_item = tree_requests.focus()
                item_details = tree_requests.item(selected_item)
                details = item_details.get("values")
                return details[1]
            
            frame_lower_1=  Frame(self)
            frame_lower_1.pack(padx=10,pady=10)

            accept_bar = Frame(frame_lower_1)
            accept_bar.pack(side = "left", padx=15)
            decline_bar  =  Frame(frame_lower_1)
            decline_bar.pack(side = "left", padx=15)
            previous_page_bar  =  Frame(frame_lower_1)
            previous_page_bar.pack(side = "left", padx=15)


            accept_button = tk.Button(accept_bar, text="Accept", fg="white",bg = "green", font=("Times",15),width = 15,
                                    command = lambda: want_to_accept())
            accept_button.pack()

            decline_button = tk.Button(decline_bar, text="Decline", fg="white",bg = "red", font=("Times",15),width = 15,
                                    command = lambda: want_to_decline())
            decline_button.pack()

            previous_page_button = tk.Button(previous_page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15), width = 15,
                                            command= lambda:[controller.show_frame(after_login_admin),tree_requests.destroy(),
                                            frame_upper_1.destroy(),
                                            frame_lower_1.destroy()] )
            previous_page_button.pack()


            def want_to_accept():
                ef = pd.read_csv("Books.csv", index_col='name_of_book')  
                book = get_data_book()
                
                ef.loc[book , "accept_or_decline"] = "ACCEPTED"
                ef.to_csv("Books.csv")
                ef.loc[book , "book_available_or_not"] = "Unavailable"
                ef.to_csv("Books.csv")
                showinfo(title= "Accepted Request", message= "Dear Admin, you have accepted the request")
                tree_requests.destroy()
                frame_upper_1.destroy()
                frame_lower_1.destroy()
                controller.show_frame(accept_or_decline_requests)
                list_of_requests()

            def want_to_decline():
                ef = pd.read_csv("Books.csv", index_col='name_of_book')  
                book = get_data_book()

                ef.loc[book , "accept_or_decline"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "book_available_or_not"] = "Available"
                ef.to_csv("Books.csv")
                ef.loc[book , "students_name"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "date_to_take"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "date_to_give"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "fine"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "reserved_or_not"] = "NO INFOS"
                ef.to_csv("Books.csv")
                showinfo(title= "Accepted Request", message= "Dear Admin, you have declined the request")
                tree_requests.destroy()
                frame_upper_1.destroy()
                frame_lower_1.destroy()
                controller.show_frame(accept_or_decline_requests)
                list_of_requests()

class change_passwords_admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_change_passwords_admin = tk.Label(self, text="Change Passwords", fg="black", font=("Times",22))
        label_change_passwords_admin.pack(pady=20,padx=20)

        button = tk.Button(self, text="Change Yours", fg="white",bg = "blue", font=("Times",15),width = 20,
                        command= lambda: controller.show_frame(change_passwords_yours_admin))
        button.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Change Student's Password", fg="white",bg = "blue", font=("Times",15),width = 20,
                            command= lambda: [controller.show_frame(change_passwords_of_students), list_change_passwords_of_students()])
        button2.pack(pady=10,padx=10)

        button3 = tk.Button(self, text="Changed By Whom?", fg="white",bg = "blue", font=("Times",15),width = 20,
                            command= lambda: [controller.show_frame(Changed_By_Whom), list_Changed_By_Whom()])
        button3.pack(pady=10,padx=10)

        button4 = tk.Button(self, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(after_login_admin),width = 20)
        button4.pack(pady=10,padx=10)

class change_passwords_yours_admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        password = tk.StringVar()

        label_change_passwords_yours_admin = tk.Label(self, text="Change Passwords", fg="black", font=("Times",22))
        label_change_passwords_yours_admin.pack(pady=20,padx=20)

        frame_add_books_upper  =  Frame(self, bg = "Grey")
        frame_add_books_upper.pack(padx=20,  pady=20)
        
        titel_bar  =  Frame(frame_add_books_upper)
        titel_bar.pack(side = "left", padx=5,  pady=5)
        
        entery_titel_bar = Frame(frame_add_books_upper)
        entery_titel_bar.pack(side = "left", padx=5,  pady=5)

        titel_label = Label(titel_bar, text= "New Password", fg="black", font=("Times",15),width = 18)
        titel_label.pack(pady=10,padx=10)
        
        entery_titel = Entry(entery_titel_bar, textvariable= password, font=("Times",15),justify='center', show="•")
        entery_titel.pack(pady=10,padx=10)

        def clear_entery_titel_1():
            entery_titel.delete(0, END)

        def get_email():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [4] == "CONNECTED":
                        email = row[0]
                        email_var = StringVar(self,email)
                        counter += 1
                        return email_var.get()

        clear_b1_bar  =  Frame(frame_add_books_upper)
        clear_b1_bar.pack(side = "left", padx=5,  pady=5)
        clear_b1 = tk.Button(clear_b1_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_1())
        clear_b1.pack()

        frame_add_books_lower  =  Frame(self)
        frame_add_books_lower.pack(padx=15,  pady=15)

        def want_to_save():
            name = get_email()
            df = pd.read_csv("one.csv", index_col='username_email') 
            df.loc[name , "password"] = password.get()
            df.to_csv("one.csv")
            df.loc[name , "changed_password_by_whom"] = "admin"
            df.to_csv("one.csv")
            showinfo(title='Password Changed Successfully', message='Dear Admin, your new password is: '+ password.get())
            clear_entery_titel_1()

        save_bar  =  Frame(frame_add_books_lower)
        save_bar.pack(side = "left", padx=5,  pady=5)
        save_button = tk.Button(save_bar, text="Save", fg="white",bg = "green", font=("Times",15), width= 15,
                                command= lambda: want_to_save())
        save_button.pack()
        
        Previous_Page_bar  =  Frame(frame_add_books_lower)
        Previous_Page_bar.pack(side = "left", padx=5,  pady=5)
        
        Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(change_passwords_admin),clear_entery_titel_1()], width= 15)
        Previous_Page_button.pack()



class change_passwords_of_students(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_change_passwords_of_students = tk.Label(self, text="Change Student's Password", fg="black", font=("Times",22))
        label_change_passwords_of_students.pack(pady=20,padx=20)


        global list_change_passwords_of_students
        password = StringVar()
        def list_change_passwords_of_students():
            frame_upper_1=  Frame(self)
            frame_upper_1.pack(padx=10,pady=10)
            
            tree_change_passwords_student_bar = Frame(frame_upper_1)
            tree_change_passwords_student_bar.pack(side = "left")
            scrollbar_2_bar = Frame(frame_upper_1)
            scrollbar_2_bar.pack(side = "left")

            scrollbar_numbers_2 = Scrollbar(scrollbar_2_bar)
            scrollbar_numbers_2.pack(ipady= 37,side = RIGHT,fill = Y)
            

            global tree_change_passwords_student
            tree_change_passwords_student = ttk.Treeview(tree_change_passwords_student_bar, column=("c1", "c2", "c3"), show='headings', height=5)
            tree_change_passwords_student.column("# 1", anchor=CENTER, width= 170)
            tree_change_passwords_student.heading("# 1", text="Number")
            tree_change_passwords_student.column("# 2", anchor=CENTER, width= 170)
            tree_change_passwords_student.heading("# 2", text="Student")
            tree_change_passwords_student.column("# 3", anchor=CENTER, width= 170)
            tree_change_passwords_student.heading("# 3", text="Password")


            with open("one.csv", "r") as k:
                i = 1
                reader = csv.reader(k)
                for row in reader:
                    if row[1] == "student":
                            tree_change_passwords_student.insert('', 'end', values=(i, row[0], row[2]))
                            i +=1

            tree_change_passwords_student.pack()
            tree_change_passwords_student.config(yscrollcommand = scrollbar_numbers_2.set)
            scrollbar_numbers_2.config(command = tree_change_passwords_student.yview)
            

            def get_student_email():
                selected_item = tree_change_passwords_student.focus()
                item_details = tree_change_passwords_student.item(selected_item)
                details = item_details.get("values")
                return details[1]
            
            frame_add_books_upper  =  Frame(self, bg = "Grey")
            frame_add_books_upper.pack(padx=20,  pady=20)
        
            titel_bar  =  Frame(frame_add_books_upper)
            titel_bar.pack(side = "left", padx=5,  pady=5)
        
            entery_titel_bar = Frame(frame_add_books_upper)
            entery_titel_bar.pack(side = "left", padx=5,  pady=5)

            titel_label = Label(titel_bar, text= "New Password", fg="black", font=("Times",15),width = 18)
            titel_label.pack(pady=10,padx=10)
        
            entery_titel = Entry(entery_titel_bar, textvariable= password, font=("Times",15),justify='center', show="•")
            entery_titel.pack(pady=10,padx=10)

            clear_b1_bar  =  Frame(frame_add_books_upper)
            clear_b1_bar.pack(side = "left", padx=5,  pady=5)
            clear_b1 = tk.Button(clear_b1_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_1())
            clear_b1.pack()

            def clear_entery_titel_1():
                    entery_titel.delete(0, END)


            def want_to_changes():
                ef = pd.read_csv("one.csv", index_col='username_email')  
                student = get_student_email()
                
                ef.loc[student , "password"] = password.get()
                ef.to_csv("one.csv")
                ef.loc[student , "changed_password_by_whom"] = "admin"
                ef.to_csv("one.csv")
                showinfo(title='Password Changed Successfully', message=student + ' new password is: '+ password.get())
                clear_entery_titel_1()
                tree_change_passwords_student.destroy()
                frame_upper_1.destroy()
                frame_add_books_upper.destroy()
                frame_add_books_lower.destroy()
                controller.show_frame(change_passwords_of_students)
                list_change_passwords_of_students()

            frame_add_books_lower  =  Frame(self)
            frame_add_books_lower.pack(padx=15,  pady=15)
            save_bar  =  Frame(frame_add_books_lower)
            save_bar.pack(side = "left", padx=5,  pady=5)
            save_button = tk.Button(save_bar, text="Save", fg="white",bg = "green", font=("Times",15), width= 15,
                                command= lambda: want_to_changes())
            save_button.pack()
        
            Previous_Page_bar  =  Frame(frame_add_books_lower)
            Previous_Page_bar.pack(side = "left", padx=5,  pady=5)
        
            Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(change_passwords_admin),clear_entery_titel_1(),
                                            tree_change_passwords_student.destroy(),
                                            frame_upper_1.destroy(),
                                            frame_add_books_upper.destroy(),
                                            frame_add_books_lower.destroy()], width= 15)
            Previous_Page_button.pack()



class Changed_By_Whom(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_Changed_By_Whom = tk.Label(self, text="Changed By Whom?", fg="black", font=("Times",22))
        label_Changed_By_Whom.pack(pady=20,padx=20)


        global list_Changed_By_Whom
        def list_Changed_By_Whom():
            frame_upper_1=  Frame(self)
            frame_upper_1.pack(padx=10,pady=10)
            
            tree_Changed_By_Whom_bar = Frame(frame_upper_1)
            tree_Changed_By_Whom_bar.pack(side = "left")
            scrollbar_2_bar = Frame(frame_upper_1)
            scrollbar_2_bar.pack(side = "left")

            scrollbar_numbers_2 = Scrollbar(scrollbar_2_bar)
            scrollbar_numbers_2.pack(ipady= 37,side = RIGHT,fill = Y)
            

            global tree_Changed_By_Whom
            tree_Changed_By_Whom = ttk.Treeview(tree_Changed_By_Whom_bar, column=("c1", "c2", "c3", "c4"), show='headings', height=5)
            tree_Changed_By_Whom.column("# 1", anchor=CENTER, width= 170)
            tree_Changed_By_Whom.heading("# 1", text="Number")
            tree_Changed_By_Whom.column("# 2", anchor=CENTER, width= 170)
            tree_Changed_By_Whom.heading("# 2", text="E-mail")
            tree_Changed_By_Whom.column("# 3", anchor=CENTER, width= 170)
            tree_Changed_By_Whom.heading("# 3", text="User Type")
            tree_Changed_By_Whom.column("# 4", anchor=CENTER, width= 170)
            tree_Changed_By_Whom.heading("# 4", text="Changed By Admin/Student")

            with open("one.csv", "r") as k:
                i = 1
                first_time = True
                reader = csv.reader(k)
                for row in reader:
                    if first_time == True:
                            first_time = False
                            continue
                    else:
                        tree_Changed_By_Whom.insert('', 'end', values=(i, row[0],row[1], row[3]))
                        i +=1

            tree_Changed_By_Whom.pack()
            tree_Changed_By_Whom.config(yscrollcommand = scrollbar_numbers_2.set)
            scrollbar_numbers_2.config(command = tree_Changed_By_Whom.yview)
            
            frame_lower=  Frame(self)
            frame_lower.pack(padx=10,pady=10)
            Previous_Page_bar = Frame(frame_lower)
            Previous_Page_bar.pack(side = "left", padx=15)

            Prevoius_page_button = tk.Button(Previous_Page_bar, text="Prevoius Page", fg="white",bg = "blue", font=("Times",15),
                                            command= lambda: [controller.show_frame(change_passwords_admin), want_to_distroy()])
            Prevoius_page_button.pack()

            def want_to_distroy():
                tree_Changed_By_Whom_bar.destroy()
                frame_upper_1.destroy()
                frame_lower.destroy()

class fine_pageee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_add_and_remove = tk.Label(self, text="Fine", fg="black", font=("Times",22))
        label_add_and_remove.pack(pady=20,padx=20)

        button = tk.Button(self, text="Set Fine Amount For Students", fg="white",bg = "blue", font=("Times",15),
                            command=lambda:[controller.show_frame(set_fine_amount),list_ofset_fine_amount()],width = 25)
        button.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Set Fine Amount", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(Set_Fine_Amount)],width = 25)
        button2.pack(pady=10,padx=10)

        button3 = tk.Button(self, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(after_login_admin),width = 25)
        button3.pack(pady=10,padx=10)



class set_fine_amount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_add_books = tk.Label(self, text="Set Fine For Students", fg="black", font=("Times",22))
        label_add_books.pack(pady=20,padx=20)


        global list_ofset_fine_amount
        def list_ofset_fine_amount():
            frame_upper_1=  Frame(self)
            frame_upper_1.pack(padx=10,pady=10)
            
            treeset_fine_amount_bar = Frame(frame_upper_1)
            treeset_fine_amount_bar.pack(side = "left")
            scrollbar_2_bar = Frame(frame_upper_1)
            scrollbar_2_bar.pack(side = "left")

            scrollbar_numbers_2 = Scrollbar(scrollbar_2_bar)
            scrollbar_numbers_2.pack(ipady= 37,side = RIGHT,fill = Y)
            

            global treeset_fine_amount
            treeset_fine_amount = ttk.Treeview(treeset_fine_amount_bar, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
            treeset_fine_amount.column("# 1", anchor=CENTER, width= 140)
            treeset_fine_amount.heading("# 1", text="Number")
            treeset_fine_amount.column("# 2", anchor=CENTER, width= 140)
            treeset_fine_amount.heading("# 2", text="Book")
            treeset_fine_amount.column("# 3", anchor=CENTER, width= 140)
            treeset_fine_amount.heading("# 3", text="Student")
            treeset_fine_amount.column("# 4", anchor=CENTER, width= 140)
            treeset_fine_amount.heading("# 4", text="Date To Take")
            treeset_fine_amount.column("# 5", anchor=CENTER, width= 140)
            treeset_fine_amount.heading("# 5", text="Date To Give")


            with open("Books.csv", "r") as k:
                i = 1
                first_time = True
                reader = csv.reader(k)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    elif row[6] != "NO INFOS" and row[4] != "NO INFOS":
                        if row[9] != "CONFIRMED":
                            date = datetime.strptime(row[6], "%Y-%m-%d")
                            today = datetime.now()
                
                            if date < today:
                                treeset_fine_amount.insert('', 'end', values=(i, row[0], row[4], row[5],row[6]))
                                i += 1
                            else:
                                continue

            treeset_fine_amount.pack()
            treeset_fine_amount.config(yscrollcommand = scrollbar_numbers_2.set)
            scrollbar_numbers_2.config(command = treeset_fine_amount.yview)
            

            def get_data_book():
                selected_item = treeset_fine_amount.focus()
                item_details = treeset_fine_amount.item(selected_item)
                details = item_details.get("values")
                return details[1]
            
            frame_lower_1=  Frame(self)
            frame_lower_1.pack(padx=10,pady=10)

            accept_bar = Frame(frame_lower_1)
            accept_bar.pack(side = "left", padx=15)
            previous_page_bar  =  Frame(frame_lower_1)
            previous_page_bar.pack(side = "left", padx=15)


            accept_button = tk.Button(accept_bar, text="Set Fine", fg="white",bg = "green", font=("Times",15), width=10,
                                    command = lambda: want_to_accept())
            accept_button.pack()


            previous_page_button = tk.Button(previous_page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                                            width=10,
                                            command= lambda:[controller.show_frame(fine_pageee),treeset_fine_amount.destroy(),
                                            frame_upper_1.destroy(),
                                            frame_lower_1.destroy()] )
            previous_page_button.pack()


            def want_to_accept():
                ef = pd.read_csv("Books.csv", index_col='name_of_book')  
                book = get_data_book()
                
                ef.loc[book , "fine"] = "CONFIRMED"
                ef.to_csv("Books.csv")
                ef.loc[book , "book_available_or_not"] = "Available"
                ef.to_csv("Books.csv")
                ef.loc[book , "reserved_or_not"] = "NO INFOS"
                ef.to_csv("Books.csv")
                showinfo(title= "Set Fine", message= "Dear Admin, you have set the fine for: "+ ef.loc[book , "students_name"])
                treeset_fine_amount.destroy()
                frame_upper_1.destroy()
                frame_lower_1.destroy()
                controller.show_frame(set_fine_amount)
                list_ofset_fine_amount()



class Set_Fine_Amount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def clear_entery_titel_1():
            Amount_entery_label1.delete(0, END)

        def give_amount1():
            fine_amount.set(value=5)
        def give_amount2():
            fine_amount.set(value=10)
        def give_amount3():
            fine_amount.set(value=20)
        def give_amount4():
            fine_amount.set(value=30)

        global fine_amount
        fine_amount = IntVar()
        label_add_books = tk.Label(self, text="Set Fine Amount", fg="black", font=("Times",22))
        label_add_books.pack(pady=20,padx=20)
        
        frame_upper=  Frame(self, bg= "grey")
        frame_upper.pack(padx=10,pady=10)

        amount1_bar  =  Frame(frame_upper)
        amount1_bar.pack(side = "left", padx=5,  pady=5)

        amount2_bar  =  Frame(frame_upper)
        amount2_bar.pack(side = "left",padx=5,  pady=5)

        amount3_bar = Frame(frame_upper)
        amount3_bar.pack(side = "left",padx=5,  pady=5)

        amount4_bar = Frame(frame_upper)
        amount4_bar.pack(side = "left",padx=5,  pady=5)

        amount1_button = Button(amount1_bar, text= "5 £", font=("Times",15),fg="white",bg = "green", width=10,
                                command= lambda: give_amount1())
        amount1_button.pack()

        amount2_button = Button(amount2_bar, text= "10 £", font=("Times",15),fg="white",bg = "green", width=10,
                                command= lambda: give_amount2())
        amount2_button.pack()

        amount3_button = Button(amount3_bar, text= "20 £", font=("Times",15),fg="white",bg = "green", width=10,
                                command= lambda: give_amount3())
        amount3_button.pack()

        amount4_button = Button(amount4_bar, text= "30 £", font=("Times",15),fg="white",bg = "green", width=10,
                                command= lambda: give_amount4())
        amount4_button.pack()
        
        frame_upper_1=  Frame(self, bg = "grey")
        frame_upper_1.pack(padx=10,pady=10)

        Amount_bar  =  Frame(frame_upper_1)
        Amount_bar.pack(side = "left", padx=5,  pady=5)

        Amount_entery_bar = Frame(frame_upper_1)
        Amount_entery_bar.pack(side = "left", padx=5,  pady=5)

        clear_all_bar  =  Frame(frame_upper_1)
        clear_all_bar.pack(side = "left", padx=5,  pady=5)

        Amount_label = Label(Amount_bar, text= "Amount", fg="black", font=("Times",14),width = 19)
        Amount_label.pack(pady=10,padx=10)

        global Amount_entery_label1
        Amount_entery_label1 = Entry(Amount_entery_bar,textvariable= fine_amount, font=("Times",14),justify='center', width= 15)
        Amount_entery_label1.pack(pady=10,padx=10)

        clear_b1 = tk.Button(clear_all_bar, text="Clear", fg="white",bg = "blue", font=("Times",15), width=10,
                            command=lambda: clear_entery_titel_1())
        clear_b1.pack()

        frame_upper_2=  Frame(self)
        frame_upper_2.pack(padx=10,pady=10)

        PreviousPage_bar = Frame(frame_upper_2)
        PreviousPage_bar.pack(side = "left", padx=5,  pady=5)

        PrevoiusPage_b1 = tk.Button(PreviousPage_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15), width=15,
                            command=lambda: controller.show_frame(fine_pageee))
        PrevoiusPage_b1.pack()


class page_status_of_books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_page_status_of_books = tk.Label(self, text="Status Of Books", fg="black", font=("Times",22))
        label_page_status_of_books.pack(pady=20,padx=20)

        button = tk.Button(self, text="See The List Of Books", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(page_See_The_List_Of_Books), List_List_Of_Books()],width = 35)
        button.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Find The Book By Searching Titel", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(page_Find_The_Book_By_Searching_Name),width = 35)
        button2.pack(pady=10,padx=10)

        button4 = tk.Button(self, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(after_login_admin),width = 35)
        button4.pack(pady=10,padx=10)

class page_See_The_List_Of_Books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_List_of_Taken_Books = tk.Label(self, text="List Of Books", fg="black", font=("Times",22))
        label_List_of_Taken_Books.pack(pady=20,padx=20)

        global List_List_Of_Books
        def List_List_Of_Books():
            frame_upper=  Frame(self)
            frame_upper.pack(padx=10,pady=10)
            
            tree_List_Of_Books = Frame(frame_upper)
            tree_List_Of_Books.pack(side = "left")
            scrollbar_1_bar = Frame(frame_upper)
            scrollbar_1_bar.pack(side = "left")

            scrollbar_numbers_1 = Scrollbar(scrollbar_1_bar)
            scrollbar_numbers_1.pack(ipady= 37,side = RIGHT,fill = Y)


            global tree_List_Of_Bookss
            tree_List_Of_Bookss = ttk.Treeview(tree_List_Of_Books, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
            tree_List_Of_Bookss.column("# 1", anchor=CENTER, width= 140)
            tree_List_Of_Bookss.heading("# 1", text="Number")
            tree_List_Of_Bookss.column("# 2", anchor=CENTER, width= 140)
            tree_List_Of_Bookss.heading("# 2", text="Book")
            tree_List_Of_Bookss.column("# 3", anchor=CENTER, width= 140)
            tree_List_Of_Bookss.heading("# 3", text="Author")
            tree_List_Of_Bookss.column("# 4", anchor=CENTER, width= 140)
            tree_List_Of_Bookss.heading("# 4", text="Genre")
            tree_List_Of_Bookss.column("# 5", anchor=CENTER, width= 140)
            tree_List_Of_Bookss.heading("# 5", text="Publisher")

            first_time = True
            i = 1
            with open("Books.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    tree_List_Of_Bookss.insert('', 'end', values=(i, row[0], row[1], row[2],row[3]))
                    i+=1

            tree_List_Of_Bookss.pack()
            tree_List_Of_Bookss.config(yscrollcommand = scrollbar_numbers_1.set)
            scrollbar_numbers_1.config(command = tree_List_Of_Bookss.yview)

            frame_lower=  Frame(self)
            frame_lower.pack(padx=10,pady=10)
            
            Previous_Page_bar = Frame(frame_lower)
            Previous_Page_bar.pack(side = "left", padx=15)

            Prevoius_page_button = tk.Button(Previous_Page_bar, text="Prevoius Page", fg="white",bg = "blue", font=("Times",15),
                                            width = 20,command= lambda: [controller.show_frame(page_status_of_books), want_to_distroy()])
            Prevoius_page_button.pack()

            def want_to_distroy():
                tree_List_Of_Bookss.destroy()
                frame_upper.destroy()
                frame_lower.destroy()



class page_Find_The_Book_By_Searching_Name(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        titel = tk.StringVar()
        label_Find_The_Book_By_Searching_Name = tk.Label(self, text="Find The Book By Searching Titel", fg="black", font=("Times",22))
        label_Find_The_Book_By_Searching_Name.pack(pady=20,padx=20)


        frame_add_books_upper  =  Frame(self, bg = "Grey")
        frame_add_books_upper.pack(padx=20,  pady=20)
        
        titel_bar  =  Frame(frame_add_books_upper)
        titel_bar.pack(side = "left", padx=5,  pady=5)
        
        entery_titel_bar = Frame(frame_add_books_upper)
        entery_titel_bar.pack(side = "left", padx=5,  pady=5)

        titel_label = Label(titel_bar, text= "Titel", fg="black", font=("Times",15),width = 18)
        titel_label.pack(pady=10,padx=10)
        
        entery_titel = Entry(entery_titel_bar, textvariable= titel, font=("Times",15),justify='center')
        entery_titel.pack(pady=10,padx=10)

        def clear_entery_titel_1():
            entery_titel.delete(0, END)
        def check_status():
            with open("Books.csv", "r") as f:
                is_there = False
                reader = csv.reader(f)
                for row in reader:
                    if titel.get() == row[0]:
                        is_there = True
                        break
                    else:
                        continue
        
            if is_there == True:        
                showinfo(title='Result', message='Dear Admin it seems, '+ titel.get() + ' is in Library')
                clear_entery_titel_1()
            else:
                showwarning(title='There is no such Book in Library!', message='Dear Admin it seems, the given data are False')
                clear_entery_titel_1()

        clear_b1_bar  =  Frame(frame_add_books_upper)
        clear_b1_bar.pack(side = "left", padx=5,  pady=5)
        clear_b1 = tk.Button(clear_b1_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_1())
        clear_b1.pack()

        frame_add_books_lower  =  Frame(self)
        frame_add_books_lower.pack(padx=15,  pady=15)
        
        Check_bar  =  Frame(frame_add_books_lower)
        Check_bar.pack(side = "left", padx=5,  pady=5)
        
        Check_button = tk.Button(Check_bar, text="Check", fg="white",bg = "green", font=("Times",15),
                            command=lambda: check_status(), width= 15)
        Check_button.pack()
        
        Previous_Page_bar  =  Frame(frame_add_books_lower)
        Previous_Page_bar.pack(side = "left", padx=5,  pady=5)
        
        Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(page_status_of_books),clear_entery_titel_1()], width= 15)
        Previous_Page_button.pack()


class after_login_student(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def log_out():
            
            df = pd.read_csv("one.csv", index_col='username_email') 
            df.loc[get_email(), "who_is_connected"] = "NO INFOS"
            df.to_csv("one.csv")

        def insert_data_to_student():
            useremail_label["text"] = get_email()

        def get_email():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [4] == "CONNECTED":
                        email = row[0]
                        email_var = StringVar(self,email)
                        counter += 1
                        return email_var.get()

            if counter == 0:
                email_var = StringVar(self,"Nothing")
                return email_var.get()

        def inset_into_profile():
            useremail_label
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [0] == get_email():
                        firstname= row[5]
                        familyname= row[6]
                        phonenumber = row[7]
                        Firstname_entery_label.insert(0, firstname)
                        lastname_entery_label.insert(0, familyname)
                        phonenumber_entery_label.insert(0, phonenumber)

        global notification_student
        def notification_student():
            with open("Books.csv", "r") as k:
                list_of_notifs = []
                i = 1
                first_time = True
                reader = csv.reader(k)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    elif row[6] != "NO INFOS" and row[4] == get_email():
                        if row[9] == "CONFIRMED":
                            date = datetime.strptime(row[6], "%Y-%m-%d")
                            today = datetime.now()

                            if date < today:
                                string = "You have to pay the Fine for the Book : "
                                book = row[0] 
                                string += book
                                list_of_notifs.append(string)
                                i += 1
                                string = ""
                                book = ""
                        elif row [8] == "ACCEPTED":
                            date = datetime.strptime(row[6], "%Y-%m-%d")
                            today = datetime.now()
                            final_date = date - today
                            final_to_showw = final_date.days
                            if final_to_showw> 0:
                                date = datetime.strptime(row[6], "%Y-%m-%d")
                                today = datetime.now()
                                final_date = date - today
                                final_to_show = str(final_date.days)
                                string_0 = "in "
                                string = " days later you have to return the Book : "
                                book = row[0] 
                                string_0 += final_to_show + string + book
                                list_of_notifs.append(string_0)
                                i += 1
                                string = ""
                                string_0 = ""
                                book = ""
            if i == 1:
                showinfo(title="Notification",
                    message="Nothing to Show")
            else:
                stringg = "\n".join(list_of_notifs[i] for i in range(len(list_of_notifs)))
                showinfo(title="Notification",
                        message="Here is the latest News:\n\n"+ stringg)
                stringg = ""

        frame_upper  =  Frame(self, bg = "Grey")
        frame_upper.pack(padx=25,  pady=25)

        user_type_bar  =  Frame(frame_upper)
        user_type_bar.pack(side = "left", padx=5,  pady=5)

        email_bar  =  Frame(frame_upper)
        email_bar.pack(side = "left",padx=5,  pady=5)
        
        date_bar = Frame(frame_upper)
        date_bar.pack(side = "left", padx=5,  pady=5)
        
        notification_bar = Frame(frame_upper)
        notification_bar.pack(side = "left", padx=5,  pady=5)

        type_label = Label(user_type_bar, text= "Student", fg="black", font=("Times",15),width = 18)
        type_label.pack(pady=10,padx=10)
        
        global email_label_student
        email_label_student = Label(email_bar,  text= get_email(), fg="black", font=("Times",15), width = 18)
        email_label_student.pack(pady=10,padx=10)

        time = Label(date_bar, text = datetime.today().strftime('%Y-%m-%d'), fg="black", font=("Times",15), width = 18)
        time.pack(pady=10,padx=10)

        notification = Button(notification_bar, text= "🔔", font=("Times",15),fg="black",bg = "yellow",width = 3, height= 1,
                                command=lambda: notification_student())
        notification.pack()

        frame_lower_1=  Frame(self, bg = "Grey")
        frame_lower_1.pack(padx=10,  pady=10)

        add_and_remove_bar  =  Frame(frame_lower_1)
        add_and_remove_bar.pack(side = "left", padx=5,  pady=5)

        Requests_bar  =  Frame(frame_lower_1)
        Requests_bar.pack(side = "left",padx=5,  pady=5)

        Change_Passwords_bar = Frame(frame_lower_1)
        Change_Passwords_bar.pack(side = "left", padx=5,  pady=5)
        
        
        button1 = tk.Button(add_and_remove_bar, text="Request a Book", fg="white",bg = "blue", font=("Times",15),
                            width = 19, command= lambda: [controller.show_frame(request_books),list_of_books()])
        button1.pack(ipadx=10)

        button2 = tk.Button(Requests_bar, text="The List Of Books", fg="white",bg = "blue", font=("Times",15),
                            width = 19, command= lambda: controller.show_frame(the_list_of_books_student))
        button2.pack(ipadx=10)

        button3 = tk.Button(Change_Passwords_bar, text="Change Password", fg="white",bg = "blue", font=("Times",15),
                            command= lambda: controller.show_frame(change_passwords_yours_student),
                            width = 19)
        button3.pack(ipadx=10)     

        frame_lower_2=  Frame(self, bg = "Grey")
        frame_lower_2.pack(padx=10,  pady=10)

        add_and_remove_bar  =  Frame(frame_lower_2)
        add_and_remove_bar.pack(side = "left", padx=5,  pady=5)

        Requests_bar  =  Frame(frame_lower_2)
        Requests_bar.pack(side = "left",padx=5,  pady=5)

        Change_Passwords_bar = Frame(frame_lower_2)
        Change_Passwords_bar.pack(side = "left", padx=5,  pady=5)
        
        button4 = tk.Button(add_and_remove_bar, text="Pay The Fine", fg="white",bg = "blue", font=("Times",15),
                            width = 19, command= lambda: [controller.show_frame(Pay_The_Fine),list_ofPay_The_Fine()])
        button4.pack(ipadx=10)

        button5 = tk.Button(Requests_bar, text="Status Of Books", fg="white",bg = "blue", font=("Times",15),
                            command= lambda: controller.show_frame(page_status_of_books_student),width = 19)
        button5.pack(ipadx=10)

        button6 = tk.Button(Change_Passwords_bar, text="Profile", fg="white",bg = "blue", font=("Times",15),
                            command = lambda:[ controller.show_frame(profile_student), insert_data_to_student(), inset_into_profile()],width = 19)
        button6.pack(ipadx=10) 

        frame_lower_3=  Frame(self, bg = "Grey")
        frame_lower_3.pack(padx=10,  pady=10)
        
        Exit_bar = Frame(frame_lower_3)
        Exit_bar.pack(side = "left", padx=5,  pady=5)
        
        button7 = tk.Button(Exit_bar, text="Log Out", fg="white",bg = "red", font=("Times",15),
                            width = 19, command=lambda: [controller.show_frame(StartPage),log_out()])
        button7.pack(ipadx=10) 



class request_books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_add_books = tk.Label(self, text="Request a Book", fg="black", font=("Times",22))
        label_add_books.pack(pady=20,padx=20)


        global list_of_books
        def list_of_books():
            frame_upper=  Frame(self)
            frame_upper.pack(padx=10,pady=10)
            
            treebook_bar = Frame(frame_upper)
            treebook_bar.pack(side = "left")
            scrollbar_1_bar = Frame(frame_upper)
            scrollbar_1_bar.pack(side = "left")

            scrollbar_numbers_1 = Scrollbar(scrollbar_1_bar)
            scrollbar_numbers_1.pack(ipady= 37,side = RIGHT,fill = Y)


            global tree_books
            tree_books = ttk.Treeview(treebook_bar, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
            tree_books.column("# 1", anchor=CENTER, width= 140)
            tree_books.heading("# 1", text="Number")
            tree_books.column("# 2", anchor=CENTER, width= 140)
            tree_books.heading("# 2", text="Book")
            tree_books.column("# 3", anchor=CENTER, width= 140)
            tree_books.heading("# 3", text="Author")
            tree_books.column("# 4", anchor=CENTER, width= 140)
            tree_books.heading("# 4", text="Genre")
            tree_books.column("# 5", anchor=CENTER, width= 140)
            tree_books.heading("# 5", text="Publisher")


            with open("Books.csv", "r") as k:
                i = 1
                reader = csv.reader(k)
                for row in reader:
                    if row[7] == "Available":
                        tree_books.insert('', 'end', values=(i, row[0], row[1], row[2],row[3]))
                        i +=1

            tree_books.pack()
            tree_books.config(yscrollcommand = scrollbar_numbers_1.set)
            scrollbar_numbers_1.config(command = tree_books.yview)
            

            def get_data_book():
                selected_item = tree_books.focus()
                item_details = tree_books.item(selected_item)
                details = item_details.get("values")
                return details[1]
            
            def get_data_author():
                selected_item = tree_books.focus()
                item_details = tree_books.item(selected_item)
                details = item_details.get("values")
                return details[2]
            
            frame_lower=  Frame(self)
            frame_lower.pack(padx=10,pady=10)



            next_bar = Frame(frame_lower)
            next_bar.pack(side = "left", padx=15)
            Prevoius_page_bar  =  Frame(frame_lower)
            Prevoius_page_bar.pack(side = "left", padx=15)



            def want_to_reserve():
                ef = pd.read_csv("Books.csv", index_col='name_of_book')  
                book = get_data_book()
                author = get_data_author()
                let_to_reserve = ef.loc[book,"reserved_or_not"]
                username = ef.loc[book,"students_name"]

                if let_to_reserve != "RESERVED" or username == get_email():
                    data_about_book_name["text"] = book
                    data_about_book_author["text"] = author
                    tree_books.destroy()
                    frame_upper.destroy()
                    frame_lower.destroy()
                    controller.show_frame(reserve_book)
                    Important_Infos_For_Requesting_a_Book()

                else:
                    showwarning(title= "Pay Attention!", message= "Dear Student, your requested Book is reserved by someone else")
                    
            Next_page_button = tk.Button(next_bar, text="Next", fg="white",bg = "green", font=("Times",15), width = 15,
                                command= lambda: showwarning(
                                            title= "Pay Attention!", message= "Dear Student, you have approched the Maximum Size")
                                            if allowed_or_not() == False
                                            else 
                                            want_to_reserve()
                                )
            Next_page_button.pack()

            Prevoius_page_button = tk.Button(Prevoius_page_bar, text="Prevoius Page", fg="white",bg = "blue", font=("Times",15), width = 15,
                                command=lambda: [controller.show_frame(after_login_student), tree_books.destroy(),
                                                frame_upper.destroy(),
                                                frame_lower.destroy()] )
            Prevoius_page_button.pack()



        def get_email():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [4] == "CONNECTED":
                        email = row[0]
                        email_var = StringVar(self,email)
                        counter += 1
                        return email_var.get()

            if counter == 0:
                email_var = StringVar(self,"Nothing")
                return email_var.get()
            
        def allowed_or_not():
            i = 1
            first_time = True
            allowed = bool
            user_number_of_taken_books = 0

            with open("Books.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    elif row[4] == get_email():
                        user_number_of_taken_books += 1
                
            if user_number_of_taken_books < 2:
                allowed = True
            elif user_number_of_taken_books == 2:
                allowed = False
            
            return allowed


class reserve_book(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global Important_Infos_For_Requesting_a_Book

        def Important_Infos_For_Requesting_a_Book():
            showinfo( title="Important Infos For Requesting a Book",
                message="Pay Attention the date should be filled out like: 2023-2-24\n Which means: Year-Month-Day")

        def get_email():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [4] == "CONNECTED":
                        email = row[0]
                        email_var = StringVar(self,email)
                        counter += 1
                        return email_var.get()

        date_to_take1 = tk.StringVar()
        date_to_take11 = tk.StringVar()
        date_to_take111 = tk.StringVar()
        
        date_to_give1 = tk.StringVar()
        date_to_give11 = tk.StringVar()
        date_to_give111 = tk.StringVar()
        
        label_add_books = tk.Label(self, text="Reserve Book", fg="black", font=("Times",22))
        label_add_books.pack(pady=20,padx=20)

        frame_upper = Frame(self)

        frame_upper.pack(padx=10,pady=10)
        titel_bar = Frame(frame_upper)
        titel_bar.pack(side = "left")
        name_bar = Frame(frame_upper)
        name_bar.pack(side = "left")
        author_aaa_bar = Frame(frame_upper)
        author_aaa_bar.pack(side = "left")
        
        author_bar = Frame(frame_upper)
        author_bar.pack(side = "left")

        data_about_book_titel = tk.Label(titel_bar, text= "Titel:", fg="white", bg = "blue", font=("Times",15))
        data_about_book_titel.pack()

        global data_about_book_name
        data_about_book_name = tk.Label(name_bar, text= "Nothing", fg="white", bg = "blue", font=("Times",15))
        data_about_book_name.pack()

        data_about_book_authorrr = tk.Label(author_aaa_bar, text= "  Author:", fg="white", bg = "blue", font=("Times",15))
        data_about_book_authorrr.pack()

        global data_about_book_author
        data_about_book_author = tk.Label(author_bar, text= "Nothing", fg="white", bg = "blue", font=("Times",15))
        data_about_book_author.pack()

        frame_reserve_books_upper  =  Frame(self, bg = "Grey")
        frame_reserve_books_upper.pack(padx=10,  pady=10)
        
        date_to_take1_bar  =  Frame(frame_reserve_books_upper)
        date_to_take1_bar.pack(side = "left",padx=5,  pady=5)
        
        entery_date_to_take1_bar = Frame(frame_reserve_books_upper)
        entery_date_to_take1_bar.pack(side = "left",padx=5,  pady=5)
        entery_date_to_take2_bar = Frame(frame_reserve_books_upper)
        entery_date_to_take2_bar.pack(side = "left",padx=5,  pady=5)
        entery_date_to_take3_bar = Frame(frame_reserve_books_upper)
        entery_date_to_take3_bar.pack(side = "left",padx=5,  pady=5)
        clear_bar1 = Frame(frame_reserve_books_upper)
        clear_bar1.pack(side = "left",padx=5,  pady=5)

        date_to_take1_label = Label(date_to_take1_bar, text= "Date To Take", fg="black", font=("Times",15),width = 18)
        date_to_take1_label.pack(pady=10,padx=10)
        
        entery_date_to_take1 = Entry(entery_date_to_take1_bar, textvariable= date_to_take1, font=("Times",15),justify='center', width=4)
        entery_date_to_take1.pack(pady=10,padx=10)
        entery_date_to_take2 = Entry(entery_date_to_take2_bar, textvariable= date_to_take11, font=("Times",15),justify='center', width=4)
        entery_date_to_take2.pack(pady=10,padx=10)
        entery_date_to_take3 = Entry(entery_date_to_take3_bar, textvariable= date_to_take111, font=("Times",15),justify='center', width=4)
        entery_date_to_take3.pack(pady=10,padx=10)
        clear_b1 = tk.Button(clear_bar1, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command= lambda: [clear_text_1(),clear_text_11(),clear_text_111()])
        clear_b1.pack()
        
        #date to give

        frame_reserve_books_lower1  =  Frame(self, bg = "Grey")
        frame_reserve_books_lower1.pack(padx=10,  pady=10)
        
        date_to_give1_bar  =  Frame(frame_reserve_books_lower1)
        date_to_give1_bar.pack(side = "left",padx=5,  pady=5)
        
        entery_date_to_give1_bar = Frame(frame_reserve_books_lower1)
        entery_date_to_give1_bar.pack(side = "left",padx=5,  pady=5)
        entery_date_to_give2_bar = Frame(frame_reserve_books_lower1)
        entery_date_to_give2_bar.pack(side = "left",padx=5,  pady=5)
        entery_date_to_give3_bar = Frame(frame_reserve_books_lower1)
        entery_date_to_give3_bar.pack(side = "left",padx=5,  pady=5)
        clear_bar2 = Frame(frame_reserve_books_lower1)
        clear_bar2.pack(side = "left",padx=5,  pady=5)

        date_to_give1_label = Label(date_to_give1_bar, text= "Date To Give", fg="black", font=("Times",15),width = 18)
        date_to_give1_label.pack(pady=10,padx=10)
        
        entery_date_to_give1 = Entry(entery_date_to_give1_bar, textvariable= date_to_give1, font=("Times",15),justify='center', width=4)
        entery_date_to_give1.pack(pady=10,padx=10)
        entery_date_to_give2 = Entry(entery_date_to_give2_bar, textvariable= date_to_give11, font=("Times",15),justify='center', width=4)
        entery_date_to_give2.pack(pady=10,padx=10)
        entery_date_to_give3 = Entry(entery_date_to_give3_bar, textvariable= date_to_give111, font=("Times",15),justify='center', width=4)
        entery_date_to_give3.pack(pady=10,padx=10)
        clear_b2 = tk.Button(clear_bar2, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command= lambda: [clear_text_2(),clear_text_22(),clear_text_222()])
        clear_b2.pack()
        # under date to take and date to give
        
        frame_add_books_lower2  =  Frame(self)
        frame_add_books_lower2.pack(padx=10,  pady=10)
        
        Save_bar  =  Frame(frame_add_books_lower2)
        Save_bar.pack(side = "left", padx=5,  pady=5)

        save_button = tk.Button(Save_bar, text="Request", fg="white",bg = "green", font=("Times",15),width= 12,
                                command= lambda: save_data())
        save_button.pack()
        
        Previous_Page_bar  =  Frame(frame_add_books_lower2)
        Previous_Page_bar.pack(side = "left", padx=5,  pady=5)

        Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page",
                                        fg="white",bg = "blue", font=("Times",15),width= 12,
                                        command= lambda: [controller.show_frame(request_books),list_of_books(),clear_text_1(),clear_text_11(),clear_text_111(),
                                                    clear_text_2(),clear_text_22(),clear_text_222()] )
        Previous_Page_button.pack()
        #clear buttons
        
        # delete date to take
        def clear_text_1():
            entery_date_to_take1.delete(0, END)
        def clear_text_11():
            entery_date_to_take2.delete(0, END)
        def clear_text_111():
            entery_date_to_take3.delete(0, END)
            
        # delete date to give
        def clear_text_2():
            entery_date_to_give1.delete(0, END)
        def clear_text_22():
            entery_date_to_give2.delete(0, END)
        def clear_text_222():
            entery_date_to_give3.delete(0, END)
        # save data
        def save_data():
            df = pd.read_csv("Books.csv", index_col='name_of_book')
            date_to_take_final = date_to_take1.get()+"-"+date_to_take11.get()+"-"+date_to_take111.get()
            date_to_give_final = date_to_give1.get()+"-"+date_to_give11.get()+"-"+date_to_give111.get()
            book = data_about_book_name.cget("text")
            df.loc[book , "date_to_take"] = date_to_take_final
            df.to_csv("Books.csv")
            df.loc[book , "date_to_give"] = date_to_give_final
            df.to_csv("Books.csv")
            df.loc[book , "students_name"] = get_email()
            df.to_csv("Books.csv")
            df.loc[book , "reserved_or_not"] = "RESERVED"
            df.to_csv("Books.csv")
            showinfo(title='Requested Successfully',message='Your demand has been successfully requested!')
            clear_text_1(),clear_text_11(),clear_text_111(),
            clear_text_2(),clear_text_22(),clear_text_222()

        clear_all_bar  =  Frame(frame_add_books_lower2)
        clear_all_bar.pack(side = "left", padx=5,  pady=5)

        clear_all_button = tk.Button(clear_all_bar, text="Clear All", fg="white",bg = "blue", font=("Times",15),width= 12,
                                    command= lambda: [clear_text_1(),clear_text_11(),clear_text_111(),
                                                    clear_text_2(),clear_text_22(),clear_text_222()])
        clear_all_button.pack()


class the_list_of_books_student(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_add_and_remove = tk.Label(self, text="The List of Books", fg="black", font=("Times",22))
        label_add_and_remove.pack(pady=20,padx=20)

        button = tk.Button(self, text="List of Requested Books", fg="white",bg = "blue", font=("Times",15),
                            command=lambda:[ controller.show_frame(List_of_Requested_Books), List_of_Requested_Booksss()],width = 20)
        button.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="List of Taken Books", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(List_of_Taken_Books), List_of_Taken_Booksss()],width = 20)
        button2.pack(pady=10,padx=10)

        button3 = tk.Button(self, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(after_login_student),width = 20)
        button3.pack(pady=10,padx=10)


class List_of_Requested_Books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_List_of_Requested_Books = tk.Label(self, text="List of Requested Books", fg="black", font=("Times",22))
        label_List_of_Requested_Books.pack(pady=20,padx=20)

        global List_of_Requested_Booksss
        def List_of_Requested_Booksss():
            frame_upper=  Frame(self)
            frame_upper.pack(padx=10,pady=10)
            
            tree_List_of_Requested_Books_bar = Frame(frame_upper)
            tree_List_of_Requested_Books_bar.pack(side = "left")
            scrollbar_1_bar = Frame(frame_upper)
            scrollbar_1_bar.pack(side = "left")

            scrollbar_numbers_1 = Scrollbar(scrollbar_1_bar)
            scrollbar_numbers_1.pack(ipady= 37,side = RIGHT,fill = Y)


            global tree_List_of_Requested_Books
            tree_List_of_Requested_Books = ttk.Treeview(tree_List_of_Requested_Books_bar, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
            tree_List_of_Requested_Books.column("# 1", anchor=CENTER, width= 140)
            tree_List_of_Requested_Books.heading("# 1", text="Number")
            tree_List_of_Requested_Books.column("# 2", anchor=CENTER, width= 140)
            tree_List_of_Requested_Books.heading("# 2", text="Book")
            tree_List_of_Requested_Books.column("# 3", anchor=CENTER, width= 140)
            tree_List_of_Requested_Books.heading("# 3", text="Student")
            tree_List_of_Requested_Books.column("# 4", anchor=CENTER, width= 140)
            tree_List_of_Requested_Books.heading("# 4", text="Date To Take")
            tree_List_of_Requested_Books.column("# 5", anchor=CENTER, width= 140)
            tree_List_of_Requested_Books.heading("# 5", text="Date To Give")

            first_time = True
            i = 1
            with open("Books.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    elif row[4] == get_email() and row[8] == "NO INFOS":
                        tree_List_of_Requested_Books.insert('', 'end', values=(i, row[0], row[4], row[5],row[6]))
                        i += 1

            tree_List_of_Requested_Books.pack()
            tree_List_of_Requested_Books.config(yscrollcommand = scrollbar_numbers_1.set)
            scrollbar_numbers_1.config(command = tree_List_of_Requested_Books.yview)


            def get_data_book():
                selected_item = tree_List_of_Requested_Books.focus()
                item_details = tree_List_of_Requested_Books.item(selected_item)
                details = item_details.get("values")
                return details[1]

            frame_lower=  Frame(self)
            frame_lower.pack(padx=10,pady=10)
            withdraw_bar = Frame(frame_lower)
            withdraw_bar.pack(side = "left", padx=15)
            Previous_Page_bar = Frame(frame_lower)
            Previous_Page_bar.pack(side = "left", padx=15)

            Withdraw_button = tk.Button(withdraw_bar, text="Withdraw", fg="white",bg = "red", font=("Times",15), width = 15,
                                    command= lambda: want_to_withdraw())
            Withdraw_button.pack()
            Prevoius_page_button = tk.Button(Previous_Page_bar, text="Prevoius Page", fg="white",bg = "blue", font=("Times",15), width =15,
                                            command= lambda:[ controller.show_frame(the_list_of_books_student),tree_List_of_Requested_Books.destroy()
                                            ,frame_upper.destroy(),frame_lower.destroy()])
            Prevoius_page_button.pack()

            def want_to_withdraw():
                df = pd.read_csv("Books.csv", index_col='name_of_book')  
                book = get_data_book()
                df.loc[book , "students_name"] = "NO INFOS"
                df.to_csv("Books.csv")
                df.loc[book , "date_to_take"] = "NO INFOS"
                df.to_csv("Books.csv")
                df.loc[book , "date_to_give"] = "NO INFOS"
                df.to_csv("Books.csv")
                df.loc[book , "book_available_or_not"] = "Available"
                df.to_csv("Books.csv")
                df.loc[book , "accept_or_decline"] = "NO INFOS"
                df.to_csv("Books.csv")
                df.loc[book , "fine"] = "NO INFOS"
                df.to_csv("Books.csv")
                df.loc[book , "reserved_or_not"] = "NO INFOS"
                df.to_csv("Books.csv")

                tree_List_of_Requested_Books.destroy()
                frame_upper.destroy()
                frame_lower.destroy()
                controller.show_frame(List_of_Requested_Books)
                List_of_Requested_Booksss()


        def get_email():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [4] == "CONNECTED":
                        email = row[0]
                        email_var = StringVar(self,email)
                        counter += 1
                        return email_var.get()




class List_of_Taken_Books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_List_of_Taken_Books = tk.Label(self, text="List of Taken Books", fg="black", font=("Times",22))
        label_List_of_Taken_Books.pack(pady=20,padx=20)

        global List_of_Taken_Booksss
        def List_of_Taken_Booksss():
            frame_upper=  Frame(self)
            frame_upper.pack(padx=10,pady=10)
            
            tree_List_of_Taken_Books_bar = Frame(frame_upper)
            tree_List_of_Taken_Books_bar.pack(side = "left")
            scrollbar_1_bar = Frame(frame_upper)
            scrollbar_1_bar.pack(side = "left")

            scrollbar_numbers_1 = Scrollbar(scrollbar_1_bar)
            scrollbar_numbers_1.pack(ipady= 37,side = RIGHT,fill = Y)


            global tree_List_of_Taken_Books
            tree_List_of_Taken_Books = ttk.Treeview(tree_List_of_Taken_Books_bar, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
            tree_List_of_Taken_Books.column("# 1", anchor=CENTER, width= 140)
            tree_List_of_Taken_Books.heading("# 1", text="Number")
            tree_List_of_Taken_Books.column("# 2", anchor=CENTER, width= 140)
            tree_List_of_Taken_Books.heading("# 2", text="Book")
            tree_List_of_Taken_Books.column("# 3", anchor=CENTER, width= 140)
            tree_List_of_Taken_Books.heading("# 3", text="Student")
            tree_List_of_Taken_Books.column("# 4", anchor=CENTER, width= 140)
            tree_List_of_Taken_Books.heading("# 4", text="Date To Take")
            tree_List_of_Taken_Books.column("# 5", anchor=CENTER, width= 140)
            tree_List_of_Taken_Books.heading("# 5", text="Date To Give")

            first_time = True
            i = 1
            with open("Books.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    elif row[4] == get_email() and row[8] == "ACCEPTED":
                        tree_List_of_Taken_Books.insert('', 'end', values=(i, row[0], row[4], row[5],row[6]))
                        i += 1

            tree_List_of_Taken_Books.pack()
            tree_List_of_Taken_Books.config(yscrollcommand = scrollbar_numbers_1.set)
            scrollbar_numbers_1.config(command = tree_List_of_Taken_Books.yview)

            frame_lower=  Frame(self)
            frame_lower.pack(padx=10,pady=10)
            Previous_Page_bar = Frame(frame_lower)
            Previous_Page_bar.pack(side = "left", padx=15)

            Prevoius_page_button = tk.Button(Previous_Page_bar, text="Prevoius Page", fg="white",bg = "blue", font=("Times",15),
                                            command= lambda: [controller.show_frame(the_list_of_books_student), want_to_distroy()])
            Prevoius_page_button.pack()

            def want_to_distroy():
                tree_List_of_Taken_Books.destroy()
                frame_upper.destroy()
                frame_lower.destroy()

        def get_email():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [4] == "CONNECTED":
                        email = row[0]
                        email_var = StringVar(self,email)
                        counter += 1
                        return email_var.get()


class change_passwords_yours_student(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        password = tk.StringVar()

        label_change_passwords_yours_student = tk.Label(self, text="Change Password", fg="black", font=("Times",22))
        label_change_passwords_yours_student.pack(pady=20,padx=20)

        frame_add_books_upper  =  Frame(self, bg = "Grey")
        frame_add_books_upper.pack(padx=20,  pady=20)
        
        titel_bar  =  Frame(frame_add_books_upper)
        titel_bar.pack(side = "left", padx=5,  pady=5)
        
        entery_titel_bar = Frame(frame_add_books_upper)
        entery_titel_bar.pack(side = "left", padx=5,  pady=5)

        titel_label = Label(titel_bar, text= "New Password", fg="black", font=("Times",15),width = 18)
        titel_label.pack(pady=10,padx=10)
        
        entery_titel = Entry(entery_titel_bar, textvariable= password, font=("Times",15),justify='center', show="•")
        entery_titel.pack(pady=10,padx=10)

        def clear_entery_titel_1():
            entery_titel.delete(0, END)

        def get_email():
            counter = 0
            with open("one.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row [4] == "CONNECTED":
                        email = row[0]
                        email_var = StringVar(self,email)
                        counter += 1
                        return email_var.get()

        clear_b1_bar  =  Frame(frame_add_books_upper)
        clear_b1_bar.pack(side = "left", padx=5,  pady=5)
        clear_b1 = tk.Button(clear_b1_bar, text="Clear", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: clear_entery_titel_1())
        clear_b1.pack()

        frame_add_books_lower  =  Frame(self)
        frame_add_books_lower.pack(padx=15,  pady=15)

        def want_to_save():
            name = get_email()
            df = pd.read_csv("one.csv", index_col='username_email') 
            df.loc[name , "password"] = password.get()
            df.to_csv("one.csv")
            df.loc[name , "changed_password_by_whom"] = "student"
            df.to_csv("one.csv")
            showinfo(title='Password Changed Successfully', message='Dear Student, your new password is: '+ password.get())
            clear_entery_titel_1()

        save_bar  =  Frame(frame_add_books_lower)
        save_bar.pack(side = "left", padx=5,  pady=5)
        save_button = tk.Button(save_bar, text="Save", fg="white",bg = "green", font=("Times",15), width= 15,
                                command= lambda: want_to_save())
        save_button.pack()
        
        Previous_Page_bar  =  Frame(frame_add_books_lower)
        Previous_Page_bar.pack(side = "left", padx=5,  pady=5)
        
        Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(after_login_student),clear_entery_titel_1()], width= 15)
        Previous_Page_button.pack()


class Pay_The_Fine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_add_books = tk.Label(self, text="Pay Fine Amount", fg="black", font=("Times",22))
        label_add_books.pack(pady=20,padx=20)


        global list_ofPay_The_Fine
        def list_ofPay_The_Fine():
            frame_upper_1=  Frame(self)
            frame_upper_1.pack(padx=10,pady=10)
            
            treePay_The_Fine_bar = Frame(frame_upper_1)
            treePay_The_Fine_bar.pack(side = "left")
            scrollbar_2_bar = Frame(frame_upper_1)
            scrollbar_2_bar.pack(side = "left")

            scrollbar_numbers_2 = Scrollbar(scrollbar_2_bar)
            scrollbar_numbers_2.pack(ipady= 37,side = RIGHT,fill = Y)
            

            global treePay_The_Fine
            treePay_The_Fine = ttk.Treeview(treePay_The_Fine_bar, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=5)
            treePay_The_Fine.column("# 1", anchor=CENTER, width= 110)
            treePay_The_Fine.heading("# 1", text="Number")
            treePay_The_Fine.column("# 2", anchor=CENTER, width= 110)
            treePay_The_Fine.heading("# 2", text="Book")
            treePay_The_Fine.column("# 3", anchor=CENTER, width= 110)
            treePay_The_Fine.heading("# 3", text="Student")
            treePay_The_Fine.column("# 4", anchor=CENTER, width= 110)
            treePay_The_Fine.heading("# 4", text="Date To Take")
            treePay_The_Fine.column("# 5", anchor=CENTER, width= 110)
            treePay_The_Fine.heading("# 5", text="Date To Give")
            treePay_The_Fine.column("# 6", anchor=CENTER, width= 110)
            treePay_The_Fine.heading("# 6", text="Fine Amount")

            def get_email():
                counter = 0
                with open("one.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row [4] == "CONNECTED":
                            email = row[0]
                            email_var = StringVar(self,email)
                            counter += 1
                            return email_var.get()

            with open("Books.csv", "r") as k:
                i = 1
                first_time = True
                reader = csv.reader(k)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    elif row[6] != "NO INFOS" and row[4] == get_email():
                        if row[9] == "CONFIRMED":
                            date = datetime.strptime(row[6], "%Y-%m-%d")
                            today = datetime.now()
                
                            if date < today:
                                final_date = today - date
                                fine_to_show = final_date.days
                                treePay_The_Fine.insert('', 'end', values=(i, row[0], row[4], row[5],row[6], str(fine_to_show*(fine_amount.get())) + " £"))
                                i += 1
                            else:
                                continue

            treePay_The_Fine.pack()
            treePay_The_Fine.config(yscrollcommand = scrollbar_numbers_2.set)
            scrollbar_numbers_2.config(command = treePay_The_Fine.yview)
            

            def get_data_book():
                selected_item = treePay_The_Fine.focus()
                item_details = treePay_The_Fine.item(selected_item)
                details = item_details.get("values")
                return details[1]
            
            frame_lower_1=  Frame(self)
            frame_lower_1.pack(padx=10,pady=10)

            accept_bar = Frame(frame_lower_1)
            accept_bar.pack(side = "left", padx=15)
            previous_page_bar  =  Frame(frame_lower_1)
            previous_page_bar.pack(side = "left", padx=15)


            accept_button = tk.Button(accept_bar, text="Pay Fine", fg="white",bg = "green", font=("Times",15), width=10,
                                    command = lambda: want_to_pay())
            accept_button.pack()


            previous_page_button = tk.Button(previous_page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                                            width=10,
                                            command= lambda:[controller.show_frame(after_login_student),treePay_The_Fine.destroy(),
                                            frame_upper_1.destroy(),
                                            frame_lower_1.destroy()] )
            previous_page_button.pack()


            def want_to_pay():
                ef = pd.read_csv("Books.csv", index_col='name_of_book')  
                book = get_data_book()
                
                ef.loc[book , "fine"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "accept_or_decline"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "book_available_or_not"] = "Available"
                ef.to_csv("Books.csv")
                ef.loc[book , "students_name"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "date_to_take"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "date_to_give"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "fine"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "reserved_or_not"] = "NO INFOS"
                ef.to_csv("Books.csv")

                showinfo(title= "Fine Paied", message= "Dear Student, you have paied the fine")
                treePay_The_Fine.destroy()
                frame_upper_1.destroy()
                frame_lower_1.destroy()
                controller.show_frame(Pay_The_Fine)
                list_ofPay_The_Fine()
                
class page_status_of_books_student(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_page_status_of_books = tk.Label(self, text="Status Of Books", fg="black", font=("Times",22))
        label_page_status_of_books.pack(pady=20,padx=20)

        button = tk.Button(self, text="See The List Of Books", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(page_See_The_List_Of_Books), List_List_Of_Books()],width = 35)
        button.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Find The Book By Searching Titel", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(page_Find_The_Book_By_Searching_Name),width = 35)
        button2.pack(pady=10,padx=10)


        button3 = tk.Button(self, text="Return The Books", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(return_books),List_of_return_Booksss()],width = 35)
        button3.pack(pady=10,padx=10)


        button4 = tk.Button(self, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: controller.show_frame(after_login_student),width = 35)
        button4.pack(pady=10,padx=10)

class return_books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_return_book = tk.Label(self, text="Return The Books", fg="black", font=("Times",22))
        label_return_book.pack(pady=20,padx=20)

        global List_of_return_Booksss
        def List_of_return_Booksss():
            frame_upper=  Frame(self)
            frame_upper.pack(padx=10,pady=10)
            
            tree_List_of_Return_Books_bar = Frame(frame_upper)
            tree_List_of_Return_Books_bar.pack(side = "left")
            scrollbar_1_bar = Frame(frame_upper)
            scrollbar_1_bar.pack(side = "left")

            scrollbar_numbers_1 = Scrollbar(scrollbar_1_bar)
            scrollbar_numbers_1.pack(ipady= 37,side = RIGHT,fill = Y)


            global tree_List_of_Return_Books
            tree_List_of_Return_Books = ttk.Treeview(tree_List_of_Return_Books_bar, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
            tree_List_of_Return_Books.column("# 1", anchor=CENTER, width= 140)
            tree_List_of_Return_Books.heading("# 1", text="Number")
            tree_List_of_Return_Books.column("# 2", anchor=CENTER, width= 140)
            tree_List_of_Return_Books.heading("# 2", text="Book")
            tree_List_of_Return_Books.column("# 3", anchor=CENTER, width= 140)
            tree_List_of_Return_Books.heading("# 3", text="Student")
            tree_List_of_Return_Books.column("# 4", anchor=CENTER, width= 140)
            tree_List_of_Return_Books.heading("# 4", text="Date To Take")
            tree_List_of_Return_Books.column("# 5", anchor=CENTER, width= 140)
            tree_List_of_Return_Books.heading("# 5", text="Date To Give")

            def get_email():
                counter = 0
                with open("one.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row [4] == "CONNECTED":
                            email = row[0]
                            email_var = StringVar(self,email)
                            counter += 1
                            return email_var.get()

            first_time = True
            i = 1
            with open("Books.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if first_time == True:
                        first_time = False
                        continue
                    elif row[4] == get_email() and row[8] == "ACCEPTED":
                        tree_List_of_Return_Books.insert('', 'end', values=(i, row[0], row[4], row[5],row[6]))
                        i += 1

            tree_List_of_Return_Books.pack()
            tree_List_of_Return_Books.config(yscrollcommand = scrollbar_numbers_1.set)
            scrollbar_numbers_1.config(command = tree_List_of_Return_Books.yview)

            frame_lower=  Frame(self)
            frame_lower.pack(padx=10,pady=10)

            return_bar = Frame(frame_lower)
            return_bar.pack(side = "left", padx=15)

            return_button = tk.Button(return_bar, text="Return", fg="white",bg = "green", font=("Times",15),width = 15,
                                            command= lambda: return_book())
            return_button.pack()

            Previous_Page_bar = Frame(frame_lower)
            Previous_Page_bar.pack(side = "left", padx=15)

            Prevoius_page_button = tk.Button(Previous_Page_bar, text="Prevoius Page", fg="white",bg = "blue", font=("Times",15), width = 15,
                                            command= lambda: [controller.show_frame(page_status_of_books_student), want_to_distroy()])
            Prevoius_page_button.pack()

            def want_to_distroy():
                tree_List_of_Return_Books.destroy()
                frame_upper.destroy()
                frame_lower.destroy()

            def get_data_book():
                selected_item = tree_List_of_Return_Books.focus()
                item_details = tree_List_of_Return_Books.item(selected_item)
                details = item_details.get("values")
                return details[1]

            def return_book():
                ef = pd.read_csv("Books.csv", index_col='name_of_book')  
                book = get_data_book()

                ef.loc[book , "fine"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "accept_or_decline"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "book_available_or_not"] = "Available"
                ef.to_csv("Books.csv")
                ef.loc[book , "students_name"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "date_to_take"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "date_to_give"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "fine"] = "NO INFOS"
                ef.to_csv("Books.csv")
                ef.loc[book , "reserved_or_not"] = "NO INFOS"
                ef.to_csv("Books.csv")

                showinfo(title= "Book Successfully Returned", message= "Dear Student, you have returned " + book)
                tree_List_of_Return_Books.destroy()
                frame_upper.destroy()
                frame_lower.destroy()
                controller.show_frame(return_books)
                List_of_return_Booksss()

class profile_student(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        firstnamee = StringVar()
        lastname = StringVar()
        phone_number = StringVar()

        def get_email():
                counter = 0
                with open("one.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row [4] == "CONNECTED":
                            email = row[0]
                            email_var = StringVar(self,email)
                            counter += 1
                            return email_var.get()


        def clear_text_1():
            Firstname_entery_label.delete(0, END)
        def clear_text_2():
            lastname_entery_label.delete(0, END)
        def clear_text_3():
            phonenumber_entery_label.delete(0, END)

        def insert_data_to_one_csv():
            ef = pd.read_csv("one.csv", index_col='username_email')  
            name = get_email()
            ef.loc[name , "firstname"] = firstnamee.get()
            ef.to_csv("one.csv")
            ef.loc[name , "familyname"] = lastname.get()
            ef.to_csv("one.csv")
            ef.loc[name , "phonenumber"] = phone_number.get()
            ef.to_csv("one.csv")
            showinfo(title="Profile Saved Successfully", message="You have Changed The Profile")

        label_profile_student = tk.Label(self, text="Profile", fg="black", font=("Times",22))
        label_profile_student.pack(pady=20,padx=20)
        
        frame_upper=  Frame(self, bg = "grey")
        frame_upper.pack(padx=2,pady=15)

        email_bar  =  Frame(frame_upper)
        email_bar.pack(side = "left", padx=5,  pady=5)

        useremail_bar = Frame(frame_upper)
        useremail_bar.pack(side = "left", padx=5,  pady=5)

        email_label = Label(email_bar, text= "E-mail", fg="black", font=("Times",14),width = 19)
        email_label.pack(pady=10,padx=10)

        global useremail_label
        useremail_label = Label(useremail_bar, text= "No Infos", font=("Times",14),justify='center', width= 27)
        useremail_label.pack(pady=10,padx=10)

        frame_upper_1=  Frame(self, bg = "grey")
        frame_upper_1.pack(padx=2,pady=2)

        Firstname_bar  =  Frame(frame_upper_1)
        Firstname_bar.pack(side = "left", padx=5,  pady=5)

        Firstname_entery_bar = Frame(frame_upper_1)
        Firstname_entery_bar.pack(side = "left", padx=5,  pady=5)

        firstname_label = Label(Firstname_bar, text= "First Name", fg="black", font=("Times",14),width = 19)
        firstname_label.pack(pady=10,padx=10)

        global Firstname_entery_label
        Firstname_entery_label = Entry(Firstname_entery_bar,textvariable= firstnamee, font=("Times",14),justify='center', width= 30)
        Firstname_entery_label.pack(pady=10,padx=10)
        

        frame_upper_2=  Frame(self, bg = "grey")
        frame_upper_2.pack(padx=2,pady=2)

        Lastname_bar  =  Frame(frame_upper_2)
        Lastname_bar.pack(side = "left", padx=5,  pady=5)

        Lastname_entery_bar = Frame(frame_upper_2)
        Lastname_entery_bar.pack(side = "left", padx=5,  pady=5)

        lastname_label = Label(Lastname_bar, text= "Last Name", fg="black", font=("Times",14),width = 19)
        lastname_label.pack(pady=10,padx=10)

        global lastname_entery_label
        lastname_entery_label = Entry(Lastname_entery_bar,textvariable= lastname, font=("Times",14),justify='center', width= 30)
        lastname_entery_label.pack(pady=10,padx=10)

        frame_upper_3=  Frame(self, bg = "grey")
        frame_upper_3.pack(padx=2,pady=2)

        PhoneNumber_bar  =  Frame(frame_upper_3)
        PhoneNumber_bar.pack(side = "left", padx=5,  pady=5)

        PhoneNumber_entery_bar = Frame(frame_upper_3)
        PhoneNumber_entery_bar.pack(side = "left", padx=5,  pady=5)

        PhoneNumber_label = Label(PhoneNumber_bar, text= "Phone Number", fg="black", font=("Times",14),width = 19)
        PhoneNumber_label.pack(pady=10,padx=10)

        global phonenumber_entery_label
        phonenumber_entery_label = Entry(PhoneNumber_entery_bar,textvariable= phone_number, font=("Times",14),justify='center', width= 30)
        phonenumber_entery_label.pack(pady=10,padx=10)
        
        frame__lower  =  Frame(self)
        frame__lower.pack(padx=10,  pady=10)

        Save_bar  =  Frame(frame__lower)
        Save_bar.pack(side = "left", padx=5,  pady=5)

        save_button = tk.Button(Save_bar, text="Save", fg="white",bg = "green", font=("Times",15), width= 15,
                                command= lambda: insert_data_to_one_csv())
        save_button.pack()
        
        Previous_Page_bar  =  Frame(frame__lower)
        Previous_Page_bar.pack(side = "left", padx=5,  pady=5)

        Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(after_login_student),clear_text_1(),clear_text_2(),
                                                clear_text_3()], width= 15)
        Previous_Page_button.pack()
        
        clear_all_bar  =  Frame(frame__lower)
        clear_all_bar.pack(side = "left", padx=5,  pady=5)

        clear_all_button = tk.Button(clear_all_bar, text="Clear All", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [clear_text_1(),clear_text_2(),clear_text_3()], width= 15)
        clear_all_button.pack()

class profile_admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        firstnamee1 = StringVar()
        lastname1 = StringVar()
        phone_number1 = StringVar()

        def get_email():
                counter = 0
                with open("one.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row [4] == "CONNECTED":
                            email = row[0]
                            email_var = StringVar(self,email)
                            counter += 1
                            return email_var.get()


        def clear_text_1():
            Firstname_entery_label1.delete(0, END)
        def clear_text_2():
            lastname_entery_label1.delete(0, END)
        def clear_text_3():
            phonenumber_entery_label1.delete(0, END)

        def insert_data_to_one_csv():
            ef = pd.read_csv("one.csv", index_col='username_email')  
            name = get_email()
            ef.loc[name , "firstname"] = firstnamee1.get()
            ef.to_csv("one.csv")
            ef.loc[name , "familyname"] = lastname1.get()
            ef.to_csv("one.csv")
            ef.loc[name , "phonenumber"] = phone_number1.get()
            ef.to_csv("one.csv")
            showinfo(title="Profile Saved Successfully", message="You have Changed The Profile")

        label_profile_student = tk.Label(self, text="Profile", fg="black", font=("Times",22))
        label_profile_student.pack(pady=20,padx=20)
        
        frame_upper=  Frame(self, bg = "grey")
        frame_upper.pack(padx=2,pady=15)

        email_bar  =  Frame(frame_upper)
        email_bar.pack(side = "left", padx=5,  pady=5)

        useremail_bar = Frame(frame_upper)
        useremail_bar.pack(side = "left", padx=5,  pady=5)

        email_label = Label(email_bar, text= "E-mail", fg="black", font=("Times",14),width = 19)
        email_label.pack(pady=10,padx=10)

        global useremail_label1
        useremail_label1 = Label(useremail_bar, text= "No Infos", font=("Times",14),justify='center', width= 27)
        useremail_label1.pack(pady=10,padx=10)

        frame_upper_1=  Frame(self, bg = "grey")
        frame_upper_1.pack(padx=2,pady=2)

        Firstname_bar  =  Frame(frame_upper_1)
        Firstname_bar.pack(side = "left", padx=5,  pady=5)

        Firstname_entery_bar = Frame(frame_upper_1)
        Firstname_entery_bar.pack(side = "left", padx=5,  pady=5)

        firstname_label = Label(Firstname_bar, text= "First Name", fg="black", font=("Times",14),width = 19)
        firstname_label.pack(pady=10,padx=10)

        global Firstname_entery_label1
        Firstname_entery_label1 = Entry(Firstname_entery_bar,textvariable= firstnamee1, font=("Times",14),justify='center', width= 30)
        Firstname_entery_label1.pack(pady=10,padx=10)
        

        frame_upper_2=  Frame(self, bg = "grey")
        frame_upper_2.pack(padx=2,pady=2)

        Lastname_bar  =  Frame(frame_upper_2)
        Lastname_bar.pack(side = "left", padx=5,  pady=5)

        Lastname_entery_bar = Frame(frame_upper_2)
        Lastname_entery_bar.pack(side = "left", padx=5,  pady=5)

        lastname_label = Label(Lastname_bar, text= "Last Name", fg="black", font=("Times",14),width = 19)
        lastname_label.pack(pady=10,padx=10)

        global lastname_entery_label1
        lastname_entery_label1 = Entry(Lastname_entery_bar,textvariable= lastname1, font=("Times",14),justify='center', width= 30)
        lastname_entery_label1.pack(pady=10,padx=10)

        frame_upper_3=  Frame(self, bg = "grey")
        frame_upper_3.pack(padx=2,pady=2)

        PhoneNumber_bar  =  Frame(frame_upper_3)
        PhoneNumber_bar.pack(side = "left", padx=5,  pady=5)

        PhoneNumber_entery_bar = Frame(frame_upper_3)
        PhoneNumber_entery_bar.pack(side = "left", padx=5,  pady=5)

        PhoneNumber_label = Label(PhoneNumber_bar, text= "Phone Number", fg="black", font=("Times",14),width = 19)
        PhoneNumber_label.pack(pady=10,padx=10)

        global phonenumber_entery_label1
        phonenumber_entery_label1 = Entry(PhoneNumber_entery_bar,textvariable= phone_number1, font=("Times",14),justify='center', width= 30)
        phonenumber_entery_label1.pack(pady=10,padx=10)
        
        frame__lower  =  Frame(self)
        frame__lower.pack(padx=10,  pady=10)

        Save_bar  =  Frame(frame__lower)
        Save_bar.pack(side = "left", padx=5,  pady=5)

        save_button = tk.Button(Save_bar, text="Save", fg="white",bg = "green", font=("Times",15), width= 15,
                                command= lambda: insert_data_to_one_csv())
        save_button.pack()
        
        Previous_Page_bar  =  Frame(frame__lower)
        Previous_Page_bar.pack(side = "left", padx=5,  pady=5)

        Previous_Page_button = tk.Button(Previous_Page_bar, text="Previous Page", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [controller.show_frame(after_login_admin),clear_text_1(),clear_text_2(),
                                                clear_text_3()], width= 15)
        Previous_Page_button.pack()
        
        clear_all_bar  =  Frame(frame__lower)
        clear_all_bar.pack(side = "left", padx=5,  pady=5)

        clear_all_button = tk.Button(clear_all_bar, text="Clear All", fg="white",bg = "blue", font=("Times",15),
                            command=lambda: [clear_text_1(),clear_text_2(),clear_text_3()], width= 15)
        clear_all_button.pack()


app = SeaofBTCapp()
app.title("Library Managment System")
app.iconphoto(False, tk.PhotoImage(file="my_icon.ico"))
app.mainloop()