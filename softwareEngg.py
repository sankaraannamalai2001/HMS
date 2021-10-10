from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="1.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=400, y=100, width=800, height=600)

        title = Label(frame_login, text="LOGIN", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(
            x=250, y=30)
        subtitle = Label(frame_login, text="Login here", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                         bg="white").place(x=250, y=100)

        lbl_user = Label(frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=140)
        self.username = Entry(frame_login, text="Username", font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=250, y=170, width=320, height=35)

        lbl_user = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=210)
        self.password = Entry(frame_login, text="Password", font=("Goudy old style", 15), bg="#E7E6E6", show="*")
        self.password.place(x=250, y=240, width=320, height=35)

        forget = Button(frame_login,command=self.login1, text="SIGN UP", bd=0, font=("Goudy old style", 15), fg="#6162FF",
                        bg="white").place(x=250, y=280)
        submit = Button(frame_login, command=self.check_function, text="LOGIN", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF", fg="white").place(x=250, y=320, width=180, height=40)

    def login1(self):
        root.after(2000, Login1(root))
    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        user=self.username.get()
        pwd=self.password.get()
        con = mysql.connect(host="localhost", user="root", password="", database="hospital")
        cursor = con.cursor()
        cursor.execute("select username from user where username='"+user+"' and password='"+pwd+"'")
        record= cursor.fetchall()
        con.close()
        try:
            if self.username.get() == "doctor" and self.password.get() == "doctor":
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
                root.after(2000, Doctor1(root))
            elif record[0][0]:
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
                root.after(2000, SecondPage(root))
        except IndexError:
            messagebox.showerror("Error", "Invalid username or password", parent=self.root)

class Login1:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)

        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=400, y=100, width=800, height=600)

        title = Label(frame_login, text="REGISTER", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(
            x=250, y=30)

        lbl_user = Label(frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=140)
        self.username = Entry(frame_login, text="Username", font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=250, y=170, width=320, height=35)

        lbl_user = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=210)
        self.password = Entry(frame_login, text="Password", font=("Goudy old style", 15), bg="#E7E6E6", show="*")
        self.password.place(x=250, y=240, width=320, height=35)

        lbl_user = Label(frame_login, text="Retype Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=250, y=285)
        self.rpassword = Entry(frame_login, text="rPassword", font=("Goudy old style", 15), bg="#E7E6E6", show="*")
        self.rpassword.place(x=250, y=320, width=320, height=35)

        submit = Button(frame_login, command=self.check_function, text="REGISTER", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF", fg="white").place(x=250, y=390, width=180, height=40)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "" or self.rpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.password.get() != self.rpassword.get():
            messagebox.showerror("Error", "Password doesn't match", parent=self.root)
            self.password.delete(0, 'end')
            self.rpassword.delete(0, 'end')
        else:
            pname = self.username.get();
            ppass = self.password.get();
            con = mysql.connect(host="localhost", user="root", password="", database="hospital")
            cursor = con.cursor()
            sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
            val = (pname, ppass)
            cursor.execute(sql, val)
            cursor.execute("commit");
            self.username.delete(0, 'end')
            self.password.delete(0, 'end')
            self.rpassword.delete(0, 'end')
            messagebox.showinfo("Details Status", "Registered sucessfully")
            root.after(6000, Login(root))
            con.close();

class SecondPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Second page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)

        frame_second = Frame(self.root, bg="white")
        frame_second.place(x=400, y=100, width=800, height=600)

        frame_inner = Frame(self.root, bg="white")
        frame_inner.place(x=700, y=280, width=150, height=150)

        title = Label(frame_second, text="Doctor's available timings", font=("Impact", 35, "bold"), fg="#6162FF",
                      bg="white").place(
            x=185, y=30)
        subtitle = Label(frame_second, text="Appointment time", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                         bg="white").place(x=250, y=100)

        v = tk.IntVar()
        con = mysql.connect(host="localhost", user="root", password="", database="hospital")
        cursor = con.cursor()
        cursor.execute("select time1,time2,time3 from doctor")
        records = cursor.fetchall()
        tk.Label(frame_inner,
                 text="""Select a timing""",
                 justify=tk.LEFT, padx=20, font=("Goudy old style", 15), bg="white").pack()
        i = 0


        for row in records:
            for i in range(0, 3):
                tk.Radiobutton(frame_inner,
                               text=row[i],
                               padx=20,
                               variable=v,
                               value=i,command=self.changeval, font=("Goudy old style", 15), bg="white").pack(anchor=tk.W)
                i += 1
                self.v=v
        con.close()

        next1 = Button(frame_second, command=self.next_page, text="NEXT", bd=0, font=("Goudy old style", 15),
                       bg="#6162FF", fg="white").place(x=420, y=400, width=180, height=40)
        next2 = Button(frame_second, command=self.prev_page, text="LOGOUT", bd=0, font=("Goudy old style", 15),
                       bg="#6162FF", fg="white").place(x=220, y=400, width=180, height=40)
    def changeval(self):
        self.val = self.v.get()

    def prev_page(self):
        c = 1
        if c == 1:
            root.after(3000, Login(root))
    def next_page(self):
        c = 1
        radio=self.val
        if c == 1:
            root.after(6000, ThirdPage(root,radio))


class ThirdPage:
    def __init__(self, root,radio):
        self.root = root
        self.radio=radio
        self.root.title("Third Page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        frame_third = Frame(self.root, bg="white")
        frame_third.place(x=400, y=100, width=800, height=600)
        title = Label(frame_third, text="Patient Details", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(
            x=250, y=30)
        lbl_user = Label(frame_third, text="Name", font=("Goudy old style", 20, "bold"), fg="gray", bg="white").place(
            x=100, y=140)
        self.name = Entry(frame_third, text="name", font=("Goudy old style", 15), bg="#E7E6E6")
        self.name.place(x=300, y=140, width=300, height=35)

        lbl_age = Label(frame_third, text="Age", font=("Goudy old style", 20, "bold"), fg="gray", bg="white").place(
            x=100, y=200)
        self.age = Entry(frame_third, text="age", font=("Goudy old style", 15), bg="#E7E6E6")
        self.age.place(x=300, y=200, width=300, height=35)

        lbl_phone = Label(frame_third, text="Phone number", font=("Goudy old style", 20, "bold"), fg="gray",
                          bg="white").place(
            x=100, y=260)
        self.phone = Entry(frame_third, text="Phone number", font=("Goudy old style", 15), bg="#E7E6E6")
        self.phone.place(x=300, y=260, width=300, height=35)

        lbl_gender = Label(frame_third, text="Gender", font=("Goudy old style", 20, "bold"), fg="gray",
                           bg="white").place(
            x=100, y=320)
        self.gender = Entry(frame_third, text="gender", font=("Goudy old style", 15), bg="#E7E6E6")
        self.gender.place(x=300, y=320, width=300, height=35)

        lbl_address = Label(frame_third, text="Address", font=("Goudy old style", 20, "bold"), fg="gray",
                            bg="white").place(x=100, y=440)
        self.address = Entry(frame_third, text="address", font=("Goudy old style", 15), bg="#E7E6E6")
        self.address.place(x=300, y=440, width=300, height=50)

        lbl_mail = Label(frame_third, text="E-mail", font=("Goudy old style", 20, "bold"), fg="gray",
                         bg="white").place(x=100, y=380)
        self.mail = Entry(frame_third, text="mail", font=("Goudy old style", 15), bg="#E7E6E6")
        self.mail.place(x=300, y=380, width=300, height=35)

        next1 = Button(frame_third, command=self.prev_page, text="BACK", bd=0, font=("Goudy old style", 15),
                       bg="#6162FF", fg="white").place(x=200, y=520, width=180, height=40)
        submit = Button(frame_third, command=self.insert, text="SUBMIT", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF", fg="white").place(x=400, y=520, width=180, height=40)

    def prev_page(self):
        c = 1
        if c == 1:
            root.after(6000, SecondPage(root))

    def insert(self):
        pname = self.name.get();
        page = self.age.get();
        pgender = self.gender.get();
        pphone = self.phone.get();
        paddress = self.address.get();
        pmail=self.mail.get()
        radio=self.radio

        if (pname == "" or page == "" or pgender == "" or pphone == "" or paddress == "" or pmail==""):
            messagebox.showerror("Error", "All fields are required")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="hospital")
            cursor = con.cursor()
            if radio==0:
                cursor.execute("SELECT time1 FROM doctor")
            elif radio==1:
                cursor.execute("SELECT time2 FROM doctor")
            else:
                cursor.execute("SELECT time3 FROM doctor")
            appointment=cursor.fetchall()
            pappoint=appointment[0][0]

            sql="INSERT INTO patient (pname, page, pgender, pphone, paddress,pappoint,pmail) VALUES (%s, %s,%s,%s,%s,%s,%s)"
            val=(pname, page, pgender, pphone, paddress,pappoint,pmail)
            cursor.execute(sql, val)
            cursor.execute("commit");
            self.name.delete(0, 'end')
            self.age.delete(0, 'end')
            self.gender.delete(0, 'end')
            self.phone.delete(0, 'end')
            self.address.delete(0, 'end')
            self.mail.delete(0,'end')
            messagebox.showinfo("Details Status", "Patient details entered sucessfully")

            root.after(6000, Thank(root))
            con.close();

class Thank:
    def __init__(self,root):
        self.root = root
        self.root.title("Thank")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        frame_thank = Frame(self.root, bg="white")
        frame_thank.place(x=400, y=100, width=800, height=600)
        title = Label(frame_thank, text="THANK YOU", font=("Impact", 40, "bold"), fg="#6162FF", bg="white").place(
            x=270, y=50)
        title = Label(frame_thank, text="Please be on time, if you can't please inform us", font=("Helvetica", 20), fg="black", bg="white").place(
            x=150, y=200)
        title = Label(frame_thank, text="For Queries contact us:+919887766554", font=("Helvetica", 20),
                      fg="black", bg="white").place(
            x=150, y=300)
        next1 = Button(frame_thank, command=self.prev_page, text="LOGOUT", bd=0, font=("Goudy old style", 15),
                       bg="#6162FF", fg="white").place(x=300, y=400, width=180, height=40)

    def prev_page(self):
        c = 1
        if c == 1:
            root.after(3000, Login(root))

class Doctor1:
    def __init__(self, root):
        self.root = root
        self.root.title("Second page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        frame_d1 = Frame(self.root, bg="white")
        frame_d1.place(x=400, y=100, width=800, height=600)

        title1 = Label(frame_d1, text="Update your availability time", font=("Impact", 35, "bold"), fg="#6162FF",
                       bg="white").place(
            x=150, y=30)

        title2 = Label(frame_d1, text="View patient details", font=("Impact", 35, "bold"), fg="#6162FF",
                       bg="white").place(x=210, y=250)

        toUpdate = Button(frame_d1, command=self.time1, text="UPDATE", bd=0, font=("Goudy old style", 15),
                          bg="#6162FF", fg="white").place(x=300, y=150, width=180, height=40)

        report = Button(frame_d1, command=self.report, text="REPORT", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF", fg="white").place(x=300, y=370, width=180, height=40)
        next1 = Button(frame_d1, command=self.prev_page, text="LOGOUT", bd=0, font=("Goudy old style", 15),
                       bg="#6162FF", fg="white").place(x=300, y=450, width=180, height=40)

    def prev_page(self):
        c = 1
        if c == 1:
            root.after(3000, Login(root))
    def time1(self):
        root.after(2000, timing(root))

    def report(self):
        root.after(2000, Doctor3(root))


class timing:
    def __init__(self, root):
        self.root = root
        self.root.title("Second page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        frame_d2 = Frame(self.root, bg="white")
        frame_d2.place(x=400, y=100, width=800, height=600)

        title1 = Label(frame_d2, text="Update your availability time", font=("Impact", 35, "bold"), fg="#6162FF",
                       bg="white").place(
            x=150, y=30)
        t1 = Label(frame_d2, text="Time 1", font=("Goudy old style", 20, "bold"), fg="gray", bg="white").place(
            x=100, y=140)
        self.t1 = Entry(frame_d2, text="Timing1", font=("Goudy old style", 15), bg="#E7E6E6")
        self.t1.place(x=300, y=140, width=300, height=35)

        t2 = Label(frame_d2, text="Time 2", font=("Goudy old style", 20, "bold"), fg="gray", bg="white").place(
            x=100, y=200)
        self.t2 = Entry(frame_d2, text="Timing2", font=("Goudy old style", 15), bg="#E7E6E6")
        self.t2.place(x=300, y=200, width=300, height=35)

        t3 = Label(frame_d2, text="Time 3", font=("Goudy old style", 20, "bold"), fg="gray",
                   bg="white").place(
            x=100, y=260)
        self.t3 = Entry(frame_d2, text="Timing3", font=("Goudy old style", 15), bg="#E7E6E6")
        self.t3.place(x=300, y=260, width=300, height=35)
        toUpdate = Button(frame_d2, command=self.insert, text="UPDATE", bd=0, font=("Goudy old style", 15),
                          bg="#6162FF", fg="white").place(x=450, y=350, width=180, height=40)
        back = Button(frame_d2, command=self.back, text="BACK", bd=0, font=("Goudy old style", 15),
                      bg="#6162FF", fg="white").place(x=250, y=350, width=180, height=40)

    def back(self):
        c = 1
        if c == 1:
            root.after(2000, Doctor1(root))

    def insert(self):
        time1 = self.t1.get();
        time2 = self.t2.get();
        time3 = self.t3.get();
        if (time1 == "" or time2 == "" or time3 == ""):
            messagebox.showerror("Error", "All fields are required")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="hospital")
            cursor = con.cursor()
            cursor.execute(
                "UPDATE doctor SET time1='" + time1 + "',time2='" + time2 + "',time3='" + time3 + "' ");
            cursor.execute("commit");
            messagebox.showinfo("Details Status", " Timings updated sucessfully")
            con.close();


class Doctor3:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient details")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        frame_doc3 = Frame(self.root, bg="white")
        frame_inner = Frame(self.root, bg="white")
        frame_doc3.place(x=400, y=100, width=800, height=600)
        frame_inner.place(x=450, y=200, width=650, height=400)
        title = Label(frame_doc3, text="Patient Details", font=("Impact", 25, "bold"), fg="#6162FF", bg="white").place(
            x=250, y=30)
        con = mysql.connect(host="localhost", user="root", password="", database="hospital")
        cursor = con.cursor()
        cursor.execute("select pname,page,pappoint from patient")
        records = cursor.fetchall()
        self.tree = ttk.Treeview(frame_inner, column=("c1", "c2", "c3"), show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Name")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Age")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Appointment Time")

        self.tree.pack()

        for row in records:
            self.tree.insert("", tk.END, values=row)
        con.close()

        report = Button(frame_doc3, command=self.show_selected, text='GENERATE REPORT', bd=0, font=("Goudy old style", 12),
                       bg="#6162FF", fg="white").place(x=450, y=500, width=180, height=40)
        back = Button(frame_doc3, command=self.back, text="BACK", bd=0, font=("Goudy old style", 12),
                      bg="#6162FF", fg="white").place(x=200, y=500, width=180, height=40)

    def show_selected(self):
        value = self.tree.selection()
        self.pid=(value[0][3])
        root.after(2000, Report(root, self.pid))
    def back(self):
        c = 1
        if c == 1:
            root.after(2000, Doctor1(root))


class Report:
    def __init__(self, root, pid):
        self.pid = pid;
        self.root = root
        self.root.title("Report Generation")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        frame_report = Frame(self.root, bg="white")
        frame_report.place(x=400, y=100, width=800, height=600)
        con = mysql.connect(host="localhost", user="root", password="", database="hospital")
        cursor = con.cursor()
        cursor.execute("select pname,page from patient where pid='" + self.pid + "'")
        detail = cursor.fetchall()


        pname = Label(frame_report, text="Patient Name:", font=("Goudy old style", 14, "bold"), fg="black",
                      bg="white").place(
            x=150, y=30)
        name = Label(frame_report, text=detail[0][0], font=("Goudy old style", 14, "bold"), fg="black",
                     bg="white").place(
            x=280, y=30)
        page = Label(frame_report, text="Patient Age:", font=("Goudy old style", 14, "bold"), fg="black",
                     bg="white").place(x=450, y=30)
        age = Label(frame_report, text=detail[0][1], font=("Goudy old style", 14, "bold"), fg="black",
                    bg="white").place(
            x=550, y=30)
        page = Label(frame_report, text="Medical report", font=("Goudy old style", 16, "bold"), fg="black",
                     bg="white").place(x=150, y=70)
        con.close()
        back = Button(frame_report, command=self.back, text="CANCEL", bd=0, font=("Goudy old style", 15),
                      bg="#6162FF", fg="white").place(x=200, y=520, width=180, height=40)
        sendmail = Button(frame_report, command=self.mail, text="SEND MAIL", bd=0, font=("Goudy old style", 15),
                          bg="#6162FF", fg="white").place(x=420, y=520, width=180, height=40)
        self.text_area = scrolledtext.ScrolledText(frame_report,
                                                   wrap=tk.WORD,
                                                   width=80,
                                                   height=22,
                                                   font=("Times New Roman",
                                                         10))
        self.text_area.place(x=150, y=100)
    def back(self):
        c = 1
        if c == 1:
            root.after(2000, Doctor3(root))
    def mail(self):
        result = self.text_area.get("1.0", tk.END)
        print(result)
        result1 = result.encode('ascii', 'ignore')
        con = mysql.connect(host="localhost", user="root", password="", database="hospital")
        cursor = con.cursor()
        cursor.execute("select pmail from patient where pid='" + self.pid + "'")
        mailid = cursor.fetchall()
        con.close()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("sankarannamalai01@gmail.com", "muthumani123")
        server.sendmail("sankarannamalai01@gmail.com", mailid[0][0], result1)
        server.quit()
        messagebox.showinfo("Sucess", "Mail sent sucessfully")
        root.after(2000, Doctor3(root))
root = Tk()
obj = Login(root)
root.mainloop()