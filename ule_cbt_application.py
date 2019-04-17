__author__ = 'PETEC'
import os
from tkinter import *
from tkinter import messagebox
directory = os.getcwd()
environment = Tk()
environment.title(directory + "\ ule cbt application")
width = environment.winfo_screenwidth()
height = environment.winfo_screenheight()
environment.geometry("%dx%d+0+0" % (width, height))

#=========================What happens after the submit======================
name_store = StringVar()# to store the user name
def submit():
    correct_name = name_store.get()
    if correct_name == " ":
        messagebox.showinfo(title="Alert",message="invalid username")
    else:
        titled_name = correct_name.title()
        environment.title(directory + "\ ule cbt application//" + titled_name)#changing the enviroments title

        background2 = Canvas(bg="white",width=width,height=height/1.1)
        background2.pack()


        #================== THE SUB HEADINGS (SUBJECTS AND INSTRUCTIONS) <START>=============================
        sub = Label(text="Subjects",font=("comic sans ms",15,"bold"),bg="white")
        sub.place(x=width/16,y=180)
        instruct = Label(text="Instructions",font=("comic sans ms",15,"bold"),bg="white")
        instruct.place(x=width/2,y=180)
        #================== THE SUB HEADINGS (SUBJECTS AND INSTRUCTIONS) <ENDS HERE>=============================

        #================= LIST OF INSTRUCTIONS <START>==========================================================
        instruction1 = Label(text=">>  Click on the Next button to attempt next Question ",font=("comic sans ms",10,"italic"),bg="white")
        instruction1.place(x=width/2,y=231)

        instruction1 = Label(text=">>  Click on the Prev button to attempt previous Question ",font=("comic sans ms",10,"italic"),bg="white")
        instruction1.place(x=width/2,y=271)

        instruction2 = Label(text=">>  Click on Finish button to view your score",font=("comic sans ms",10,"italic"),bg="white")
        instruction2.place(x=width/2,y=311)

        instruction3 = Label(text=">>  Click on the Logout button to quit the Exam ",font=("comic sans ms",10,"italic"),bg="white")
        instruction3.place(x=width/2,y=351)
        #================= LIST OF INSTRUCTIONS <ENDS HERE>==========================================================

        warning = Label(text="Select English and three more subject combinations ",font=("comic sans ms",10,"italic"),bg="white",fg="red")
        warning.place(x=width/16,y=231)#=============THE SELECTING OF SUBJECTS WARNING=======================

        def start():#===============THE START FUNCTION WHEN THE ""GET STARTED BUTTON"" IS CLICKED==================
##############################################=GENERAL-PURPOSE FUNCTIONS BELOW FOR ANY SELECTED SUBJECT TO AVOID """""""=############################
            def time_counter(): #=========FUNCTION FOR THE TIME INCREAMENT AND SPEED====================================
                    global seconds
                    seconds = 60
                    global minutes
                    minutes = 120
                    def count():
                        global minutes
                        global seconds
                        seconds -= 1
                        if seconds == 0:
                            minutes -= 1
                            seconds = 60
                        show_time.config(text=str(minutes)+":"+str(seconds))
                        show_time.after(1000,count)
                        if minutes == 0:
                            finish()
                    count()

            def finish():#========FUNCTION THAT DISPLAYS WHAT HAPPENS AFTER THE ""FINISH BUTTON"" IS CLICKED OR WHEN THE TIME IS OVER=========================
                    store_answer = 0
                    Incorrect_Answers = 0
                    correct_Answers = 0
                    for the_variable in variable_storage:
                        get_answer = int(the_variable[0].get())
                        if get_answer == the_variable[1]:
                            correct_Answers = correct_Answers + 1
                            if variable_storage.index(the_variable) > 99:
                                store_answer = store_answer + 2
                            else:
                                store_answer = store_answer + 1
                        elif get_answer == 0:
                            Incorrect_Answers = Incorrect_Answers + 1
                            pass

                    thanks_statement = "Thank you  for using Ule cbt application it is our pleasure. \nDo Ensure To Send Us Feedback On How To Improve The Software "
                    show_score_background = Canvas(bg="white",width=width,height=height/1.1)
                    show_score_background.place(x=0,y=0)
                    show_score = Message(text="Congratulation "+correct_name+" \nyour total score : "+str(store_answer)+"\nTotal Question : "+str(len(variable_storage))+"\n"+str(correct_Answers)+" >> correct Answer(s)""\n"+str(Incorrect_Answers)+" >> Incorrect Answer(s) :\n \n"+thanks_statement,
                                         bg="white",fg="green",font=("comic sans ms",25,"bold"),width=width/2)
                    show_score.place(x=width/15,y=height/30)

            def text_format_underline(text):#============THE FUNCTION THAT HELPS IN UNDERLINING SOME TEXT====================
                    show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                    starting_point = prevlistQ[navigation_counter].find(text)
                    word_to_count = text
                    Ending_point = starting_point + len(word_to_count)
                    begin1 = "1."+str(starting_point)
                    end1 = "1."+str(Ending_point)
                    begin = float(begin1)
                    end = float(end1)
                    show_question.insert(INSERT,prevlistQ[navigation_counter])
                    show_question.configure(state="disabled")
                    show_question.place(x=width/1.8,y=height/5)
                    show_question.tag_add("first",begin,end)
                    show_question.tag_config("first",underline=True)
            def text_format_italics(text):#============THE FUNCTION THAT HELPS IN ITALAIZING SOME TEXT====================
                    show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                    starting_point = prevlistQ[navigation_counter].find(text)
                    word_to_count = text
                    Ending_point = 1 + starting_point + len(word_to_count)
                    begin1 = "1."+str(starting_point)
                    end1 = "1."+str(Ending_point)
                    begin = float(begin1)
                    end = float(end1)
                    show_question.insert(INSERT,prevlistQ[navigation_counter])
                    show_question.configure(state="disabled")
                    show_question.place(x=width/1.8,y=height/5)
                    show_question.tag_add("first",begin,end)
                    show_question.tag_config("first",font=("comic sans ms",12,"italic"))

            def image_show(image_name):#=====================THE IMAGE DISPLAY FUNCTION STARTS HERE========================================
                    show_instruction.configure(state="normal")
                    show_instruction.delete("1.0","end")
                    show_instruction.insert(END,prevlist_IN[navigation_counter])
                    show_instruction.image_create(END,image=image_name)
                    show_instruction.configure(state="disabled")
                    #=====================THE IMAGE DISPLAY FUNCTION ENDS HERE========================================

            
            
            def calculator():#===========CALCULATOR FUNCTION=======================

                    def add(number):
                        entryField.insert(1000,number)

                    def delete():
                        entryField.delete(0,END)
    #=================SOLUTION FOR CALCULATOR STARTS HERE======================================================
                    def solve():
                        store_Q = entryField.get()
                        solution = eval(store_Q)
                        entryField.delete(0,END)
                        entryField.insert(END,solution)

                    calc = Toplevel()
                    calc.title("Calculator")
                    calc.geometry("200x200+%s+%s" %(int(width//1.2),int(height//3.5)))
                    Entry_store = StringVar
                    entryField = Entry(calc,textvariable=Entry_store,font = ("arial",15),relief=RAISED)
                    entryField.pack()
                    button1 = Button(calc,text=1,width=5,bg="green",fg="white",command=lambda: add(1))
                    button1.place(x=0,y=30)
                    button2 = Button(calc,text=2,width=5,bg="green",fg="white",command=lambda: add(2))
                    button2.place(x=50,y=30)
                    button3 = Button(calc,text=3,width=5,bg="green",fg="white",command=lambda: add(3))
                    button3.place(x=100,y=30)
                    Subbutton = Button(calc,text="-",width=5,bg="green",fg="white",command=lambda: add("-"))
                    Subbutton.place(x=150,y=30)

                    button4 = Button(calc,text=4,width=5,bg="green",fg="white",command=lambda: add(4))
                    button4.place(x=0,y=60)
                    button5 = Button(calc,text=5,width=5,bg="green",fg="white",command=lambda: add(5))
                    button5.place(x=50,y=60)
                    button6 = Button(calc,text=6,width=5,bg="green",fg="white",command=lambda: add(6))
                    button6.place(x=100,y=60)
                    Divbutton = Button(calc,text="/",width=5,bg="green",fg="white",command=lambda: add("/"))
                    Divbutton.place(x=150,y=60)


                    button7 = Button(calc,text=7,width=5,bg="green",fg="white",command=lambda: add(7))
                    button7.place(x=0,y=90)
                    button8 = Button(calc,text=8,width=5,bg="green",fg="white",command=lambda: add(8))
                    button8.place(x=50,y=90)
                    button9 = Button(calc,text=9,width=5,bg="green",fg="white",command=lambda: add(9))
                    button9.place(x=100,y=90)
                    Xbutton = Button(calc,text="x",width=5,bg="green",fg="white",command=lambda: add("*"))
                    Xbutton.place(x=150,y=90)

                    Pointbutton = Button(calc,text=".",width=5,bg="green",fg="white",command=lambda: add("."))
                    Pointbutton.place(x=0,y=120)
                    button0 = Button(calc,text=0,width=5,bg="green",fg="white",command=lambda: add(0))
                    button0.place(x=50,y=120)
                    Delbutton = Button(calc,text="C",width=5,bg="green",fg="white",command=delete)
                    Delbutton.place(x=100,y=120)
                    Addbutton = Button(calc,text="+",width=5,bg="green",fg="white",command=lambda: add("+"))
                    Addbutton.place(x=150,y=120)

                    EQbutton = Button(calc,text="=",width=27,height=2,bg="green",fg="white",command=solve)
                    EQbutton.place(x=0,y=150)

                    calc.mainloop()
    #=================SOLUTION FOR CALCULATOR ENDS HERE======================================================


##########################################=GENERAL-PURPOSE FUNCTIONS ABOVE FOR ANY SELECTED SUBJECT TO AVOID """""""=############################

            
            profile = PhotoImage(file="icon.png")
            icon_display = Text(height=5,width=10)
            icon_display.image_create(END,image=profile)
            icon_display.place(x=width/1.4,y=height/100)


            name_display = Label(text=titled_name,font=("arial",15,"italic"),fg="white",bg="green")
            name_display.place(x=width/1.4,y=height/10)

            get_stored_year = year_store.get()
            if get_stored_year == 2004:

                Eng_convert = Eng.get()
                Acc_convert = Acc.get()
                Bio_convert = Bio.get()
                Chem_convert = Chem.get()
                Comm_convert = Comm.get()
                Crk_convert = Crk.get()
                Econs_convert = Econs.get()
                Geo_convert = Geo.get()
                Govt_convert = Govt.get()
                Lit_convert = Lit.get()
                Math_convert = Math.get()
                Phy_convert = Phy.get()
                #==========================POSSIBLE SUBJECT COMBINATIONS STARTS HERE ======================================
                EngBioChemMaths = [Eng_convert,Bio_convert,Chem_convert,Math_convert]
                EngBioChemPhy = [Eng_convert,Bio_convert,Chem_convert,Phy_convert]
                EngEonsGovtMaths = [Eng_convert,Econs_convert,Govt_convert,Math_convert]
                #==========================POSSIBLE SUBJECT COMBINATIONS ENDS HERE ======================================

                checker = [Acc_convert,Bio_convert,Chem_convert,Comm_convert,Crk_convert,Econs_convert,Geo_convert,Govt_convert,Lit_convert,Math_convert,Phy_convert]
                check3 = checker.count(1)
                if Eng_convert == 0:
                    messagebox.showinfo(title="Warning",message="You must include English in the selected subjects")
                elif check3 > 3:
                    messagebox.showinfo(title="Warning",message="You must not select above three(4) subjects")
                elif check3 < 3:
                    messagebox.showinfo(title="Warning",message="You must select the total of four(4) subjects")
                elif EngBioChemMaths == [1,1,1,1]:
                    started_background = Canvas(bg="white",width=width,height=height/1.1)
                    started_background.place(x=0,y=height/5)
                    #====================================== STUFFS FOR TIME DISPLAY STARTS HERE=================================================
                    show_time = Label(fg="white",font=("Chromia Condensed",25,"italic"),bg="green")
                    show_time.place(x=width/1.23,y=height/25)
                    time_counter()
                    #======================================STUFFS FOR TIME DISPLAY ENDSS HERE=================================================

                    #===========================ARRANGING OF SUBJECT FILES AND FOUR SUBJECT DISPLAY STARTS HERE======================================
                    four_subject_show = [(Eng_convert,"English"),(Acc_convert,"Account"),(Bio_convert,"Biology"),
                                         (Chem_convert,"Chemistry"),(Comm_convert,"Commerce"),(Crk_convert,"Crk"),
                                         (Econs_convert,"Economics"),(Geo_convert,"Geography"),(Govt_convert,"Government"),
                                         (Lit_convert,"Literature"),(Math_convert,"Mathematics"),(Phy_convert,"Physics")]

                    read_four_subject_files = [(Eng_convert,"files/2004/English2004IN.txt","files/2004/English2004Q.txt","files/2004/English2004O.txt"),
                                                 (Acc_convert,"files/2004/Account2004IN.txt","files/2004/Account2004Q.txt","files/2004/Account2004O.txt"),
                                                 (Bio_convert,"files/2004/Biology2004IN.txt","files/2004/Biology2004Q.txt","files/2004/Biology2004O.txt"),
                                                 (Chem_convert,"files/2004/Chemistry2004IN.txt","files/2004/Chemistry2004Q.txt","files/2004/Chemistry2004O.txt"),
                                                 (Comm_convert,"files/2004/Commerce2004IN.txt","files/2004/Commerce2004Q.txt","files/2004/Commerce2004O.txt"),
                                                 (Crk_convert,"files/2004/Crk2004IN.txt","files/2004/Crk2004Q.txt","files/2004/Crk2004O.txt"),
                                                 (Econs_convert,"files/2004/Economics2004IN.txt","files/2004/Economics2004Q.txt","files/2004/Economics2004O.txt"),
                                                 (Geo_convert,"files/2004/Geography2004IN.txt","files/2004/Geography2004Q.txt","files/2004/Geography2004O.txt"),
                                                 (Govt_convert,"files/2004/Government2004IN.txt","files/2004/Government2004Q.txt","files/2004/Government2004O.txt"),
                                                 (Lit_convert,"files/2004/Literature2004IN.txt","files/2004/Literature2004Q.txt","files/2004/Literature2004O.txt"),
                                                 (Math_convert,"files/2004/Maths2004IN.txt","files/2004/Maths2004Q.txt","files/2004/Maths2004O.txt"),
                                                 (Phy_convert,"files/2004/physics2004IN.txt","files/2004/physics2004Q.txt","files/2004/physics2004O.txt")]
                    #===========================ARRANGING OF SUBJECT FILES AND FOUR SUBJECT DISPLAY ENDS HERE========================================================

                    #=========================== ASSIGNMENT OF ANSWERS STORE STARTS HERE =========================================================================================
                    var1 = IntVar(); var2 = IntVar(); var3 = IntVar(); var4 = IntVar(); var5 = IntVar(); var6 = IntVar(); var7 = IntVar(); var8 = IntVar(); var9 = IntVar(); var10 = IntVar()
                    var11 = IntVar(); var12 = IntVar(); var13 = IntVar(); var14 = IntVar(); var15 = IntVar(); var16 = IntVar(); var17 = IntVar(); var18 = IntVar(); var19 = IntVar(); var20 = IntVar()
                    var21 = IntVar(); var22 = IntVar(); var23 = IntVar(); var24 = IntVar(); var25 = IntVar(); var26 = IntVar(); var27 = IntVar(); var28 = IntVar(); var29 = IntVar(); var30 = IntVar()
                    var31 = IntVar(); var32 = IntVar(); var33 = IntVar(); var34 = IntVar(); var35 = IntVar(); var36 = IntVar(); var37 = IntVar(); var38 = IntVar(); var39 = IntVar(); var40 = IntVar()
                    var41 = IntVar(); var42 = IntVar(); var43 = IntVar(); var44 = IntVar(); var45 = IntVar(); var46 = IntVar(); var47 = IntVar(); var48 = IntVar(); var49 = IntVar(); var50 = IntVar()
                    var51 = IntVar(); var52 = IntVar(); var53 = IntVar(); var54 = IntVar(); var55 = IntVar(); var56 = IntVar(); var57 = IntVar(); var58 = IntVar(); var59 = IntVar(); var60 = IntVar()
                    var61 = IntVar(); var62 = IntVar(); var63 = IntVar(); var64 = IntVar(); var65 = IntVar(); var66 = IntVar(); var67 = IntVar(); var68 = IntVar(); var69 = IntVar(); var70 = IntVar()
                    var71 = IntVar(); var72 = IntVar(); var73 = IntVar(); var74 = IntVar(); var75 = IntVar(); var76 = IntVar(); var77 = IntVar(); var78 = IntVar(); var79 = IntVar(); var80 = IntVar()
                    var81 = IntVar(); var82 = IntVar(); var83 = IntVar(); var84 = IntVar(); var85 = IntVar(); var86 = IntVar(); var87 = IntVar(); var88 = IntVar(); var89 = IntVar(); var90 = IntVar()
                    var91 = IntVar(); var92 = IntVar(); var93 = IntVar(); var94 = IntVar(); var95 = IntVar(); var96 = IntVar(); var97 = IntVar(); var98 = IntVar(); var99 = IntVar(); var100 = IntVar()
                    var101 = IntVar(); var102 = IntVar(); var103 = IntVar(); var104 = IntVar(); var105 = IntVar(); var106 = IntVar(); var107 = IntVar(); var108 = IntVar(); var109 = IntVar(); var110 = IntVar()
                    var111 = IntVar(); var112 = IntVar(); var113 = IntVar(); var114 = IntVar(); var115 = IntVar(); var116 = IntVar(); var117 = IntVar(); var118 = IntVar(); var119 = IntVar(); var120 = IntVar()
                    var121 = IntVar(); var122 = IntVar(); var123 = IntVar(); var124 = IntVar(); var125 = IntVar(); var126 = IntVar(); var127 = IntVar(); var128 = IntVar(); var129 = IntVar(); var130 = IntVar()
                    var131 = IntVar(); var132 = IntVar(); var133 = IntVar(); var134 = IntVar(); var135 = IntVar(); var136 = IntVar(); var137 = IntVar(); var138 = IntVar(); var139 = IntVar(); var140 = IntVar()
                    var141 = IntVar(); var142 = IntVar(); var143 = IntVar(); var144 = IntVar(); var145 = IntVar(); var146 = IntVar(); var147 = IntVar(); var148 = IntVar(); var149 = IntVar(); var150 = IntVar()
                    var151 = IntVar(); var152 = IntVar(); var153 = IntVar(); var154 = IntVar(); var155 = IntVar(); var156 = IntVar(); var157 = IntVar(); var158 = IntVar(); var159 = IntVar(); var160 = IntVar()
                    var161 = IntVar(); var162 = IntVar(); var163 = IntVar(); var164 = IntVar(); var165 = IntVar(); var166 = IntVar(); var167 = IntVar(); var168 = IntVar(); var169 = IntVar(); var170 = IntVar()
                    var171 = IntVar(); var172 = IntVar(); var173 = IntVar(); var174 = IntVar(); var175 = IntVar(); var176 = IntVar(); var177 = IntVar(); var178 = IntVar(); var179 = IntVar(); var180 = IntVar()
                    var181 = IntVar(); var182 = IntVar(); var183 = IntVar(); var184 = IntVar(); var185 = IntVar(); var186 = IntVar(); var187 = IntVar(); var188 = IntVar(); var189 = IntVar(); var190 = IntVar()
                    var191 = IntVar(); var192 = IntVar(); var193 = IntVar(); var194 = IntVar(); var195 = IntVar(); var196 = IntVar(); var197 = IntVar(); var198 = IntVar(); var199 = IntVar(); var200 = IntVar()
                    var201 = IntVar(); var202 = IntVar(); var203 = IntVar(); var204 = IntVar(); var205 = IntVar(); var206 = IntVar(); var207 = IntVar(); var208 = IntVar(); var209 = IntVar(); var210 = IntVar()
                    var211 = IntVar(); var212 = IntVar(); var213 = IntVar(); var214 = IntVar(); var215 = IntVar(); var216 = IntVar(); var217 = IntVar(); var218 = IntVar(); var219 = IntVar(); var220 = IntVar()
                    var221 = IntVar(); var222 = IntVar(); var223 = IntVar(); var224 = IntVar(); var225 = IntVar(); var226 = IntVar(); var227 = IntVar(); var228 = IntVar(); var229 = IntVar(); var230 = IntVar()
                    var231 = IntVar(); var232 = IntVar(); var233 = IntVar(); var234 = IntVar(); var235 = IntVar(); var236 = IntVar(); var237 = IntVar(); var238 = IntVar(); var239 = IntVar(); var240 = IntVar()
                    var241 = IntVar(); var242 = IntVar(); var243 = IntVar(); var244 = IntVar(); var245 = IntVar(); var246 = IntVar(); var247 = IntVar(); var248 = IntVar(); var249 = IntVar(); var250 = IntVar()

                    #=========================== ASSIGNMENT OF ANSWERS STORE STARTS HERE =========================================================================================
                    #===========================================================================================================================================================
                    variable_storage = [(var1,1),(var2,1),(var3,1),(var4,1),(var5,1),(var6,1),(var7,1),(var8,1),(var9,1),(var10,1),(var11,1),(var12,1),(var13,1),(var14,1),(var15,1),(var16,1),
                                        (var17,1),(var18,1),(var19,1),(var20,1),(var21,1),(var22,1),(var23,1),(var24,1),(var25,1),(var26,1),(var27,1),(var28,1),(var29,1),(var30,1),(var31,1),
                                        (var32,1),(var33,1),(var34,1),(var35,1),(var36,1),(var37,1),(var38,1),(var39,1),(var40,1),(var41,1),(var42,1),(var43,1),(var44,1),(var45,1),(var46,1),
                                        (var47,1),(var48,1),(var49,1),(var50,1),(var51,1),(var52,1),(var53,1),(var54,1),(var55,1),(var56,1),(var57,1),(var58,1),(var59,1),(var60,1),(var61,1),
                                        (var62,2),(var63,2),(var64,2),(var65,2),(var66,2),(var67,2),(var68,2),(var69,2),(var70,2),(var71,2),(var72,2),(var73,2),(var74,2),(var75,2),(var76,2),
                                        (var77,2),(var78,2),(var79,2),(var80,2),(var81,2),(var82,2),(var83,2),(var84,2),(var85,2),(var86,2),(var87,2),(var88,2),(var89,2),(var90,2),(var91,2),
                                        (var92,2),(var93,2),(var94,2),(var95,2),(var96,2),(var97,2),(var98,2),(var99,2),(var100,2),(var101,2),(var102,2),(var103,2),(var104,2),(var105,2),
                                        (var106,2),(var107,2),(var108,2),(var109,2),(var110,2),(var111,2),(var112,2),(var113,2),(var114,2),(var115,2),(var116,2),(var117,2),(var118,2),
                                        (var119,2),(var120,2),(var121,2),(var122,2),(var123,2),(var124,2),(var125,2),(var126,2),(var127,2),(var128,2),(var129,2),(var130,2),(var131,2),
                                        (var132,3),(var133,3),(var134,3),(var135,3),(var136,3),(var137,3),(var138,3),(var139,3),(var140,3),(var141,3),(var142,3),(var143,3),(var144,3),
                                        (var145,3),(var146,3),(var147,3),(var148,3),(var149,3),(var150,3),(var151,3),(var152,3),(var153,3),(var154,3),(var155,3),(var156,3),(var157,3),
                                        (var158,3),(var159,3),(var160,3),(var161,3),(var162,3),(var163,3),(var164,3),(var165,3),(var166,3),(var167,3),(var168,3),(var169,3),(var170,3),
                                        (var171,3),(var172,3),(var173,3),(var174,3),(var175,3),(var176,3),(var177,3),(var178,3),(var179,3),(var180,3),(var181,3),(var182,3),(var183,3),
                                        (var184,4),(var185,4),(var186,4),(var187,4),(var188,4),(var189,4),(var190,4),(var191,4),(var192,4),(var193,4),(var194,4),(var195,4),(var196,4),
                                        (var197,4),(var198,4),(var199,4),(var200,4),(var201,4),(var202,4),(var203,4),(var204,4),(var205,4),(var206,4),(var207,4),(var208,4),(var209,4),
                                        (var210,4),(var211,4),(var212,4),(var213,4),(var214,4),(var215,4),(var216,4),(var217,4),(var218,4),(var219,4),(var220,4),(var221,4),(var222,4),
                                        (var223,4),(var224,4),(var225,4),(var226,4),(var227,4),(var228,4),(var229,4),(var230,4),(var231,4),(var232,4),(var233,4),(var234,4),(var235,4),
                                        (var236,4),(var237,4),(var238,4),(var239,4),(var240,4),(var241,4),(var242,4),(var243,4),(var244,4),(var245,4),(var246,4),(var247,4),(var248,4),
                                        (var249,4),(var250,4)]
                    #================================================================================================================================================================
                    def first_subject_navigation():
                        global navigation_counter
                        navigation_counter = 0
                        show_instruction.configure(state="normal")
                        show_instruction.delete("1.0","end")
                        show_instruction.insert(END,prevlist_IN[navigation_counter])
                        show_instruction.configure(state="disabled")
                        Canvas(bg="white",width=width/2.2,height=height/2.5).place(x=width/1.85,y=height/5)
                        show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                        show_question.insert(INSERT,prevlistQ[navigation_counter])
                        show_question.configure(state="disabled")
                        show_question.place(x=width/1.8,y=height/5)
                        radio_value_count_down = 1
                        y_axis_radiobutton_space = 1
                        for a in prevlistOP[navigation_counter]:
                            show_option = Radiobutton(text=a,variable=variable_storage[navigation_counter][0],value=radio_value_count_down,bg="white")
                            show_option.place(x=width/1.8,y=250+y_axis_radiobutton_space)
                            radio_value_count_down += 1
                            y_axis_radiobutton_space += 30


                    def second_subject_navigation():
                        global navigation_counter
                        navigation_counter = 100
                        show_instruction.configure(state="normal")
                        show_instruction.delete("1.0","end")
                        show_instruction.insert(END,prevlist_IN[navigation_counter])
                        show_instruction.configure(state="disabled")
                        Canvas(bg="white",width=width/2.2,height=height/2.5).place(x=width/1.85,y=height/5)
                        show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                        show_question.insert(INSERT,prevlistQ[navigation_counter])
                        show_question.configure(state="disabled")
                        show_question.place(x=width/1.8,y=height/5)
                        radio_value_count_down = 1
                        y_axis_radiobutton_space = 1
                        for a in prevlistOP[navigation_counter]:
                            show_option = Radiobutton(text=a,variable=variable_storage[navigation_counter][0],value=radio_value_count_down,bg="white")
                            show_option.place(x=width/1.8,y=250+y_axis_radiobutton_space)
                            radio_value_count_down += 1
                            y_axis_radiobutton_space += 30


                    def third_subject_navigation():
                        global navigation_counter
                        navigation_counter = 150
                        show_instruction.configure(state="normal")
                        show_instruction.delete("1.0","end")
                        show_instruction.insert(END,prevlist_IN[navigation_counter])
                        show_instruction.configure(state="disabled")
                        Canvas(bg="white",width=width/2.2,height=height/2.5).place(x=width/1.85,y=height/5)
                        show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                        show_question.insert(INSERT,prevlistQ[navigation_counter])
                        show_question.configure(state="disabled")
                        show_question.place(x=width/1.8,y=height/5)
                        radio_value_count_down = 1
                        y_axis_radiobutton_space = 1
                        for a in prevlistOP[navigation_counter]:
                            show_option = Radiobutton(text=a,variable=variable_storage[navigation_counter][0],value=radio_value_count_down,bg="white")
                            show_option.place(x=width/1.8,y=250+y_axis_radiobutton_space)
                            radio_value_count_down += 1
                            y_axis_radiobutton_space += 30


                    def fourth_subject_navigation():
                        global navigation_counter
                        navigation_counter = 200
                        show_instruction.configure(state="normal")
                        show_instruction.delete("1.0","end")
                        show_instruction.insert(END,prevlist_IN[navigation_counter])
                        show_instruction.configure(state="disabled")
                        Canvas(bg="white",width=width/2.2,height=height/2.5).place(x=width/1.85,y=height/5)
                        show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                        show_question.insert(INSERT,prevlistQ[navigation_counter])
                        show_question.configure(state="disabled")
                        show_question.place(x=width/1.8,y=height/5)
                        radio_value_count_down = 1
                        y_axis_radiobutton_space = 1
                        for a in prevlistOP[navigation_counter]:
                            show_option = Radiobutton(text=a,variable=variable_storage[navigation_counter][0],value=radio_value_count_down,bg="white")
                            show_option.place(x=width/1.8,y=250+y_axis_radiobutton_space)
                            radio_value_count_down += 1
                            y_axis_radiobutton_space += 30


                    four_subject_button_function_list = [first_subject_navigation,second_subject_navigation,third_subject_navigation,fourth_subject_navigation]
                    the_list_slice_var = -1
                    x_axis_button_spacing = 100
                    for display,subject in four_subject_show:
                            if display == 1:
                                the_list_slice_var = the_list_slice_var + 1
                                show_four_sub = Button(text=subject,width=15,bg="White",fg="green",command=four_subject_button_function_list[the_list_slice_var])
                                show_four_sub.place(x=x_axis_button_spacing,y=height/6)
                                x_axis_button_spacing = x_axis_button_spacing+100


                    global navigation_counter
                    navigation_counter = 0
                    prevlist_IN = []
                    for display,INSTRUCTION,QUESTION,OPTION in read_four_subject_files:
                        if display == 1:
                            instructions = open(INSTRUCTION,"r",encoding="utf8")#===============OPENING QUESTION GUIDE FILE===================================
                            while True:
                                instruction = instructions.readline()
                                prevlist_IN.append(instruction)
                                if instruction.endswith("~"):
                                    break

                    #==================IMAGES ARE STORED FROM HERE==============================

                    Biophoto3and4 = PhotoImage(file="files/2004/img/Bio2004_3and4.gif")
                    Biophoto8and9 = PhotoImage(file="files/2004/img/Bio2004_8and9.gif")
                    Biophoto12and13 = PhotoImage(file="files/2004/img/Bio2004_12and13.gif")
                    Biophoto15and16 = PhotoImage(file="files/2004/img/Bio2004_15and16.gif")
                    Biophoto32and33 = PhotoImage(file="files/2004/img/Bio2004_32and33.gif")
                    Biophoto44and45 = PhotoImage(file="files/2004/img/Bio2004_44and45.gif")
                    chemphoto2 = PhotoImage(file="files/2004/img/chem2004_2.gif")
                    chemphoto8 = PhotoImage(file="files/2004/img/chem2004_8.gif")
                    chemphoto9 = PhotoImage(file="files/2004/img/chem2004_9.gif")
                    chemphoto16 = PhotoImage(file="files/2004/img/chem2004_16.gif")
                    chemphoto20 = PhotoImage(file="files/2004/img/chem2004_20.gif")
                    chemphoto22 = PhotoImage(file="files/2004/img/chem2004_22.gif")
                    chemphoto23 = PhotoImage(file="files/2004/img/chem2004_23.gif")
                    chemphoto36 = PhotoImage(file="files/2004/img/chem2004_36.gif")
                    chemphoto40 = PhotoImage(file="files/2004/img/chem2004_40.gif")
                    mathsphoto1 = PhotoImage(file="files/2004/img/Maths2004_1.gif")
                    mathsphoto3 = PhotoImage(file="files/2004/img/Maths2004_3.gif")
                    mathsphoto6 = PhotoImage(file="files/2004/img/Maths2004_6.gif")
                    mathsphoto8 = PhotoImage(file="files/2004/img/Maths2004_8.gif")
                    mathsphoto9 = PhotoImage(file="files/2004/img/Maths2004_9.gif")
                    mathsphoto11 = PhotoImage(file="files/2004/img/Maths2004_11.gif")
                    mathsphoto12 = PhotoImage(file="files/2004/img/Maths2004_12.gif")
                    mathsphoto16 = PhotoImage(file="files/2004/img/Maths2004_16.gif")
                    mathsphoto18 = PhotoImage(file="files/2004/img/Maths2004_18.gif")
                    mathsphoto22 = PhotoImage(file="files/2004/img/Maths2004_22.gif")
                    mathsphoto23 = PhotoImage(file="files/2004/img/Maths2004_23.gif")
                    mathsphoto26 = PhotoImage(file="files/2004/img/Maths2004_26.gif")
                    mathsphoto27and29 = PhotoImage(file="files/2004/img/Maths2004_27and29.gif")
                    mathsphoto33 = PhotoImage(file="files/2004/img/Maths2004_33.gif")
                    mathsphoto36 = PhotoImage(file="files/2004/img/Maths2004_36.gif")
                    mathsphoto37 = PhotoImage(file="files/2004/img/Maths2004_37.gif")
                    mathsphoto39 = PhotoImage(file="files/2004/img/Maths2004_39.gif")
                    mathsphoto40 = PhotoImage(file="files/2004/img/Maths2004_40.gif")
                    mathsphoto42 = PhotoImage(file="files/2004/img/Maths2004_42.gif")
                    mathsphoto49 = PhotoImage(file="files/2004/img/Maths2004_49.gif")
                    #==================IMAGES STORES ENDS HERE==============================

                    def nextQ():#======================================THE NEXT_QUESTION FUNCTION DEFINITION==========================
                        global navigation_counter
                        navigation_counter = navigation_counter + 1
                        if navigation_counter == 102:
                            image_show(Biophoto3and4)
                        elif navigation_counter == 103:
                            image_show(Biophoto3and4)
                        elif navigation_counter == 107:
                            image_show(Biophoto8and9)
                        elif navigation_counter == 108:
                            image_show(Biophoto8and9)
                        elif navigation_counter == 111:
                            image_show(Biophoto12and13)
                        elif navigation_counter == 112:
                            image_show(Biophoto12and13)
                        elif navigation_counter == 114:
                            image_show(Biophoto15and16)
                        elif navigation_counter == 115:
                            image_show(Biophoto15and16)
                        elif navigation_counter == 131:
                            image_show(Biophoto32and33)
                        elif navigation_counter == 132:
                            image_show(Biophoto32and33)
                        elif navigation_counter == 143:
                            image_show(Biophoto44and45)
                        elif navigation_counter == 144:
                            image_show(Biophoto44and45)
                        elif navigation_counter == 151:
                            image_show(chemphoto2)
                        elif navigation_counter == 157:
                            image_show(chemphoto8)
                        elif navigation_counter == 158:
                            image_show(chemphoto9)
                        elif navigation_counter == 165:
                            image_show(chemphoto16)
                        elif navigation_counter == 169:
                            image_show(chemphoto20)
                        elif navigation_counter == 171:
                            image_show(chemphoto22)
                        elif navigation_counter == 172:
                            image_show(chemphoto23)
                        elif navigation_counter == 185:
                            image_show(chemphoto36)
                        elif navigation_counter == 189:
                            image_show(chemphoto40)
                        elif navigation_counter == 200:
                            image_show(mathsphoto1)
                        elif navigation_counter == 202:
                            image_show(mathsphoto3)
                        elif navigation_counter == 205:
                            image_show(mathsphoto6)
                        elif navigation_counter == 207:
                            image_show(mathsphoto8)
                        elif navigation_counter == 208:
                            image_show(mathsphoto9)
                        elif navigation_counter == 210:
                            image_show(mathsphoto11)
                        elif navigation_counter == 211:
                            image_show(mathsphoto12)
                        elif navigation_counter == 215:
                            image_show(mathsphoto16)
                        elif navigation_counter == 217:
                            image_show(mathsphoto18)
                        elif navigation_counter == 221:
                            image_show(mathsphoto22)
                        elif navigation_counter == 222:
                            image_show(mathsphoto23)
                        elif navigation_counter == 225:
                            image_show(mathsphoto26)
                        elif navigation_counter == 226:
                            image_show(mathsphoto27and29)
                        elif navigation_counter == 228:
                            image_show(mathsphoto27and29)
                        elif navigation_counter == 232:
                            image_show(mathsphoto33)
                        elif navigation_counter == 235:
                            image_show(mathsphoto36)
                        elif navigation_counter == 236:
                            image_show(mathsphoto37)
                        elif navigation_counter == 238:
                            image_show(mathsphoto39)
                        elif navigation_counter == 239:
                            image_show(mathsphoto40)
                        elif navigation_counter == 241:
                            image_show(mathsphoto42)
                        elif navigation_counter == 248:
                            image_show(mathsphoto49)
                        else:
                            show_instruction.configure(state="normal")
                            show_instruction.delete("1.0","end")
                            show_instruction.insert(END,prevlist_IN[navigation_counter])
                            show_instruction.configure(state="disabled")
                        Canvas(bg="white",width=width/2.2,height=height/2.5).place(x=width/1.85,y=height/5)
                        show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                        if navigation_counter == 25:
                            text_format_underline("ea")
                        elif navigation_counter == 26:
                            text_format_underline("i")
                        elif navigation_counter == 54:
                            text_format_underline("ed")
                        elif navigation_counter == 55:
                            text_format_underline("ch")
                        elif navigation_counter == 56:
                            text_format_underline("j")
                        elif navigation_counter == 68:
                            text_format_italics("ill at ease")
                        elif navigation_counter == 69:
                            text_format_italics("liberality")
                        elif navigation_counter == 70:
                            text_format_italics("misnomer")
                        elif navigation_counter == 71:
                            text_format_italics("pejorative")
                        elif navigation_counter == 72:
                            text_format_italics("turmoil")
                        elif navigation_counter == 73:
                            text_format_italics("heritage")
                        elif navigation_counter == 74:
                            text_format_italics("with a heavy hand")
                        elif navigation_counter == 75:
                            text_format_italics("levity")
                        elif navigation_counter == 76:
                            text_format_italics("insignia")
                        elif navigation_counter == 77:
                            text_format_italics("Funnily enough")
                        elif navigation_counter == 78:
                            text_format_italics("mottled")
                        elif navigation_counter == 79:
                            text_format_italics("substantiate")
                        elif navigation_counter == 80:
                            text_format_italics("utmost")
                        elif navigation_counter == 81:
                            text_format_italics("downturn")
                        elif navigation_counter == 82:
                            text_format_italics("boomeranged")
                        elif navigation_counter == 85:
                            text_format_italics("unnerved")
                        elif navigation_counter == 86:
                            text_format_italics("shady")
                        elif navigation_counter == 87:
                            text_format_italics("writhed in pain")
                        elif navigation_counter == 88:
                            text_format_italics("imperilled")
                        elif navigation_counter == 89:
                            text_format_italics("ecstatic")
                        elif navigation_counter == 90:
                            text_format_italics("dauntless")
                        elif navigation_counter == 91:
                            text_format_italics("outlandish")
                        elif navigation_counter == 92:
                            text_format_italics("casual")
                        elif navigation_counter == 93:
                            text_format_italics("plucky")
                        elif navigation_counter == 94:
                            text_format_italics("freelance")
                        elif navigation_counter == 95:
                            text_format_italics("get back at")
                        elif navigation_counter == 96:
                            text_format_italics("tractable")
                        elif navigation_counter == 97:
                            text_format_italics("vindictive")
                        elif navigation_counter == 98:
                            text_format_italics("potency")
                        elif navigation_counter == 99:
                            text_format_italics("deranged")
                        else:
                            show_question.insert(INSERT,prevlistQ[navigation_counter])
                            show_question.configure(state="disabled")
                            show_question.place(x=width/1.8,y=height/5)
                        radio_value_count_down = 1
                        y_axis_radiobutton_space = 1
                        for a in prevlistOP[navigation_counter]:
                            show_option = Radiobutton(text=a,variable=variable_storage[navigation_counter][0],value=radio_value_count_down,bg="white")
                            show_option.place(x=width/1.8,y=250+y_axis_radiobutton_space)
                            radio_value_count_down += 1
                            y_axis_radiobutton_space += 30
                        def prevQ():#THE PREVIOUS_FUNCTION DEFINITION========================================
                            global navigation_counter
                            navigation_counter = navigation_counter - 1
                            if navigation_counter < 0:
                                navigation_counter = 0
                                show_instruction.configure(state="normal")
                                show_instruction.delete("1.0","end")
                                show_instruction.insert(END,prevlist_IN[navigation_counter])
                                show_instruction.configure(state="disabled")
                                Canvas(bg="white",width=width/2.2,height=height/2.5).place(x=width/1.85,y=height/5)
                                show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                                show_question.insert(INSERT,prevlistQ[navigation_counter])
                                show_question.configure(state="disabled")
                                show_question.place(x=width/1.8,y=height/5)
                                radio_value_count_down = 1
                                y_axis_radiobutton_space = 1
                                for a in prevlistOP[navigation_counter]:
                                    show_option = Radiobutton(text=a,variable=variable_storage[navigation_counter][0],value=radio_value_count_down,bg="white")
                                    show_option.place(x=width/1.8,y=250+y_axis_radiobutton_space)
                                    radio_value_count_down += 1
                                    y_axis_radiobutton_space += 30
                            else:
                                if navigation_counter == 102:
                                    image_show(Biophoto3and4)
                                elif navigation_counter == 103:
                                    image_show(Biophoto3and4)
                                elif navigation_counter == 107:
                                    image_show(Biophoto8and9)
                                elif navigation_counter == 108:
                                    image_show(Biophoto8and9)
                                elif navigation_counter == 111:
                                    image_show(Biophoto12and13)
                                elif navigation_counter == 112:
                                    image_show(Biophoto12and13)
                                elif navigation_counter == 114:
                                    image_show(Biophoto15and16)
                                elif navigation_counter == 115:
                                    image_show(Biophoto15and16)
                                elif navigation_counter == 131:
                                    image_show(Biophoto32and33)
                                elif navigation_counter == 132:
                                    image_show(Biophoto32and33)
                                elif navigation_counter == 143:
                                    image_show(Biophoto44and45)
                                elif navigation_counter == 144:
                                    image_show(Biophoto44and45)
                                elif navigation_counter == 151:
                                    image_show(chemphoto2)
                                elif navigation_counter == 157:
                                    image_show(chemphoto8)
                                elif navigation_counter == 158:
                                    image_show(chemphoto9)
                                elif navigation_counter == 165:
                                    image_show(chemphoto16)
                                elif navigation_counter == 169:
                                    image_show(chemphoto20)
                                elif navigation_counter == 171:
                                    image_show(chemphoto22)
                                elif navigation_counter == 172:
                                    image_show(chemphoto23)
                                elif navigation_counter == 185:
                                    image_show(chemphoto36)
                                elif navigation_counter == 189:
                                    image_show(chemphoto40)
                                elif navigation_counter == 200:
                                    image_show(mathsphoto1)
                                elif navigation_counter == 202:
                                    image_show(mathsphoto3)
                                elif navigation_counter == 205:
                                    image_show(mathsphoto6)
                                elif navigation_counter == 207:
                                    image_show(mathsphoto8)
                                elif navigation_counter == 208:
                                    image_show(mathsphoto9)
                                elif navigation_counter == 210:
                                    image_show(mathsphoto11)
                                elif navigation_counter == 211:
                                    image_show(mathsphoto12)
                                elif navigation_counter == 215:
                                    image_show(mathsphoto16)
                                elif navigation_counter == 217:
                                    image_show(mathsphoto18)
                                elif navigation_counter == 221:
                                    image_show(mathsphoto22)
                                elif navigation_counter == 222:
                                    image_show(mathsphoto23)
                                elif navigation_counter == 225:
                                    image_show(mathsphoto26)
                                elif navigation_counter == 226:
                                    image_show(mathsphoto27and29)
                                elif navigation_counter == 228:
                                    image_show(mathsphoto27and29)
                                elif navigation_counter == 232:
                                    image_show(mathsphoto33)
                                elif navigation_counter == 235:
                                    image_show(mathsphoto36)
                                elif navigation_counter == 236:
                                    image_show(mathsphoto37)
                                elif navigation_counter == 238:
                                    image_show(mathsphoto39)
                                elif navigation_counter == 239:
                                    image_show(mathsphoto40)
                                elif navigation_counter == 241:
                                    image_show(mathsphoto42)
                                elif navigation_counter == 248:
                                    image_show(mathsphoto49)
                                else:
                                    show_instruction.configure(state="normal")
                                    show_instruction.delete("1.0","end")
                                    show_instruction.insert(END,prevlist_IN[navigation_counter])
                                    show_instruction.configure(state="disabled")
                                Canvas(bg="white",width=width/2.2,height=height/2.5).place(x=width/1.85,y=height/5)
                                show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                                if navigation_counter == 25:
                                    text_format_underline("ea")
                                elif navigation_counter == 26:
                                    text_format_underline("i")
                                elif navigation_counter == 54:
                                    text_format_underline("ed")
                                elif navigation_counter == 55:
                                    text_format_underline("ch")
                                elif navigation_counter == 56:
                                    text_format_underline("j")
                                elif navigation_counter == 68:
                                    text_format_italics("ill at ease")
                                elif navigation_counter == 69:
                                    text_format_italics("liberality")
                                elif navigation_counter == 70:
                                    text_format_italics("misnomer")
                                elif navigation_counter == 71:
                                    text_format_italics("pejorative")
                                elif navigation_counter == 72:
                                    text_format_italics("turmoil")
                                elif navigation_counter == 73:
                                    text_format_italics("heritage")
                                elif navigation_counter == 74:
                                    text_format_italics("with a heavy hand")
                                elif navigation_counter == 75:
                                    text_format_italics("levity")
                                elif navigation_counter == 76:
                                    text_format_italics("insignia")
                                elif navigation_counter == 77:
                                    text_format_italics("Funnily enough")
                                elif navigation_counter == 78:
                                    text_format_italics("mottled")
                                elif navigation_counter == 79:
                                    text_format_italics("substantiate")
                                elif navigation_counter == 80:
                                    text_format_italics("utmost")
                                elif navigation_counter == 81:
                                    text_format_italics("downturn")
                                elif navigation_counter == 82:
                                    text_format_italics("boomeranged")
                                elif navigation_counter == 85:
                                    text_format_italics("unnerved")
                                elif navigation_counter == 86:
                                    text_format_italics("shady")
                                elif navigation_counter == 87:
                                    text_format_italics("writhed in pain")
                                elif navigation_counter == 88:
                                    text_format_italics("imperilled")
                                elif navigation_counter == 89:
                                    text_format_italics("ecstatic")
                                elif navigation_counter == 90:
                                    text_format_italics("dauntless")
                                elif navigation_counter == 91:
                                    text_format_italics("outlandish")
                                elif navigation_counter == 92:
                                    text_format_italics("casual")
                                elif navigation_counter == 93:
                                    text_format_italics("plucky")
                                elif navigation_counter == 94:
                                    text_format_italics("freelance")
                                elif navigation_counter == 95:
                                    text_format_italics("get back at")
                                elif navigation_counter == 96:
                                    text_format_italics("tractable")
                                elif navigation_counter == 97:
                                    text_format_italics("vindictive")
                                elif navigation_counter == 98:
                                    text_format_italics("potency")
                                elif navigation_counter == 99:
                                    text_format_italics("deranged")
                                else:
                                    show_question.insert(INSERT,prevlistQ[navigation_counter])
                                    show_question.configure(state="disabled")
                                    show_question.place(x=width/1.8,y=height/5)
                                radio_value_count_down = 1
                                y_axis_radiobutton_space = 1
                                for a in prevlistOP[navigation_counter]:
                                    show_option = Radiobutton(text=a,variable=variable_storage[navigation_counter][0],value=radio_value_count_down,bg="white")
                                    show_option.place(x=width/1.8,y=250+y_axis_radiobutton_space)
                                    radio_value_count_down += 1
                                    y_axis_radiobutton_space += 30

                        prev_button = Button(text="<< Prev",width=15,bg="green",fg="white",font=("arial",12,"bold"),command=prevQ)
                        prev_button.place(x=width/22,y=height/1.25)


                    question_background = Canvas(bg="white",width=width,height=height/1.8)
                    question_background.place(x=0,y=height/4.3)
                    scrollbar = Scrollbar()
                    scrollbar.place(x=0,y=height/1.4)
                    show_instruction = Text(bg="white",font=("comic sans ms",12),width=width//20,height=height//40,relief=FLAT,wrap=WORD)
                    show_instruction.insert(INSERT,prevlist_IN[navigation_counter])
                    show_instruction.configure(state="disabled")
                    show_instruction.place(x=width/35,y=height/5)
                    scrollbar.config(command=show_instruction.yview)
                    global prevlistQ
                    prevlistQ  = []
                    for display,INSTRUCTION,QUESTION,OPTION in read_four_subject_files:
                        if display == 1:
                            questions = open(QUESTION,"r",encoding="utf8")
                            while True:
                                question = questions.readline()
                                prevlistQ.append(question)
                                if question.endswith("~"):
                                    break
                    global  show_question
                    show_question = Text(bg="white",font=("arial",12),width=int(width//25),height=int(height//70),relief=FLAT,wrap=WORD)
                    show_question.insert(INSERT,prevlistQ[navigation_counter])
                    show_question.configure(state="disabled")
                    show_question.place(x=width/1.8,y=height/5)

                    prevlistOP = []
                    for display,INSTRUCTION,QUESTION,OPTION in read_four_subject_files:
                        if display == 1:
                            options = open(OPTION,"r",encoding="utf8")
                            while True:
                                option = options.readline()
                                x = option.split("_")
                                prevlistOP.append(x)
                                if option.endswith("~"):
                                    break
                    radio_value_count_down = 1
                    y_axis_radiobutton_space = 1
                    for a in prevlistOP[navigation_counter]:
                        show_option = Radiobutton(text=a,variable=variable_storage[navigation_counter][0],value=radio_value_count_down,bg="white")
                        show_option.place(x=width/1.8,y=250+y_axis_radiobutton_space)
                        radio_value_count_down += 1
                        y_axis_radiobutton_space += 30

                    prev_button = Button(text="<< Prev",width=15,bg="green",fg="white",font=("arial",12,"bold"))
                    prev_button.place(x=width/22,y=height/1.25)
                    next_button = Button(text="Next >>",width=15,bg="green",fg="white",font=("arial",12,"bold"),command=nextQ)
                    next_button.place(x=width/1.2,y=height/1.25)
                    calc_button = Button(text="CALCULATOR",width=15,bg="green",fg="white",command=calculator)
                    calc_button.place(x=width/1.4,y=height/6)
                    submit_button = Button(text="Finish",width=15,bg="green",fg="white",command=finish)
                    submit_button.place(x=width/1.2,y=height/6)

                    #instructions.close()
                    #questions.close()
                    #options.close()
                else:
                    messagebox.showinfo(title="Alert",message="your subject combination is not ready")
            else:
                messagebox.showinfo(title="Alert",message="The year you selected is not ready")

        #===================STORINGN OF THE SELECTED SUBJECTS <STARTS HERE>================================================
        Eng = IntVar()
        Acc = IntVar()
        Bio = IntVar()
        Chem = IntVar()
        Comm = IntVar()
        Crk = IntVar()
        Econs = IntVar()
        Geo = IntVar()
        Govt = IntVar()
        Lit = IntVar()
        Math = IntVar()
        Phy = IntVar()
        #===================STORINGN OF THE SELECTED SUBJECTS <ENDS HERE>================================================

        #==================== THE LIST AND LOOP FOR DISPLAYING  ALL SUBJECTS <STARTS HERE>==================================================
        subjects = [("Account",Acc,250),("Biology",Bio,270),("Chemistry",Chem,290),("Commerce",Comm,310),("Crk",Crk,330),
                    ("Economics",Econs,350),("Geography",Geo,370),("Government",Govt,390),("Literature",Lit,410),("Mathematics",Math,430),("Physics",Phy,450)]
        for subject,code,place in subjects:
            English = Checkbutton(text="English",variable=Eng,bg="white",font=("Chromia Condensed",11,"bold"))
            English.place(x=width/16,y=210)
            show = Checkbutton(text=subject,variable=code,bg="white",font=("Chromia Condensed",11,"bold"))
            show.place(x=width/16,y=place)

        #========================YEAR SELECTION CODE STARTS HERE========================================================
        year_store = IntVar()
        year_selection_scrol = Scale(variable = year_store,from_=1990,to=2004,fg="white",bg="green",length=height/3)
        year_selection_scrol.place(x=width/120,y=height/4)


        #========================YEAR SELECTION CODE ENDS HERE========================================================
        #==================== THE LIST AND LOOP FOR DISPLAYING ALL SUBJECTS <ENDS HERE>==================================================
        start_button = Button(text="Get Started >>",font=("comic sans ms",15,"bold"),fg="white",bg="green",activebackground="white",activeforeground="green",command=start)
        start_button.place(x=width/2,y=450)#============== THE GET STARTED BUTTON=========================================
#============================ CONTENTS IN THE HEADING <STARTS HERE>==========================================================================
top_color = Canvas(bg="green", width=width,   height=height/6)
photo = PhotoImage(file="logo.png",width=100,height=100)
pic = top_color.create_image(width/40,height/10,anchor=W,image=photo)
top_color.pack()

logo_name = Label(text="Ule",font=("Chromia Condensed",50,"bold"),fg="white",bg="green")
logo_name.place(x=width/20,y=height/30)
#============================ CONTENTS IN THE HEADING <STARTS HERE>==========================================================================

name_display = Label(text="UTME Reg.No/Username:",font=("arial",15,"bold"))
name_display.place(x=width/5.3,y=height/2.5)

input_field = Entry(textvariable=name_store,font=("comic sans ms",20,"italic"))
input_field.place(x=width/2.7,y=height/2.6)
input_field.insert(0,"E.g. 01234567AZ")

submit_button = Button(text="Submit >>",font=("comic sans ms",15,"bold"),fg="white",bg="green",activebackground="white",activeforeground="green",command=submit)
submit_button.place(x=width/2.3,y=height/2.2)

environment. overrideredirect(True)
environment.mainloop(0)
