from logging import root
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def  __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        
        
        title=Label(self.root,text="STUDENT  MANAGEMENT  SYSTEM",font=("time new roman",30,"bold"),bg="skyblue",fg="black")
        title.pack(side=TOP)
        
        
        
        
        #all variables

        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.address_var=StringVar()
        
        
        self.search_by=StringVar()
        self.search_txt=StringVar()

        

        #MANAGE FRAME
        Manage_frame=Frame(bd=20,relief=RIDGE,background="white")
        Manage_frame.place(x=10,y=100,width=420,height=540)
        
        
        m_title=Label(Manage_frame,text="MANAGE STUDENTS",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=15)
        
        
        
        #roll

        lbl_roll=Label(Manage_frame,text="Roll No :",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=1,padx=20,sticky="w")
        
        txt_roll=Entry(Manage_frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=1,padx=0,sticky="w")

        
        
        #name

        lbl_name=Label(Manage_frame,text="Name :",font=("times new roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=1,padx=20,sticky="w")
        
        txt_name=Entry(Manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=1,padx=0,sticky="w")
        
        
        #email

        lbl_email=Label(Manage_frame,text="Email :",font=("times new roman",15,"bold"))
        lbl_email.grid(row=3,column=0,pady=1,padx=20,sticky="w")
        
        txt_email=Entry(Manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=1,padx=0,sticky="w")

        
        
        #gendar

        lbl_gender=Label(Manage_frame,text="Gendar :",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=4,column=0,pady=1,padx=20,sticky="w")
        
        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")    
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=1,padx=0,sticky="w")

        
        
        
        #contact

        lbl_contact=Label(Manage_frame,text="Contact :",font=("times new roman",15,"bold"))
        lbl_contact.grid(row=5,column=0,pady=1,padx=20,sticky="w")
        
        txt_contact=Entry(Manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=1,padx=0,sticky="w")
        
        
        #date of birth

        lbl_dob=Label(Manage_frame,text="Date Of Birth :",font=("times new roman",15,"bold"))
        lbl_dob.grid(row=6,column=0,pady=1,padx=20,sticky="w")
        
        txt_dob=Entry(Manage_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=1,padx=0,sticky="w")
        
        
        #address

        lbl_address=Label(Manage_frame,text="Address :",font=("times new roman",15,"bold"))
        lbl_address.grid(row=7,column=0,pady=1,padx=20,sticky="w")
        
        self.txt_address=Text(Manage_frame,bd=4,width=25,height=5,font=("arial",11,"bold"))
        self.txt_address.grid(row=7,column=1,pady=1,padx=0,sticky="w")
        
        
        #button frame

        addbtn_frame=Frame(bd=10,relief=RIDGE,background="blue")
        addbtn_frame.place(x=33,y=550,width=90,height=45)
        btn=Button(addbtn_frame,text="Add",width=8,command=self.add_students).grid(row=0,column=0,padx=1)
        
        updatebtn_frame=Frame(bd=10,relief=RIDGE,background="blue")
        updatebtn_frame.place(x=127,y=550,width=90,height=45)
        btn=Button(updatebtn_frame,text="Update",width=8,command=self.update_data).grid(row=0,column=1,padx=1)

        deletebtn_frame=Frame(bd=10,relief=RIDGE,background="blue")
        deletebtn_frame.place(x=221,y=550,width=90,height=45)
        btn=Button(deletebtn_frame,text="Delete",width=8,command=self.delete_data).grid(row=0,column=2,padx=1)

        clearbtn_frame=Frame(bd=10,relief=RIDGE,background="blue")
        clearbtn_frame.place(x=315,y=550,width=90,height=45)
        btn=Button(clearbtn_frame,text="Clear",width=8,command=self.clear).grid(row=0,column=3,padx=1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        #detail frame
        detail_frame=Frame(bd=20,relief=RIDGE,background="black")
        detail_frame.place(x=450,y=100,width=820,height=540)
        
        
        
        lbl_search=Label(detail_frame,text="Search by:",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=3,pady=15,padx=20,sticky="w")
        

            
        combo_Search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")    
        combo_Search['values']=("Roll_No","Name","Contact")
        combo_Search.grid(row=0,column=4,pady=15,padx=10,sticky="w")
        
        
        

        txt_search=Entry(detail_frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=9,pady=1,padx=0,sticky="w")



        searchbtn=Button(detail_frame,text="Search",width=10,command=self.search_data).grid(row=0,column=19,padx=10,pady=10)
        showallbtn=Button(detail_frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=27,padx=10,pady=10)
        
        
        
        
        #TABLE FRAME

        Table_frame=Frame(detail_frame,bd=10,relief=RIDGE,background="silver")
        Table_frame.place(x=1,y=79,height=419,width=779)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_frame,columns=("roll_no","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        
        self.Student_table.heading("roll_no",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="Date Of Birth")
        self.Student_table.heading("address",text="Address")
        
        self.Student_table['show']='headings'
        
        
        self.Student_table.column("roll_no",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
        
        

        self.fetch_data()
        
        
        
        
        
    def add_students(self):

        if self.roll_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "All fields are required!!!")
        else:

            con=pymysql.connect(host="localhost",user="root",password="",database="stu")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                               self.name_var.get(),
                                                                               self.email_var.get(),
                                                                               self.gender_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.dob_var.get(),
                                                                               self.txt_address.get('1.0',END)
                                                                               ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")
            
            
            
            
            
            
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stu")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                         self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
        
        
        
        
        
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)
        
        
        
        
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']

        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
        
        
        

    def update_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="stu")
        cur=conn.cursor()
        cur.execute("UPDATE students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                              self.name_var.get(),
                                                                                                              self.email_var.get(),
                                                                                                              self.gender_var.get(),
                                                                                                              self.contact_var.get(),
                                                                                                              self.dob_var.get(),
                                                                                                              self.txt_address.get('1.0',END),
                                                                                                              self.roll_no_var.get()
                                                                                                              
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("Success","Record has been Updated")
            
            
            
            
            
            
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stu")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        rows=cur.fetchall()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success"," Your record hasbeen deleted")
        
        
        
        
        
        
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stu")
        cur=con.cursor()
        
        cur.execute("select * from students where "+str(self.search_by.get())+ " LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
                # messagebox.showinfo("NO","this Roll_No hasn't been inserted yet")
        con.close()
        
        
        
        
        
        
        
        
    
    
root=Tk()
ob=Student(root)
root.mainloop()