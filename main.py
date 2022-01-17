import tkinter as tk
import tkinter.font as tkFont
from random import*
import os

#activer la prochaine ligne que si vous voulez que le programme ne se ferme pas
#while 5>4 :
for i in range(1) : 

    def windows():

            #Les variable : 
            font="Helvetica"
            backgroud_color = '#EBF6F4'
            space = '                                                 '
            title = "Are you stupid ?"
            longueur = 11
            largeur = 3
            resizable = False
            hide = 700
            not_hide = 420
            #mise en place de la fenetre
            
            app = tk.Tk()
            x=app.winfo_screenwidth()
            y=app.winfo_screenheight()
            app.geometry(f"450x500+{randint(25,x-470)}+{randint(10, y-560)}")
            app.iconbitmap('icon.ico')
            app['background'] = backgroud_color
            app.resizable(width=resizable, height=resizable)
            app.title(space+title)

            #contenu de la page 

            AYS = tk.Label(app ,
                                    text="Are you stupid ?",
                                    font=(font,25))   
            Yes = tk.Button(app,
                                    text="Yes🙂",
                                    width=longueur,
                                    height=largeur,
                                    command=you,
                                    font=(font,15))
            No = tk.Button(app,
                                    text="No🙃",
                                    width=longueur,
                                    height=largeur,
                                    command=windows,
                                    font=(font,15))
            Exit = tk.Button(app,
                                    text="Exit",
                                    width=9,
                                    height=2,
                                    command=app.destroy,
                                    font=(font,15))
            
            Other = tk.Button(app,
                                    text="Other",
                                    width=9,
                                    height=2,
                                    command=other,
                                    font=(font,15))


            #affichage des éléments

            Yes.place(x=35, y=320)
            No.place(x=285, y=320)
            AYS.place(x=110 ,y=80)
            Exit.place(x=171, y=not_hide)
            Other.place(x=171, y=not_hide-90)
                
            app.mainloop()
        
    def you() :
            #Les variable : 

            font="Helvetica"
            backgroud_color = '#A3ACAA'
            space = '                                                 '
            title = "Are you stupid ?"
            longueur = 11
            largeur = 3
            resizable = False
            Hide = 700
            not_hide = 420
            #mise en place de la fenetre
            
            app = tk.Tk()                
            x=app.winfo_screenwidth()
            y=app.winfo_screenheight()
            app.geometry(f"450x500+{randint(25,x-470)}+{randint(10, y-560)}")
            app.iconbitmap('icon.ico')
            app['background'] = backgroud_color
            app.resizable(width=resizable, height=resizable)
            app.title(space+title)

            You = tk.Button(app,
                                    text="You",
                                    width=longueur,
                                    height=largeur,
                                    command=are,
                                    font=(font,15))
            x=randint(25, 285)
            y=randint(25, 385)
            
            You.place(x=x, y=y)

    def are() :


        #Les variable : 

            font="Helvetica"
            backgroud_color = '#292929'
            space = '                                                 '
            title = "Are you stupid ?"
            longueur = 11
            largeur = 3
            resizable = False
            Hide = 700
            not_hide = 420
            #mise en place de la fenetre
            
            app = tk.Tk()                
            x=app.winfo_screenwidth()
            y=app.winfo_screenheight()
            app.geometry(f"450x500+{randint(25,x-470)}+{randint(10, y-560)}")
            app.iconbitmap('icon.ico')
            app['background'] = backgroud_color
            app.resizable(width=resizable, height=resizable)
            app.title(space+title)

            Are = tk.Button(app,
                                    text="Are",
                                    width=longueur,
                                    height=largeur,
                                    command=stupid,
                                    font=(font,15))
            x=randint(25, 285)
            y=randint(25, 385)
            
            Are.place(x=x, y=y)

    def stupid() :


        #Les variable : 

            font="Helvetica"
            backgroud_color = '#000000'
            space = '                                                 '
            title = "Are you stupid ?"
            longueur = 11
            largeur = 3
            resizable = False
            Hide = 700
            not_hide = 420
            #mise en place de la fenetre
            
            app = tk.Tk()                
            x=app.winfo_screenwidth()
            y=app.winfo_screenheight()
            app.geometry(f"450x500+{randint(25,x-470)}+{randint(10, y-560)}")
            app.iconbitmap('icon.ico')
            app['background'] = backgroud_color
            app.resizable(width=resizable, height=resizable)
            app.title(space+title)
        
            Stupid = tk.Button(app,
                                    text="Stupid",
                                    width=longueur,
                                    height=largeur,
                                    command=kill,
                                    font=(font,15))
            x=randint(25, 285)
            y=randint(25, 385)
            
            Stupid.place(x=x, y=y)
        
    def kill() :
        os.system("rundll32.exe user32.dll,LockWorkStation")
    

    def other() :
            font="Helvetica"
            backgroud_color = '#EBF6F4'
            space = '                                                 '
            title = "Are you stupid ?"
            longueur = 11
            largeur = 3
            resizable = False
            Hide = 700
            not_hide = 420
            #mise en place de la fenetre
            
            app = tk.Tk()                
            x=app.winfo_screenwidth()
            y=app.winfo_screenheight()
            app.geometry("450x500")
            app.iconbitmap('icon.ico')
            app['background'] = backgroud_color
            app.resizable(width=resizable, height=resizable)
            app.title(space+title)
            
            
                
            AYS = tk.Label(app ,
                                    text="Sommaire des TP",
                                    font=(font,25)) 
    
            TP_1 = tk.Button(app,
                                    text="TP 1",
                                    width=longueur,
                                    height=largeur,
                                    command=TP_01,
                                    font=(font,15))
            
            TP_2 = tk.Button(app,
                                    text="TP 2",
                                    width=longueur,
                                    height=largeur,
                                    command=TP_02,
                                    font=(font,15))
            TP_3 = tk.Button(app,
                                    text="TP 3",
                                    width=longueur,
                                    height=largeur,
                                    command=TP_03,
                                    font=(font,15))
                                    
            TP_4 = tk.Button(app,
                                    text="TP 4",
                                    width=longueur,
                                    height=largeur,
                                    command=TP_04,
                                    font=(font,15))

            TP_5 = tk.Button(app,
                                    text="TP 5",
                                    width=longueur,
                                    height=largeur,
                                    command=TP_05,
                                    font=(font,15))
            
            Exit = tk.Button(app,
                                    text="Exit",
                                    width=9,
                                    height=2,
                                    command=app.destroy,
                                    font=(font,15))
                                    
            TP_1.place(x=35, y=100)
            TP_2.place(x=290, y= 100)
            TP_3.place(x=35, y=210)
            TP_4.place(x=290, y=210)
            TP_5.place(x=35, y=315)
            Exit.place(x=171, y=not_hide)
            AYS.place(x=110 ,y=25)
            
    def TP_01() :
                font="Helvetica"
                backgroud_color = '#EBF6F4'
                space = '                                                 '
                title = "Are you stupid ?"
                longueur = 11
                largeur = 3
                resizable = False
                Hide = 700
                not_hide = 420
                #mise en place de la fenetre
                
                app = tk.Tk()                
                x=app.winfo_screenwidth()
                y=app.winfo_screenheight()
                app.geometry("450x500")
                app.iconbitmap('icon.ico')
                app['background'] = backgroud_color
                app.resizable(width=resizable, height=resizable)
                app.title(space+title)
                
                AYS = tk.Label(app ,
                                        text="Are you stupid ?1",
                                        font=(font,25))
                AYS.place(x=110 ,y=80)
                
    def TP_02() :
                font="Helvetica"
                backgroud_color = '#EBF6F4'
                space = '                                                 '
                title = "Are you stupid ?"
                longueur = 11
                largeur = 3
                resizable = False
                Hide = 700
                not_hide = 420
                #mise en place de la fenetre
                
                app = tk.Tk()                
                x=app.winfo_screenwidth()
                y=app.winfo_screenheight()
                app.geometry("450x500")
                app.iconbitmap('icon.ico')
                app['background'] = backgroud_color
                app.resizable(width=resizable, height=resizable)
                app.title(space+title)
                
                AYS = tk.Label(app ,
                                        text="Are you stupid ?2",
                                        font=(font,25))
                AYS.place(x=110 ,y=80)
                
    def TP_03() :
                font="Helvetica"
                backgroud_color = '#EBF6F4'
                space = '                                                 '
                title = "Are you stupid ?"
                longueur = 11
                largeur = 3
                resizable = False
                Hide = 700
                not_hide = 420
                #mise en place de la fenetre
                
                app = tk.Tk()                
                x=app.winfo_screenwidth()
                y=app.winfo_screenheight()
                app.geometry("450x500")
                app.iconbitmap('icon.ico')
                app['background'] = backgroud_color
                app.resizable(width=resizable, height=resizable)
                app.title(space+title)
                
                AYS = tk.Label(app ,
                                        text="Are you stupid ?3",
                                        font=(font,25))
                AYS.place(x=110 ,y=80)
                
    def TP_04() :
                font="Helvetica"
                backgroud_color = '#EBF6F4'
                space = '                                                 '
                title = "Are you stupid ?"
                longueur = 11
                largeur = 3
                resizable = False
                Hide = 700
                not_hide = 420
                
                #mise en place de la fenetre
                
                app = tk.Tk()                
                x=app.winfo_screenwidth()
                y=app.winfo_screenheight()
                app.geometry("450x500")
                app.iconbitmap('icon.ico')
                app['background'] = backgroud_color
                app.resizable(width=resizable, height=resizable)
                app.title(space+title)
                
                AYS = tk.Label(app ,
                                        text="Are you stupid ?4",
                                        font=(font,25))
                AYS.place(x=110 ,y=80)
                
    def TP_05() :
                font="Helvetica"
                backgroud_color = '#EBF6F4'
                space = '                                                 '
                title = "Are you stupid ?"
                longueur = 11
                largeur = 3
                resizable = False
                Hide = 700
                not_hide = 420
                #mise en place de la fenetre
                
                app = tk.Tk()                
                x=app.winfo_screenwidth()
                y=app.winfo_screenheight()
                app.geometry("450x500")
                app.iconbitmap('icon.ico')
                app['background'] = backgroud_color
                app.resizable(width=resizable, height=resizable)
                app.title(space+title)
                
                AYS = tk.Label(app ,
                                        text="Are you stupid ?5",
                                        font=(font,25))
                AYS.place(x=110 ,y=80)
            
    windows()
    
'''
                def getEntry():
                    UR_1 = Var_1.get()
                    print(UR_1)
                    return UR_1
                    
                    
                Var_1 = tk.Entry(app,width=20, textvariable=tk.StringVar())
                Execut = tk.Button(app, height=1, width=10, text="Lire", command=getEntry)
                
                Var_1.pack()
                Execut.pack()
                '''
