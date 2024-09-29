from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Checkbutton
from tkinter import Radiobutton
from tkinter import messagebox
from tkinter import Entry
from tkinter import Frame
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Menu
from tkinter import Variable
from tkinter import StringVar
from tkinter import IntVar
#تیکینتر و اجرا کننده ی ان
screen=Tk()
screen.resizable(True,False)
screen.geometry("%dx%d+%d+%d" % (1000,500,200,200))
screen.title("ثبت نام در دانشگاه")
#function
def OnClickRigester():
    print("tahol is:",tahol.get()) 
    print("din is :",din.get())
    print("meliyat is:",meliyat.get())
    print("jens is :",jens.get())
    print("mofiat:",moafiyat.get())
    name=Name.get()
    famili=Famili.get()
    age=Age.get()
    avrage=Avrage.get()
    Information={"Name":name,"Famili":famili,"Age":age,"Avrage":avrage}
    result=Rigester(Information)
    if result==True:
        listitems=[Name,Famili,Age,Avrage]
        insertDATA(listitems)
        Clear(listitems)
userAll=[]
def Rigester(user):
    if float(user["Avrage"])>=15 and float(user["Avrage"])<=20 and meliyat.get()==1 and moafiyat.get()==1:
        if Exist(user):
            messagebox.showerror("خطا","این داده تکراری است")
            return False
        else:
            userAll.append(user)
            messagebox.showinfo("تبریک ","ثبت نام شما با موفقیت انجام شد")
            return True
    else:
        messagebox.showwarning("توجه","مدارک شما برای ثبت نام کافی نیست")
        return False            
def Exist(value):
    for item in userAll:
        if item["Name"]==value["Name"] and item["Famili"]==value["Famili"] and item["Age"]==value["Age"] and item["Avrage"]==value["Avrage"]:
            return True
    return False    
def insertDATA(value):
    tbl.insert("","end",text="1",values=[Avrage.get(),Age.get(),Famili.get(),Name.get()])    
def Clear(listval):
    for item in listval:
        item.set("")
        TxtName.focus_set()
def GetSelection(event):
    selection_row=tbl.selection()
    if selection_row!=():
        btnEdit.place(x=870,y=188)        
        print(tbl.item(selection_row)['values'])
        Name.set(tbl.item(selection_row)['values'][3])
        Famili.set(tbl.item(selection_row)['values'][2])
        Age.set(tbl.item(selection_row)['values'][1])
        Avrage.set(tbl.item(selection_row)['values'][0])
def OnClickSearch():
    qury=TxtSearch.get()
    result=Search(qury)
    CleanTable()
    LoadDeta(result)
def Search(value):
    list_secend=[]
    for item in userAll:
        if item["Name"]==value or item["Famili"]==value or item["Age"]==value or item["Avrage"]==value:
            list_secend.append(item)
    return list_secend
def CleanTable():
    for item in tbl.get_children():
        sel=str(item)
        tbl.delete(sel)        
def LoadDeta(value):
    for item in value:
        tbl.insert("" ,"end",text="1",values=[item["Name"],item['Famili'],item['Age'],item['Avrage']])
def OnClickDelete():
    result=messagebox.askquestion("حذف","ایا داده مورد نظر را می خواهید حذف کنید")
    print(result) 
    if result=="yes":
        Delete()
def Delete():
    selection_row=tbl.selection()      
    if selection_row != ():
        selectionitem=tbl.item(selection_row)["values"]
        dic={'Name':selectionitem[3],'Famili':selectionitem[2],'Age':str(selectionitem[1]),"Avrage":str(selectionitem[0])}
        tbl.delete(selection_row)
        userAll.remove(dic)
        print(userAll)
def OnClickEdit():
    selection_row=tbl.selection()
    selectionitem=tbl.item(selection_row)["values"]
    dic={'Name':selectionitem[3],'Famili':selectionitem[2],'Age':str(selectionitem[1]),"Avrage":str(selectionitem[0])}
    userindex=userAll.index(dic)    
    print(userindex)
    mydic={'Name':selectionitem[3],'Famili':selectionitem[2],'Age':str(selectionitem[1]),"Avrage":str(selectionitem[0])}
    print("userAll:",userAll)
    print("mydic:",mydic)
    if selection_row!=():
        tbl.item(selection_row,values=[Avrage.get(),Age.get(),Famili.get(),Name.get()])
        listitems=[Name,Famili,Age,Avrage]
        Clear(listitems)        
        btnEdit.place_forget()
                        
def ShowSearch():
    frmSearch.place(x=0,y=0)    
def closeFrm():
    frmSearch.place_forget()    
#frame
frmSearch=Frame(screen,width=400,height=400,background="green")
frmSearch.place(x=0,y=0)
frmSearch.place_forget()
#photoImage
bgSearch=PhotoImage(file="D:/salam/image/graduation-cap.png")
bgClose=PhotoImage(file="D:/salam/image/close.png")
lblBg=Label(frmSearch,text="*",image=bgSearch)
lblBg.place(x=0,y=0)
#.label
lblName=Label(screen,text="نام")
lblName.place(x=930,y=20)
lblFamili=Label(screen,text="نام خانوادگی")
lblFamili.place(x=930,y=60)
lblAge=Label(screen,text="سن")
lblAge.place(x=930,y=100)
lblAvrage=Label(screen,text="معدل")
lblAvrage.place(x=930,y=140)
lblSearch=Label(frmSearch,text="مقدار جستجو")
lblSearch.place(x=0,y=0)
#variable
Name=StringVar()
Famili=StringVar()
Age=StringVar()
Avrage=StringVar()
#def and combobox    
def Getvalue():
    counter=[]
    for item in range(0,21):
        counter.append(item)
    return counter
#Entry
TxtName=Entry(screen,justify="right",textvariable=Name)
TxtName.place(x=770,y=20)
TxtFamili=Entry(screen,justify="right",textvariable=Famili)
TxtFamili.place(x=770,y=60)
TxtAge=Entry(screen,justify="right",textvariable=Age)
TxtAge.place(x=770,y=100)
ComboAvrage=ttk.Combobox(screen,justify="right",textvariable=Avrage)
ComboAvrage.place(x=770,y=140)
ComboAvrage["values"]=Getvalue()
ComboAvrage.current(10)
'''TxtAvrage=Entry(screen,justify="right",textvariable=Avrage)
TxtAvrage.place(x=570,y=140)'''
TxtSearch=Entry(frmSearch,justify="right")
TxtSearch.place(x=70,y=0)
#button
btnRigester=Button(screen,text="ثبت نام",bg="green",fg="black",command=OnClickRigester).place(x=770,y=188)
btnSearch=Button(frmSearch,text="جستجو کنید",command=OnClickSearch).place(x=0,y=30)
btnDelete=Button(screen,text="حذف",justify="right",bg="red",fg="black",command=OnClickDelete)
btnDelete.place(x=825,y=188)
btnEdit=Button(screen,text="ویرایش",justify="right",bg="orange",fg="black",command=OnClickEdit)
#btnEdit.place(x=870,y=188)
btnFrmSearch=Button(screen,text="نمایش جستجو",command=ShowSearch)
btnFrmSearch.place(x=770,y=160)
btnFrmClose=Button(frmSearch,text="*",bg="black",fg="white",command=closeFrm,image=bgClose)
btnFrmClose.place(x=330,y=0)
#checkButton and chek_gharamani
chek1=IntVar()
chek_gharamani1=IntVar()
chek_gharamani2=IntVar()
chek_gharamani3=IntVar()
chek2=IntVar()
chek3=IntVar()
check=Checkbutton(screen,text="سابقه قهرمانی",variable=chek1).place(x=650,y=250)
check=Checkbutton(screen,text="کشوری",variable=chek_gharamani1).place(x=590,y=250)
check=Checkbutton(screen,text="اسیایی",variable=chek_gharamani2).place(x=530,y=250)
check=Checkbutton(screen,text="جهانی",variable=chek_gharamani3).place(x=470,y=250)
#نوع شغل
check=Checkbutton(screen,text="شاغل",variable=chek2).place(x=680,y=300)
shoghl=IntVar()
shoghlDolati=Radiobutton(screen,text="دولتی",variable=shoghl,value=1).place(x=620,y=300)
shoghlAzad=Radiobutton(screen,text="ازاد",variable=shoghl,value=2).place(x=570,y=300)
#برای مردها معافیت داشتن
moafiyat=IntVar()
Dashtan_moafiat=Radiobutton(screen,text="داشتن معافیت",variable=moafiyat,value=1).place(x=640,y=350)
FaghedSharayet=Radiobutton(screen,text="فاقد معافیت ",variable=moafiyat,value=2).place(x=550,y=350)
#radiobutton
tahol=IntVar()
Maghtae_tahsili=IntVar()
din=IntVar()
jens=IntVar()
meliyat=IntVar()
#زن یا مرد بودن    
radio_mard=Radiobutton(screen,text="اقا",variable=jens,value=2).place(x=670,y=0)
radio_zan=Radiobutton(screen,text="خانم",variable=jens,value=1).place(x=710,y=0)
#مجرد بودن یا متاهل بودنl
radio_mojard=Radiobutton(screen,text="مجرد",variable=tahol,value=1).place(x=650,y=50)
radio_Motahel=Radiobutton(screen,text="متاهل",variable=tahol,value=2).place(x=710,y=50)
#ملیت
radio_irani=Radiobutton(screen,text="ایرانی",variable=meliyat,value=1).place(x=710,y=100)
radio_Ghyre_irani=Radiobutton(screen,text="غیر ایرانی",variable=meliyat,value=2).place(x=640,y=100)
#پیروان ادیان
raddio_shie=Radiobutton(screen,text="شیعه",variable=din,value=1).place(x=710,y=150)
raddio_soni=Radiobutton(screen,text="سنی",variable=din,value=2).place(x=660,y=150)
raddio_masihi=Radiobutton(screen,text="مسیحی",variable=din,value=3).place(x=600,y=150)
raddio_yahoodi=Radiobutton(screen,text="یهودی",variable=din,value=4).place(x=540,y=150)
raddio_zartoshti=Radiobutton(screen,text="زرتشتی",variable=din,value=5).place(x=480,y=150)
raddio_sayeradyan=Radiobutton(screen,text="سایرادیان",variable=din,value=6).place(x=410,y=150)
#مقطعه تحصیلی
radio_Kardani=Radiobutton(screen,text="کاردانی",variable=Maghtae_tahsili,value=1).place(x=700,y=200)
radio_Karshenasi=Radiobutton(screen,text="کارشناسی",variable=Maghtae_tahsili,value=2).place(x=630,y=200)
radio_KarshenasiArshad=Radiobutton(screen,text="کارشناسی ارشد",variable=Maghtae_tahsili,value=3).place(x=530,y=200)
radio_Doctora=Radiobutton(screen,text="دکترا",variable=Maghtae_tahsili,value=4).place(x=470,y=200)
#نمودارهای درختی و سطر و ستون
tbl=ttk.Treeview(screen,show="headings",columns=("c1","c2","c3","c4"),height=50)
tbl.column("# 1",width=50)
tbl.column("# 2",width=50)
tbl.column("# 3",width=50)
tbl.column("# 4",width=50)
tbl.heading("# 1",text="معدل")
tbl.heading("# 2",text="سن")
tbl.heading("# 3",text="نام خانوادگی")
tbl.heading("# 4",text="نام")
tbl.place(x=770,y=220)
tbl.bind("<Button-1>",GetSelection)
#def menu
def PRT():
    print("klick shod")
def money_situation():
    print("dar hal baresi")
def Term():
    print("welcome be term jadid")    
def communication():
    print("lotfan montazer bemanid")
#Mene
menoRigester=Menu(screen)
userMenu=Menu(menoRigester,tearoff=0)
userMenu.add_command(label="ثبت نام دانشجو",command=PRT)
userMenu.add_command(label="افزودن دانشجو",command=PRT)
userMenu.add_separator()
userMenu.add_command(label="اخراج دانشجو",command=PRT,background="black",foreground="white")
menoRigester.add_cascade(label="دانشجو",menu=userMenu)
MenuGetmony=Menu(menoRigester,tearoff=0)
MenuGetmony.add_command(label="شهریه",command=money_situation)
MenuGetmony.add_command(label="بدهی",command=money_situation)
MenuGetmony.add_separator()
MenuGetmony.add_command(label="تسویه",command=money_situation,background="green")
menoRigester.add_cascade(label="وضیعت پرداختها",menu=MenuGetmony)
MenuTerm=Menu(menoRigester,tearoff=0)
MenuTerm.add_command(label="نیم سال اول تحصیلی",command=Term)
MenuTerm.add_command(label="نیم سال دوم تحصیلی",command=Term)
MenuTerm.add_separator()
MenuTerm.add_command(label='ترم تابستانه',command=Term,background="red")
menoRigester.add_cascade(label="ترم",menu=MenuTerm)
MenoSection=Menu(menoRigester,tearoff=0)
MenoSection.add_command(label="واحد مدیریت",command=communication)
MenoSection.add_command(label="واحد اموزش",command=communication)
MenoSection.add_command(label="معاونت",command=communication)
MenoSection.add_command(label="حراست",command=communication)
MenoSection.add_command(label="شورا",command=communication)
MenoSection.add_command(label="فارغ تحصیلان",command=communication)
MenoSection.add_command(label="دبیر خانه",command=communication)
menoRigester.add_cascade(label="محیط اداری",menu=MenoSection)
screen.config(menu=menoRigester)
screen.mainloop()