#HAZIRLAYANLAR
#385173 - Emre DEMİR
#385215 - Burak ŞENTÜRK
#385228 - Orhan Enes KILIÇ

from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import shutil
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import smtplib
import time

ekran=Tk()
ekran.title("RANDEVU SİSTEMİ")
ekran.state("zoomed")

vertab = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="farabirandevu"
)

mycursor = vertab.cursor(buffered=True)
sondeg = 0

#resim
resim1 = Image.open("ktuus.png")
yukle = ImageTk.PhotoImage(resim1)
goruntu1 = Label(ekran,image=yukle)
goruntu1.image = yukle
goruntu1.place(x=0, y=0)

def giris():
    ekran2 = Toplevel(ekran)
    ekran2.state("zoomed")
    ekran2.title("KTÜ FARABİ HASTANESİ HASTA BİLGİLERİ")

    resim2 = Image.open("ktuus.png")
    yukle2 = ImageTk.PhotoImage(resim2)
    goruntu2 = Label(ekran2, image=yukle2)
    goruntu2.image = yukle2
    goruntu2.place(x=0, y=0)
    
    #tc
    tc= Label(ekran2,text="T.C. Kimlik No:")
    tc.place(x=500, y=350)
    tc.config(font=("Arial", 12, "bold"),width=15,background="Light Goldenrod")

    tc1 = Entry(ekran2, width=25,font=("Arial", 12, "italic"),background="#E3F2FD")
    tc1.place(x=670, y=350)

    #şifre
    sifre= Label(ekran2,text="Şifrenizi Giriniz:")
    sifre.place(x=500, y=400)
    sifre.config(font=("Arial", 12, "bold"),width=15,background="Light Goldenrod")

    sifre1 = Entry(ekran2, width=25,font=("Arial", 12, "italic"),show="*",background="#E3F2FD")
    sifre1.place(x=670, y=400)

    def sorgu():
        def kullanici_giris(kisi):
            mycursor=vertab.cursor()
            mycursor.execute("select * from kullanici where tc=%s and sifre=%s",kisi)
            return (mycursor.fetchall())
        verigiris=(
            tc1.get(),
            sifre1.get())

        if tc1.get() == "":
            messagebox.showinfo("UYARI","Tc Giriniz")
        elif sifre1.get() == "":
            messagebox.showinfo("UYARI","Şifre giriniz")
        else:
            res=kullanici_giris(verigiris)
            if res:
                messagebox.showinfo("BİLGİ","Giriş Başarılı")
                anasayfa()
            else:
                messagebox.showinfo("UYARI","Tc ve Şifre hatalı")

    def anasayfa():
        ekran4=Toplevel(ekran)
        ekran4.title("RANDEVU SİSTEMİ")
        ekran4.state("zoomed")

        #Resim
        resim4 = Image.open("ktuuic.png")
        yukle4 = ImageTk.PhotoImage(resim4)
        goruntu4 = Label(ekran4,text="Adam", image=yukle4)
        goruntu4.image = yukle4
        goruntu4.place(x=0, y=0)

        b= StringVar()
        

        def hesap_bilgilerim_butonlar():
            ekran5 = Toplevel(ekran)
            ekran5.state("zoomed")
            ekran5.title("KTÜ FARABİ HASTANESİ HASTA BİLGİLERİ")

            resim5 = Image.open("ktuus.png")
            yukle5 = ImageTk.PhotoImage(resim5)
            goruntu5 = Label(ekran5, image=yukle5)
            goruntu5.image = yukle5
            goruntu5.place(x=0, y=0)

            def hesap_bilgilerim():
                ekran6 = Toplevel(ekran)
                ekran6.geometry("750x700+300+0")
                ekran6.title("KTÜ FARABİ HASTANESİ HASTA BİLGİLERİ")

                resim6 = Image.open("ktuuic2.png")
                yukle6 = ImageTk.PhotoImage(resim6)
                goruntu6 = Label(ekran6, image=yukle6)
                goruntu6.image = yukle6
                goruntu6.place(x=0, y=0)

                hbilgi2= Label(ekran6,text="  Hesap Bilgilerim")
                hbilgi2.place(x=50, y=200,height=40,width=150)
                hbilgi2.config(font=("Arial", 12, "bold"),background="#e9afaf")

                def bagla():
                    global sonuclar
                    global sorgu6
                    mycursor = vertab.cursor()
                    sorgu6 = "SELECT tc,adsoyad,tel,cinsiyet,sifre FROM kullanici where tc="+tc1.get()

                    mycursor.execute(sorgu6)

                    sonuclar = mycursor.fetchall()

                bagla()
                                                
                tree1 = ttk.Treeview(ekran6)
                tree1.config(height=10)

                tree1["columns"] = ("Tc Kimlik","Adınız Soyadınız", "Telefon Numaranız", "Cinsiyetiniz","Şifreniz")
                tree1.column("#0", width=1,anchor='sw')
                tree1.column("Tc Kimlik", width=110,anchor='sw')
                tree1.column("Adınız Soyadınız", width=110,anchor='sw')
                tree1.column("Telefon Numaranız", width=110,anchor='sw')
                tree1.column("Cinsiyetiniz", width=90,anchor='sw')
                tree1.column("Şifreniz", width=100,anchor='sw')
                
                tree1.heading("#0", text="",anchor='sw')
                tree1.heading("Tc Kimlik", text="Tc Kimlik ",anchor='sw')
                tree1.heading("Adınız Soyadınız", text="Adınız Soyadınız",anchor='sw')
                tree1.heading("Telefon Numaranız", text="Telefon Numaranız",anchor='sw')
                tree1.heading("Cinsiyetiniz", text="Cinsiyetiniz",anchor='sw')
                tree1.heading("Şifreniz", text="Şifreniz",anchor='sw')

                for satir in range(len(sonuclar)):
                    for sutun in range(1):
                        tree1.insert("", 0, values=(sonuclar[satir]))
                tree1.place(x=200,y=200)



            def sifredegistir():
                ekran7 = Toplevel(ekran)
                ekran7.geometry("750x700+300+0")
                ekran7.title("KTÜ FARABİ HASTANESİ HASTA BİLGİLERİ")

                resim7 = Image.open("ktuuic2.png")
                yukle7 = ImageTk.PhotoImage(resim7)
                goruntu7 = Label(ekran7, image=yukle7)
                goruntu7.image = yukle7
                goruntu7.place(x=0, y=0)

                hbilgi2= Label(ekran7,text="Şifre Değiştirme")
                hbilgi2.place(x=50, y=200,height=40,width=150)
                hbilgi2.config(font=("Arial", 12, "bold"),background="#e9afaf")

                #eskiparola
                ep= tk.Label(ekran7,text="Parolanız:")
                ep.place(x=250, y=210)
                ep.config(font=("Arial", 12, "bold"),width=20,background="Light Goldenrod")

                ep1 = Entry(ekran7, width=25,font=("Arial", 12, "italic"),show="*",background="#E3F2FD")
                ep1.place(x=470, y=210)
                #yeniparola
                yp= tk.Label(ekran7,text="Yeni Parolanız:")
                yp.place(x=250, y=250)
                yp.config(font=("Arial", 12, "bold"),width=20,background="Light Goldenrod")

                yp1 = Entry(ekran7, width=25,font=("Arial", 12, "italic"),show="*",background="#E3F2FD")
                yp1.place(x=470, y=250)
                #yeniparola(Tekrar)
                ypt= tk.Label(ekran7,text="Yeni Parolanız(Tekrar):")
                ypt.place(x=250, y=290)
                ypt.config(font=("Arial", 12, "bold"),width=20,background="Light Goldenrod")

                ypt1 = Entry(ekran7, width=25,font=("Arial", 12, "italic"),show="*",background="#E3F2FD")
                ypt1.place(x=470, y=290)

                def sifredegistirmevt():
                    mycursor = vertab.cursor()
                    

                    if ep1.get() == "":
                        messagebox.showinfo("UYARI","Şifrenizi Giriniz.")
                        sifredegistir()
                    elif ep1.get()!= sifre1.get():
                        messagebox.showinfo("UYARI","Şifrenizi Yanlış Girdiniz.")
                        sifredegistir()
                    elif yp1.get() == "":
                        messagebox.showinfo("UYARI","Yeni Şifrenizi Giriniz.")
                        sifredegistir()
                    elif ypt1.get() == "":
                        messagebox.showinfo("UYARI","Yeni Şifre Tekrarını Giriniz.")
                        sifredegistir()
                    elif yp1.get()!=ypt1.get():
                        messagebox.showinfo("UYARI","Yeni Şifreler Uyuşmamakta.")
                        sifredegistir()
                    else:
                        mycursor.execute("UPDATE kullanici SET sifre = %s WHERE tc = %s and sifre = %s;", (yp1.get(), tc1.get(),sifre1.get()))

                        vertab.commit()
                        res=(sifredegistirmevt)
                        if res:
                            messagebox.showinfo("BİLGİ","Şifreniz Başarılı Bir Şekilde Değiştirildi.")
                            sifredegistir()
                        else:
                            messagebox.showinfo("UYARI","Hata Oluştu")
                            sifredegistir()
                
                #buton
                sb=tk.Button(ekran7,text="Kaydet",command=sifredegistirmevt,width=30,bg="#FFEB3B",activebackground="#FDD835")
                sb.place(x=300,y=350)

                
            #butonlar
            buton1=tk.Button(ekran5,text="Bilgilerim",command=hesap_bilgilerim,
                            width=50,
                            height=5,
                            bg="#FFEB3B",
                            activebackground="#FDD835")
            buton1.place(x=550,y=350)

            buton2=tk.Button(ekran5,text="Şifre Değiştirme",command=sifredegistir,
                            width=50,
                            height=5,
                            bg="#FFEB3B",
                            activebackground="#FDD835")
            buton2.place(x=550,y=500)


        def randevularım():
            ekran8 = Toplevel(ekran)
            ekran8.geometry("750x700+300+0")
            ekran8.title("KTÜ FARABİ HASTANESİ RANDEVULAR")

            resim8 = Image.open("randevularim.png")
            yukle8 = ImageTk.PhotoImage(resim8)
            goruntu8 = Label(ekran8, image=yukle8)
            goruntu8.image = yukle8
            goruntu8.place(x=0, y=0)

            randevu8= Label(ekran8,text="Randevularım")
            randevu8.place(x=50, y=250,height=40,width=150)
            randevu8.config(font=("Arial", 12, "bold"),background="#e9afaf")

            def vtrandevularım():
                    global son
                    global randevularımsorgu
                    mycursor = vertab.cursor()
                    randevularımsorgu = "SELECT kullanici_tc,tarih,klinik,doktor,saat FROM randevular where kullanici_tc="+tc1.get()

                    mycursor.execute(randevularımsorgu)

                    son = mycursor.fetchall()

            vtrandevularım()
            

            tree1 = ttk.Treeview(ekran8)
            tree1.config(height=20)

            tree1["columns"] = ("Kullanıcı TC","Randevu Tarihi","Klinik Adı","Doktor Adı","Randevu Saati")
            tree1.column("#0", width=1,anchor='sw')
            tree1.column("Kullanıcı TC", width=100,anchor='sw')
            tree1.column("Randevu Tarihi", width=100,anchor='sw')
            tree1.column("Klinik Adı", width=120,anchor='sw')
            tree1.column("Doktor Adı", width=115,anchor='sw')
            tree1.column("Randevu Saati", width=100,anchor='sw')

            tree1.heading("#0", text="",anchor='sw')
            tree1.heading("Kullanıcı TC", text="Kullanıcı TC",anchor='sw')
            tree1.heading("Randevu Tarihi", text="Randevu Tarihi",anchor='sw')
            tree1.heading("Klinik Adı", text="Klinik Adı",anchor='sw')
            tree1.heading("Doktor Adı", text="Doktor Adı",anchor='sw')
            tree1.heading("Randevu Saati", text="Randevu Saati",anchor='sw')
           
            for satir in range(len(son)):
                for sutun in range(1):
                    tree1.insert("", 0, values=(son[satir]))
            tree1.place(x=200,y=200)


        def randevu_gecmisi():
            ekran9 = Toplevel(ekran)
            ekran9.geometry("750x700+300+0")
            ekran9.title("KTÜ FARABİ HASTANESİ RANDEVU GEÇMİŞİ")

            resim9 = Image.open("randevugecmisim.png")
            yukle9 = ImageTk.PhotoImage(resim9)
            goruntu9 = Label(ekran9, image=yukle9)
            goruntu9.image = yukle9
            goruntu9.place(x=0, y=0)

            randevu8= Label(ekran9,text="Randevu Geçmisi")
            randevu8.place(x=50, y=250,height=40,width=150)
            randevu8.config(font=("Arial", 12, "bold"),background="#e9afaf")

            def vtgecmisrandevularım():
                    global son
                    global randevularımsorgu
                    mycursor = vertab.cursor()
                    randevularımsorgu = "SELECT kullanici_tc,tarih,klinik,doktor,saat FROM randevular where kullanici_tc="+tc1.get()

                    mycursor.execute(randevularımsorgu)

                    son = mycursor.fetchall()

            vtgecmisrandevularım()
            

            tree1 = ttk.Treeview(ekran9)
            tree1.config(height=20)

            tree1["columns"] = ("Kullanıcı TC","Randevu Tarihi","Klinik Adı","Doktor Adı","Randevu Saati")
            tree1.column("#0", width=1,anchor='sw')
            tree1.column("Kullanıcı TC", width=100,anchor='sw')
            tree1.column("Randevu Tarihi", width=100,anchor='sw')
            tree1.column("Klinik Adı", width=120,anchor='sw')
            tree1.column("Doktor Adı", width=115,anchor='sw')
            tree1.column("Randevu Saati", width=100,anchor='sw')

            tree1.heading("#0", text="",anchor='sw')
            tree1.heading("Kullanıcı TC", text="Kullanıcı TC",anchor='sw')
            tree1.heading("Randevu Tarihi", text="Randevu Tarihi",anchor='sw')
            tree1.heading("Klinik Adı", text="Klinik Adı",anchor='sw')
            tree1.heading("Doktor Adı", text="Doktor Adı",anchor='sw')
            tree1.heading("Randevu Saati", text="Randevu Saati",anchor='sw')
           
            for satir in range(len(son)):
                for sutun in range(1):
                    tree1.insert("", 0, values=(son[satir]))
            tree1.place(x=200,y=200)
            

        def iletisim():
            ekran10 = Toplevel(ekran)
            ekran10.geometry("750x700+300+0")
            ekran10.title("KTÜ FARABİ HASTANESİ İLETİŞİM FORMU")

            resim10 = Image.open("iletisimic.png")
            yukle10 = ImageTk.PhotoImage(resim10)
            goruntu10 = Label(ekran10, image=yukle10)
            goruntu10.image = yukle10
            goruntu10.place(x=0, y=0)

            #Contact Form
            alici_text=Label(ekran10,text="Alıcı E-posta:")
            alici_text.place(x=100,y=220)
            alici_text.config(font=("Arial", 12, "bold"),background="#6f9191")
            epostaniz_text=Label(ekran10,text="E-postanız:")
            epostaniz_text.place(x=100,y=280)
            epostaniz_text.config(font=("Arial", 12, "bold"),background="#6f9191")
            mesaj_text=Label(ekran10,text="Mesajınız:")
            mesaj_text.place(x=100,y=340)
            mesaj_text.config(font=("Arial", 12, "bold"),background="#6f9191")

            alici=StringVar()
            epostaniz=StringVar()

            alici_entry=Entry(ekran10,textvariable="info@ktu.edu.gov.tr",width="50")
            alici_entry.insert(0,"info@ktu.edu.gov.tr")
            alici_entry.configure(state=DISABLED)
            alici_entry.place(x=230,y=220)
            epostaniz_entry=Entry(ekran10,textvariable="epostaniz",width="50")
            epostaniz_entry.insert(0,"E-postanızı Giriniz")
            epostaniz_entry.place(x=230,y=280)
            mesaj_entry=Entry(ekran10,textvariable="mesaj")
            mesaj_entry.insert(0,"Lütfen Mesajınızı Buraya Yazınız.")
            mesaj_entry.place(x=230,y=340,width=350,height=200)
            
                
            def iletisimal():
                global iletisimsorgu
                mycursor = vertab.cursor()


                print(mycursor.rowcount, "Mesaınız İletildi.")
                if epostaniz_entry.get() == "E-postanızı Giriniz":
                    messagebox.showinfo("UYARI","E-postanızı Girmediniz.")
                    anasayfa()
                elif mesaj_entry.get() == "Lütfen Mesajınızı Buraya Yazınız.":
                    messagebox.showinfo("UYARI","Mesaj Girilmedi.")
                    anasayfa()
                else:
                    iletisimsorgu = "INSERT INTO iletisim (kullanici_tc,kullanici_eposta,mesaj) VALUES (%s,%s,%s)"
                    deger = (tc1.get(), epostaniz_entry.get(), mesaj_entry.get())
                    mycursor.execute(iletisimsorgu, deger)

                    vertab.commit()
                    res=(iletisimal)
                    if res:
                        messagebox.showinfo("BİLGİ","Epostanız Gönderildi.")
                        anasayfa()
                    else:
                        messagebox.showinfo("UYARI","Bi Hata Oluştu")
                        anasayfa()

            yap=tk.Button(ekran10,text="Gönder",command=iletisimal,width=30,bg="#FFEB3B",activebackground="#FDD835")
            yap.place(x=300,y=630)

                        

        #Üst Menüler
        hbilgi101 = tk.Button(ekran4,text="Hesap Bilgilerim", compound=TOP,
                              background="Blue",
                              fg="white",
                              activebackground="#FDD835",
                              command=hesap_bilgilerim_butonlar)
        hbilgi101.place(x=70, y=130, height=50, width=150)


        randevularım = tk.Button(ekran4,text="Randevularım", compound=TOP,
                                 background="Blue",
                                 fg="white",
                                 activebackground="#FDD835",
                                 command=randevularım)
        randevularım.place(x=230, y=130, height=50, width=150)



        randevugecmisim = tk.Button(ekran4,text="Randevu Geçmişim", compound=TOP,
                                    background="Blue",
                                    fg="white",
                                    activebackground="#FDD835",
                                    command=randevu_gecmisi)
        randevugecmisim.place(x=390, y=130, height=50, width=150)



        iletisim = tk.Button(ekran4,text="İletisim", compound=TOP,
                             background="blue",
                             fg="white",
                             activebackground="#FDD835",
                             command=iletisim)
        iletisim.place(x=550, y=130, height=50, width=150)


        dil =Combobox(ekran4, width=7)
        dil['values'] = (
            "Türkçe", "Almanca", "İngilizce")
        dil.place(x=1040, y=130,height=50,width=150)
        dil.current(0)


        cikis = tk.Button(ekran4,text="Çıkış", compound=TOP,
                             background="blue",
                             fg="white",
                             activebackground="#FDD835",
                             command=quit)
        cikis.place(x=1200, y=130, height=50, width=150)

        #Randevu Tarihi Belirleme
        rantar = Label(ekran4, text="Randevu Tarihi", font=("Arial", 12, "bold"), background="Light Goldenrod")
        rantar.place(x=250, y=300)

        combo1 = Combobox(ekran4, width=7)
        combo1['values'] = (
            "Gün", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        combo1.place(x=400, y=300)
        combo1.current(0)
        combo1.config(font=("Arial", 12, "bold"),background="#509CCE")


        combo2 = Combobox(ekran4, width=7)
        combo2['values'] = (
            "Ay", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım",
            "Aralik")
        combo2.place(x=500, y=300)
        combo2.current(0)
        combo2.config(font=("Arial", 12, "bold"),background="#509CCE")


        combo3 = Combobox(ekran4, width=7)
        combo3['values'] = (
            "Yıl", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030")
        combo3.place(x=600, y=300)
        combo3.current(0)
        combo3.config(font=("Arial", 12, "bold"),background="#509CCE")

        #klinik seçimi
        ksec = Label(ekran4, text="Klinik Seçiniz:", font=("Arial", 12, "bold"), background="Light Goldenrod")
        ksec.place(x=250, y=350)


        liste=["Klinikler","Çocuk Sağlığı ve Hastalıkları","Dahiliye - İç Hastalıkları", "Dermatoloji","Kadın Hastalıkları ve Doğum","Kulak Burun Boğaz hastalıkları - KBB"]
        liste2=["Doktorlar"]
        liste3=["Dr.Ahmet Güvenç","Dr.Şafak Ersöz","Dr.Gülçin Yıldız","Dr.Sevim Yılmaz"]
        liste4=["Dr.Mehmet Dinçöz","Dr.Murat Hamdi Övüç","Yrd.Doç.Dr.Burak Şen","Yrd.Dr.Caner Yetişkin"]
        liste5=["Prof.Dr.Emre Bakır","Dr.Sait Atmaca","Dr.Furkan Ay","Dr.Seda Özbakır"]
        liste6=["Op.Dr.Korhan Enis Kalça","Dr.Kerim Can Güven","Dr.Burcu Tekin","Dr.Ramazan İn"]
        liste7=["Dr.Suna Demir","Dr.Emel Temel","Dr.Ayhan Aydın","Dr.Doğukan Batı"]

        def doktor_cek(event):
            if dcinsi.get()=="Çocuk Sağlığı ve Hastalıkları":
                klinik_cek['values']=liste3
            if dcinsi.get()=="Dahiliye - İç Hastalıkları":
                klinik_cek['values']=liste4
            if dcinsi.get()=="Dermatoloji":
                klinik_cek['values']=liste5
            if dcinsi.get()=="Kadın Hastalıkları ve Doğum":
                klinik_cek['values']=liste6
            if dcinsi.get()=="Kulak Burun Boğaz hastalıkları - KBB":
                klinik_cek['values']=liste7
            if dcinsi.get()=="Klinikler":
                klinik_cek['values']=liste2

        dcinsi=ttk.Combobox(ekran4,width=29)
        dcinsi['values']=liste
        dcinsi.bind('<<ComboboxSelected>>', doktor_cek)
        dcinsi.config(font=("Arial", 12, "bold"),background="Light Goldenrod")
        dcinsi.current(0)
        dcinsi.place(x=400,y=350)

        klinik_cek=ttk.Combobox(ekran4,width=29)
        klinik_cek['values']=liste3
        klinik_cek['values']=liste4
        klinik_cek['values']=liste5
        klinik_cek['values']=liste6
        klinik_cek['values']=liste7
        klinik_cek['values']=liste2
        klinik_cek.config(font=("Arial", 12, "bold"),background="#509CCE")
        klinik_cek.current(0)
        klinik_cek.place(x=400,y=400)
    

        #doktor seçimi
        ksec = Label(ekran4, text="Doktor Seçiniz:", font=("Arial", 12, "bold"), background="Light Goldenrod")
        ksec.place(x=250, y=400)

        #saat seçiniz
        rsaat1 = Label(ekran4, text="Saat Seçiniz:")
        rsaat1.place(x=800, y=300)
        rsaat1.config(font=("Arial", 12, "bold"),background="Light Goldenrod")

        rs1 = Radiobutton(ekran4, text="10:00", value="a", variable=b)
        rs1.place(x=925, y=300)

        rs2 = Radiobutton(ekran4, text="11:00", value="b", variable=b)
        rs2.place(x=1000, y=300)

        rs3 = Radiobutton(ekran4, text="12:00", value="c", variable=b)
        rs3.place(x=1075, y=300)

        rs4 = Radiobutton(ekran4, text="13:00", value="d", variable=b)
        rs4.place(x=925, y=350)

        rs5 = Radiobutton(ekran4, text="14:00", value="e", variable=b)
        rs5.place(x=1000, y=350)

        rs6 = Radiobutton(ekran4, text="15:00", value="f", variable=b)
        rs6.place(x=1075, y=350)

        rs7 = Radiobutton(ekran4, text="16:00", value="g", variable=b)
        rs7.place(x=925, y=400)

        rs8 = Radiobutton(ekran4, text="17:00", value="h", variable=b)
        rs8.place(x=1000, y=400)

        rs9 = Radiobutton(ekran4, text="18:00", value="i", variable=b)
        rs9.place(x=1075, y=400)

        rs10 = Radiobutton(ekran4, text="19:00", value="o", variable=b)
        rs10.place(x=925, y=450)

        rs11 = Radiobutton(ekran4, text="20:00", value="p", variable=b)
        rs11.place(x=1000, y=450)

        def randevual():
            global randevusorgu
            global saat
            mycursor = vertab.cursor()

            if b.get() == "a":
                saat = "10:00"
            if b.get() == "b":
                saat = "11:00"
            if b.get() == "c":
                saat = "12:00"
            if b.get() == "d":
                saat = "13:00"
            if b.get() == "e":
                saat = "14:00"
            if b.get() == "f":
                saat = "15:00"
            if b.get() == "g":
                saat = "16:00"
            if b.get() == "h":
                saat = "17:00"
            if b.get() == "i":
                saat = "18:00"
            if b.get() == "o":
                saat = "19:00"
            if b.get() == "p":
                saat = "20:00"
                
                
            if combo1.get() == "Gün":
                messagebox.showinfo("UYARI","Gün Seçiniz.")
                anasayfa()
            elif combo2.get() == "Ay":
                messagebox.showinfo("UYARI","Ay Seçiniz.")
                anasayfa()
            elif combo3.get() == "Yıl":
                messagebox.showinfo("UYARI","Yıl Seçiniz.")
                anasayfa()
            else:
                randevusorgu = "INSERT INTO randevular (kullanici_tc,tarih,klinik,doktor,saat) VALUES (%s,%s,%s,%s,%s)"
                deger = (tc1.get(), combo1.get()+ combo2.get()+ combo3.get(), dcinsi.get(),klinik_cek.get(), saat)
                mycursor.execute(randevusorgu, deger)

                vertab.commit()
                res=(randevual)
                if res:
                    messagebox.showinfo("BİLGİ","Randevu Başarı ile Alındı")
                    anasayfa()
                else:
                    messagebox.showinfo("UYARI","Bilgiler Hatalı")
                    anasayfa()
                

            
        #Button
        buton5=tk.Button(ekran4,text="RANDEVU AL",command= randevual,
                         width=30,
                         height=3,
                         bg="#FFEB3B",
                         activebackground="#FDD835")
        buton5.place(x=650,y=500)

        #saat
        zaman=''
        tiktak=Label(ekran4,font=("Arial",20))
        tiktak.place(x=1240,y=20)
        def saat():
            global zaman
            global tiktak
            zaman2=time.strftime('%H:%M:%S')
            if zaman2 != zaman:
                zaman=zaman2
                tiktak.config(text=zaman2,background="#E3F2FD")
            tiktak.after(50,saat)
        saat()

    #Button
    buton3=tk.Button(ekran2,text="GİRİŞ YAP",command=sorgu,
                  width=30,
                  height=3,
                  bg="#FFEB3B",
                  activebackground="#FDD835")
    buton3.place(x=600,y=460)

def kayit():
    ekran3 = Toplevel(ekran)
    ekran3.state("zoomed")
    ekran3.title("KTÜ FARABİ HASTANESİ HASTA BİLGİLERİ")

    resim3 = Image.open("ktuus.png")
    yukle3 = ImageTk.PhotoImage(resim3)
    goruntu3 = Label(ekran3, image=yukle3)
    goruntu3.image = yukle3
    goruntu3.place(x=0, y=0)

    a = StringVar()
    
    #ad
    ad= tk.Label(ekran3,text="Ad Soyad:")
    ad.place(x=500, y=300)
    ad.config(font=("Arial", 12, "bold"),width=15,background="Light Goldenrod")

    ad1 = Entry(ekran3, width=25,font=("Arial", 12, "italic"),background="#E3F2FD")
    ad1.place(x=670, y=300)
    #tc
    tc= tk.Label(ekran3,text="T.C. Kimlik No:")
    tc.place(x=500, y=350)
    tc.config(font=("Arial", 12, "bold"),width=15,background="Light Goldenrod")

    tc1 = Entry(ekran3, width=25,font=("Arial", 12, "italic"),background="#E3F2FD")
    tc1.place(x=670, y=350)
    #şifre
    sifre= tk.Label(ekran3,text="Şifrenizi Giriniz:")
    sifre.place(x=500, y=400)
    sifre.config(font=("Arial", 12, "bold"),width=15,background="Light Goldenrod")

    sifre1 = Entry(ekran3, width=25,font=("Arial", 12, "italic"),show="*",background="#E3F2FD")
    sifre1.place(x=670, y=400)
    #tel
    tel= tk.Label(ekran3,text="Telefon Numaranız:")
    tel.place(x=500, y=450)
    tel.config(font=("Arial", 12, "bold"),width=15,background="Light Goldenrod")

    tel1 = Entry(ekran3, width=25,font=("Arial", 12, "italic"),background="#E3F2FD")
    tel1.place(x=670, y=450)
    #cinsiyet
    cinsiyet = tk.Label(ekran3, text="Cinsiyetiniz:")
    cinsiyet.place(x=500, y=500)
    cinsiyet.config(font=("Arial", 12, "bold"),width=15,background="Light Goldenrod")

    rd1 = tk.Radiobutton(ekran3,bg="#E3F2FD", text="Erkek", value="xy", variable=a)
    rd1.place(x=670, y=500)

    rd2 = tk.Radiobutton(ekran3,bg="#E3F2FD", text="Kadın", value="xx", variable=a)
    rd2.place(x=740, y=500)

    def veriekle():
        global sorgu3
        global cins
        mycursor = vertab.cursor()

        if a.get() == "xy":
            cins = "Erkek"
        if a.get() == "xx":
            cins = "Kadın"

        sorgu3 = "INSERT INTO kullanici (adsoyad,tc,sifre,tel,cinsiyet) VALUES (%s,%s,%s,%s,%s)"
        deger = (ad1.get(), tc1.get(), sifre1.get(), tel1.get(),cins)
        mycursor.execute(sorgu3, deger)

        vertab.commit()

        print(mycursor.rowcount, "Kayıt İşlemi Tamamlandı.")
        if ad1.get() == "":
            messagebox.showinfo("UYARI","Ad Giriniz")
        elif tc1.get() == "":
            messagebox.showinfo("UYARI","Tc giriniz")
        elif sifre1.get() == "":
            messagebox.showinfo("UYARI","Şifre giriniz")
        elif tel1.get() == "":
            messagebox.showinfo("UYARI","Telefon Numarası giriniz")
        else:
            res=(veriekle)
            if res:
                messagebox.showinfo("BİLGİ","Kayıt Başarılı")
                giris()
            else:
                messagebox.showinfo("UYARI","Bilgiler Hatalı")
    
    #Button
    buton4=tk.Button(ekran3,text="KAYIT OL",command=veriekle,width=30,
                  height=3,
                  bg="#FFEB3B",
                  activebackground="#FDD835")
    buton4.place(x=580,y=580)

#butonlar
buton1=tk.Button(text="GİRİŞ YAP",command=giris,
              width=50,
              height=5,
              bg="#FFEB3B",
              activebackground="#FDD835")
buton1.place(x=550,y=350)

buton2=tk.Button(text="KAYIT OL",command=kayit,
              width=50,
              height=5,
              bg="#FFEB3B",
              activebackground="#FDD835")
buton2.place(x=550,y=500)

#saat
zaman=''
tiktak=Label(ekran,font=("Arial",20))
tiktak.place(x=1240,y=20)
def saat():
    global zaman
    global tiktak
    zaman2=time.strftime('%H:%M:%S')
    if zaman2 != zaman:
        zaman=zaman2
        tiktak.config(text=zaman2,background="#E3F2FD")
    tiktak.after(50,saat)
saat()

ekran.mainloop()
