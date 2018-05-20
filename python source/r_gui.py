#!/usr/bin/python3
try:
    print("trying to load Tkinter")
    import Tkinter as TK
    from Tkinter import N, S, E, W, END
except ImportError:
    print("loading Tkinter failed, trying tkinter instead")
    import tkinter as TK
    from tkinter import N, S, E, W, END
    from tkinter import messagebox
    from tkinter import Frame, Label, Entry, Button
    import xml.dom.minidom

class r_gui:
    form = TK.Tk()
    toplevel = form

    def center(self):
        self.toplevel.update_idletasks()
        w = self.toplevel.winfo_screenwidth()
        h = self.toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in self.toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def r_MainApp(self):
        #self.center()
        
        form = self.form
        # Code to add widgets will go here...
        self.form.wm_title('File Parser')

        stepOne = TK.LabelFrame(form, text=" 1. Enter File Details: ")
        stepOne.grid(row=0, columnspan=7, sticky='W',
                 padx=5, pady=5, ipadx=5, ipady=5)

        helpLf = TK.LabelFrame(form, text=" Quick Help ")
        helpLf.grid(row=0, column=9, columnspan=2, rowspan=8,
                sticky='NS', padx=5, pady=5)
        helpLbl = TK.Label(helpLf, text="Help will come - ask for it.")
        helpLbl.grid(row=0) 

        stepTwo = TK.LabelFrame(form, text=" 2. Enter Table Details: ")
        stepTwo.grid(row=2, columnspan=7, sticky='W',
                    padx=5, pady=5, ipadx=5, ipady=5)

        stepThree = TK.LabelFrame(form, text=" 3. Configure: ")
        stepThree.grid(row=3, columnspan=7, sticky='W',
                    padx=5, pady=5, ipadx=5, ipady=5)

        inFileLbl = TK.Label(stepOne, text="Select the File:")
        inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)

        inFileTxt = TK.Entry(stepOne)
        inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

        inFileBtn = TK.Button(stepOne, text="Browse ...")
        inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)

        outFileLbl = TK.Label(stepOne, text="Save File to:")
        outFileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)

        outFileTxt = TK.Entry(stepOne)
        outFileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

        outFileBtn = TK.Button(stepOne, text="Browse ...")
        outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)

        inEncLbl = TK.Label(stepOne, text="Input File Encoding:")
        inEncLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2)

        inEncTxt = TK.Entry(stepOne)
        inEncTxt.grid(row=2, column=1, sticky='E', pady=2)

        outEncLbl = TK.Label(stepOne, text="Output File Encoding:")
        outEncLbl.grid(row=2, column=5, padx=5, pady=2)

        outEncTxt = TK.Entry(stepOne)
        outEncTxt.grid(row=2, column=7, pady=2)

        outTblLbl = TK.Label(stepTwo,
                                text="Enter the name of the table to be used in the statements:")
        outTblLbl.grid(row=3, column=0, sticky='W', padx=5, pady=2)

        outTblTxt = TK.Entry(stepTwo)
        outTblTxt.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE')

        fldLbl = TK.Label(stepTwo,
                            text="Enter the field (column) names of the table:")
        fldLbl.grid(row=4, column=0, padx=5, pady=2, sticky='W')

        getFldChk = TK.Checkbutton(stepTwo,
                                        text="Get fields automatically from input file",
                                        onvalue=1, offvalue=0)
        getFldChk.grid(row=4, column=1, columnspan=3, pady=2, sticky='WE')

        fldRowTxt = TK.Entry(stepTwo)
        fldRowTxt.grid(row=5, columnspan=5, padx=5, pady=2, sticky='WE')

        transChk = TK.Checkbutton(stepThree,
                                    text="Enable Transaction", onvalue=1, offvalue=0)
        transChk.grid(row=6, sticky='W', padx=5, pady=2)

        transRwLbl = TK.Label(stepThree,
                                text=" => Specify number of rows per transaction:")
        transRwLbl.grid(row=6, column=2, columnspan=2,
                        sticky='W', padx=5, pady=2)

        transRwTxt = TK.Entry(stepThree)
        transRwTxt.grid(row=6, column=4, sticky='WE')

        self.toplevel.mainloop()


