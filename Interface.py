import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import CTkTable as table

import ProbabilityCalculator as ProbCalc


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")



class App(ctk.CTk):
    cdata = [
        ["No. of Events Occured (n)"],
        ["No. of Events Occured (N)"],
        ["Probability of A occuring: P(A)"],
        ["Probability of A NOT occuring: P(A')"]
    ]

    pdata = [
        ["Total Amount in a Set (n)"],
        ["Amount in Each Subset (r)"],
        ["Total Number of Permutations: nPr"],
        ["Total Number of Combinations: nCr"]
    ]
    
    cpdata = [
        ["Probability of A occuring: P(A)"],
        ["Probability of B occuring: P(B)"],
        ["Probability of A & B: P(C)"],
        ["Probability of B if A Occurs: P(A|B)"],
        ["Probability of A if B Occurs: P(B|A)"],
        ["Probability of B NOT Occuring if A Occurs: P(A|B')"],
        ["Probability of A NOT Occuring if B Occurs: P(B|A')"],
        ["Probability of Union: P(A∪B)"],
        ["Probability of Intersection: P(A∩B)"]
    ]

    idata = [
        ["Probability of A occuring: P(A)"],
        ["Probability of B occuring: P(B)"],
        ["Probability of A NOT occuring: P(A')"],
        ["Probability of B NOT occuring: P(B')"],
        ["Probability of A and B both occuring: P(A∩B)"],
        ["Probability that A or B or both occur: P(A∪B)"],
        ["Probability that A or B occurs but NOT both: P(AΔB)"],
        ["Probability of neither A nor B occuring: P((A∪B)')"],
        ["Probability of A occuring but NOT B"],
        ["Probability of B occuring but NOT A"]
    ]

    def __init__(self):
        super().__init__()

        # Configure Window
        self.title("Probability Caculator")
        self.geometry(f"{1100}x{580}")
        self.after(0, lambda: self.state("zoomed"))

        # Configure Tab View
        self.optionmenu = ctk.CTkTabview(self)
        self.optionmenu.pack(expand=True, fill="both")

        self.optionmenu.add("P(A)")
        self.optionmenu.add("nPr & nCr")
        self.optionmenu.add("P(A|B)")
        self.optionmenu.add("P(A) & P(B)")



        # Classical Probability
        self.cmainframe = ctk.CTkFrame(self.optionmenu.tab("P(A)"))
        self.cmainframe.pack(expand=True, fill="both")
        self.cmainframe.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.cmainframe.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Classical Probability Left Section
        self.clframe = ctk.CTkFrame(
            self.cmainframe, width=140, corner_radius=0, border_width=1
        )
        self.clframe.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.clfield = ctk.CTkFrame(self.clframe, corner_radius=0, border_width=1)
        self.clfield.pack(expand=True, padx=15, pady=15)

        self.clheader = ctk.CTkLabel(
            self.clfield, text="Input", font=ctk.CTkFont(size=50, weight="bold")
        )
        self.clheader.grid(row=0, column=0, columnspan=2, pady=10)

        # Classical Probability Input Field
        self.clabeln1 = ctk.CTkLabel(
            self.clfield,
            text="Event A Frequency",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.clabeln1.grid(row=1, column=0, columnspan=2, pady=(15, 0))
        self.clabeln2 = ctk.CTkLabel(
            self.clfield, text="(n)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.clabeln2.grid(row=2, column=0, pady=15)
        self.centryn = ctk.CTkEntry(
            self.clfield, height=35, width=100, font=ctk.CTkFont(size=20, weight="bold")
        )
        self.centryn.grid(row=2, column=1, pady=15)

        self.clabelN1 = ctk.CTkLabel(
            self.clfield,
            text="Possible Outcomes",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.clabelN1.grid(row=3, column=0, columnspan=2, padx=70, pady=(15, 0))
        self.clabelN2 = ctk.CTkLabel(
            self.clfield, text="(N)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.clabelN2.grid(row=4, column=0, pady=15)
        self.centryN = ctk.CTkEntry(
            self.clfield, height=35, width=100, font=ctk.CTkFont(size=20, weight="bold")
        )
        self.centryN.grid(row=4, column=1, pady=15)

        self.cnote1 = ctk.CTkLabel(
            self.clfield,
            text="*Enter Only Positive Integers*",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#808080",
        )
        self.cnote1.grid(row=5, column=0, columnspan=2)
        self.cnote2 = ctk.CTkLabel(
            self.clfield,
            text="*(n) Must be bigger than (N)*",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#808080",
        )
        self.cnote2.grid(row=6, column=0, columnspan=2)

        # Classical Probability Buttons
        self.ccalculate = ctk.CTkButton(
            self.clfield,
            text="Calculate",
            height=50,
            width=150,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.cCheckInput,
        )
        self.ccalculate.grid(row=7, column=0, columnspan=2, pady=(15, 0))
        self.cclear = ctk.CTkButton(
            self.clfield,
            fg_color="#5A5A5A",
            text="Clear",
            height=50,
            width=150,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.cClearInput,
        )
        self.cclear.grid(row=8, column=0, columnspan=2, pady=15)

        # Classical Probability Right Section
        self.crframe = ctk.CTkFrame(self.cmainframe, corner_radius=0, border_width=1)
        self.crframe.grid(row=0, column=1, rowspan=4, columnspan=3, sticky="nsew")

        self.crfield = ctk.CTkFrame(self.crframe, corner_radius=0, border_width=1)
        self.crfield.pack(expand=True)

        self.crheader = ctk.CTkLabel(
            self.crfield,
            text="Classical Probability Results",
            font=ctk.CTkFont(size=40, weight="bold"),
        )
        self.crheader.pack(pady=10)

        self.coutput = table.CTkTable(
            master=self.crfield, row=4, column=2, values=self.cdata, font=("Arial", 30)
        )
        self.coutput.pack(expand=True, padx=15, pady=15)



        # Permutation & Combination
        self.pmainframe = ctk.CTkFrame(self.optionmenu.tab("nPr & nCr"))
        self.pmainframe.pack(expand=True, fill="both")
        self.pmainframe.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.pmainframe.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.plframe = ctk.CTkFrame(
            self.pmainframe, width=140, corner_radius=0, border_width=1
        )
        self.plframe.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.plfield = ctk.CTkFrame(self.plframe, corner_radius=0, border_width=1)
        self.plfield.pack(expand=True, padx=15, pady=15)

        self.plheader = ctk.CTkLabel(
            self.plfield, text="Input", font=ctk.CTkFont(size=50, weight="bold")
        )
        self.plheader.grid(row=0, column=0, columnspan=2, pady=10)

        # Permutation & Combination Input Field
        self.plabeln1 = ctk.CTkLabel(
            self.plfield,
            text="Total Amount in Set",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.plabeln1.grid(row=1, column=0, columnspan=2, pady=(15, 0))
        self.plabeln2 = ctk.CTkLabel(
            self.plfield, text="(n)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.plabeln2.grid(row=2, column=0, pady=15)
        self.pentryn = ctk.CTkEntry(
            self.plfield, height=35, width=100, font=ctk.CTkFont(size=20, weight="bold")
        )
        self.pentryn.grid(row=2, column=1, pady=15)

        self.plabelr1 = ctk.CTkLabel(
            self.plfield,
            text="Amount in Each Subset",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.plabelr1.grid(row=3, column=0, columnspan=2, padx=46.5, pady=(15, 0))
        self.plabelr2 = ctk.CTkLabel(
            self.plfield, text="(r)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.plabelr2.grid(row=4, column=0, pady=15)
        self.pentryr = ctk.CTkEntry(
            self.plfield, height=35, width=100, font=ctk.CTkFont(size=20, weight="bold")
        )
        self.pentryr.grid(row=4, column=1, pady=15)

        self.pnote1 = ctk.CTkLabel(
            self.plfield,
            text="*Enter Only Positive Integers*",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#808080",
        )
        self.pnote1.grid(row=5, column=0, columnspan=2)
        self.pnote2 = ctk.CTkLabel(
            self.plfield,
            text="*(n) Must be bigger than (r)*",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#808080",
        )
        self.pnote2.grid(row=6, column=0, columnspan=2)

        # Permutation & Combination Buttons
        self.pcalculate = ctk.CTkButton(
            self.plfield,
            text="Calculate",
            height=50,
            width=150,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.pCheckInput,
        )
        self.pcalculate.grid(row=7, column=0, columnspan=2, pady=(15, 0))
        self.pclear = ctk.CTkButton(
            self.plfield,
            fg_color="#5A5A5A",
            text="Clear",
            height=50,
            width=150,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.pClearInput,
        )
        self.pclear.grid(row=8, column=0, columnspan=2, pady=15)

        # Permutation & Combination Right Section
        self.prframe = ctk.CTkFrame(self.pmainframe, corner_radius=0, border_width=1)
        self.prframe.grid(row=0, column=1, rowspan=4, columnspan=3, sticky="nsew")

        self.prfield = ctk.CTkFrame(self.prframe, corner_radius=0, border_width=1)
        self.prfield.pack(expand=True)

        self.prheader = ctk.CTkLabel(
            self.prfield,
            text="Permutation & Combination Results",
            font=ctk.CTkFont(size=40, weight="bold"),
        )
        self.prheader.pack(pady=10)

        self.poutput = table.CTkTable(
            master=self.prfield, row=4, column=2, values=self.pdata, font=("Arial", 30)
        )
        self.poutput.pack(expand=True, padx=15, pady=15)



        # Conditional Probability
        self.cpmainframe = ctk.CTkFrame(self.optionmenu.tab("P(A|B)"))
        self.cpmainframe.pack(expand=True, fill="both")
        self.cpmainframe.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.cpmainframe.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.cplframe = ctk.CTkFrame(
            self.cpmainframe, width=140, corner_radius=0, border_width=1
        )
        self.cplframe.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.cplfield = ctk.CTkFrame(self.cplframe, corner_radius=0, border_width=1)
        self.cplfield.pack(expand=True, padx=65, pady=15)

        self.cplheader = ctk.CTkLabel(
            self.cplfield, text="Input", font=ctk.CTkFont(size=50, weight="bold")
        )
        self.cplheader.grid(row=0, column=0, columnspan=2, pady=10)

        # Conditional Probability Input Field
        self.cplabelA1 = ctk.CTkLabel(
            self.cplfield,
            text="Probability of A",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.cplabelA1.grid(row=1, column=0, columnspan=2, pady=(15, 0))
        self.cplabelA2 = ctk.CTkLabel(
            self.cplfield, text="P(A)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.cplabelA2.grid(row=2, column=0, pady=15)
        self.cpentryA = ctk.CTkEntry(
            self.cplfield,
            height=35,
            width=100,
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.cpentryA.grid(row=2, column=1, pady=15)

        self.cplabelB1 = ctk.CTkLabel(
            self.cplfield,
            text="Probability of B",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.cplabelB1.grid(row=3, column=0, columnspan=2, padx=46.5, pady=(15, 0))
        self.cplabelB2 = ctk.CTkLabel(
            self.cplfield, text="P(B)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.cplabelB2.grid(row=4, column=0, pady=15)
        self.cpentryB = ctk.CTkEntry(
            self.cplfield,
            height=35,
            width=100,
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.cpentryB.grid(row=4, column=1, pady=15)

        self.cpoption = ctk.CTkOptionMenu(
            self.cplfield,
            height=50,
            width=175,
            values=["Union", "Intersection"],
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.cpoption.grid(row=5, column=0, columnspan=2, pady=15)

        self.cplabelC1 = ctk.CTkLabel(
            self.cplfield,
            text="Probability of A & B",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.cplabelC1.grid(row=6, column=0, columnspan=2, padx=46.5, pady=(15, 0))
        self.cplabelC2 = ctk.CTkLabel(
            self.cplfield, text="P(C)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.cplabelC2.grid(row=7, column=0, pady=15)
        self.cpentryC = ctk.CTkEntry(
            self.cplfield,
            height=35,
            width=100,
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.cpentryC.grid(row=7, column=1, pady=15)

        self.cpnote1 = ctk.CTkLabel(
            self.cplfield,
            text="*Input values between 0 and 1*",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#808080",
        )
        self.cpnote1.grid(row=8, column=0, columnspan=2, padx=50)

        # Conditional Probability Buttons
        self.cpcalculate = ctk.CTkButton(
            self.cplfield,
            text="Calculate",
            height=50,
            width=150,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.cpCheckInput
        )
        self.cpcalculate.grid(row=9, column=0, columnspan=2, pady=(15, 0))
        self.cpclear = ctk.CTkButton(
            self.cplfield,
            fg_color="#5A5A5A",
            text="Clear",
            height=50,
            width=150,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.cpClearInput
        )
        self.cpclear.grid(row=10, column=0, columnspan=2, pady=15)
        
        # Permutation & Combination Right Section
        self.cprframe = ctk.CTkFrame(self.cpmainframe, corner_radius=0, border_width=1)
        self.cprframe.grid(row=0, column=1, rowspan=4, columnspan=3, sticky="nsew")

        self.cprfield = ctk.CTkFrame(self.cprframe, corner_radius=0, border_width=1)
        self.cprfield.pack(expand=True)

        self.cprheader = ctk.CTkLabel(
            self.cprfield,
            text="Conditional Probability Results",
            font=ctk.CTkFont(size=40, weight="bold"),
        )
        self.cprheader.pack(pady=10)

        self.cpoutput = table.CTkTable(
            master=self.cprfield, row=9, column=2, values=self.cpdata, font=("Arial", 30)
        )
        self.cpoutput.pack(expand=True, padx=15, pady=15)
        
        

        # Independent Events
        self.imainframe = ctk.CTkFrame(self.optionmenu.tab("P(A) & P(B)"))
        self.imainframe.pack(expand=True, fill="both")
        self.imainframe.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.imainframe.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.ilframe = ctk.CTkFrame(
            self.imainframe, width=140, corner_radius=0, border_width=1
        )
        self.ilframe.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.ilfield = ctk.CTkFrame(self.ilframe, corner_radius=0, border_width=1)
        self.ilfield.pack(expand=True, padx=65, pady=15)

        self.ilheader = ctk.CTkLabel(
            self.ilfield, text="Input", font=ctk.CTkFont(size=50, weight="bold")
        )
        self.ilheader.grid(row=0, column=0, columnspan=2, pady=10)

        # Independent Events Input Field
        self.ilabelA1 = ctk.CTkLabel(
            self.ilfield,
            text="Probability of A",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.ilabelA1.grid(row=1, column=0, columnspan=2, pady=(15, 0))
        self.ilabelA2 = ctk.CTkLabel(
            self.ilfield, text="P(A)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.ilabelA2.grid(row=2, column=0, pady=15)
        self.ientryA = ctk.CTkEntry(
            self.ilfield, height=35, width=100, font=ctk.CTkFont(size=20, weight="bold")
        )
        self.ientryA.grid(row=2, column=1, pady=15)

        self.ilabelB1 = ctk.CTkLabel(
            self.ilfield,
            text="Probability of B",
            font=ctk.CTkFont(size=25, weight="bold"),
        )
        self.ilabelB1.grid(row=3, column=0, columnspan=2, pady=(15, 0))
        self.ilabelB2 = ctk.CTkLabel(
            self.ilfield, text="P(B)", font=ctk.CTkFont(size=25, weight="bold")
        )
        self.ilabelB2.grid(row=4, column=0, pady=15)
        self.ientryB = ctk.CTkEntry(
            self.ilfield, height=35, width=100, font=ctk.CTkFont(size=20, weight="bold")
        )
        self.ientryB.grid(row=4, column=1, pady=15)

        self.inote1 = ctk.CTkLabel(
            self.ilfield,
            text="*Input values between 0 and 1*",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#808080",
        )
        self.inote1.grid(row=5, column=0, columnspan=2, padx=50)

        # Independent Events Buttons
        self.icalculate = ctk.CTkButton(
            self.ilfield,
            text="Calculate",
            height=50,
            width=150,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.iCheckInput,
        )
        self.icalculate.grid(row=6, column=0, columnspan=2, pady=(15, 0))
        self.iclear = ctk.CTkButton(
            self.ilfield,
            fg_color="#5A5A5A",
            text="Clear",
            height=50,
            width=150,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.iClearInput,
        )
        self.iclear.grid(row=7, column=0, columnspan=2, pady=15)

        # Independent Events Right Section
        self.irframe = ctk.CTkFrame(self.imainframe, corner_radius=0, border_width=1)
        self.irframe.grid(row=0, column=1, rowspan=4, columnspan=3, sticky="nsew")

        self.irfield = ctk.CTkFrame(self.irframe, corner_radius=0, border_width=1)
        self.irfield.pack(expand=True)

        self.irheader = ctk.CTkLabel(
            self.irfield,
            text="Independent Events Results",
            font=ctk.CTkFont(size=40, weight="bold"),
        )
        self.irheader.pack(pady=10)

        self.ioutput = table.CTkTable(
            master=self.irfield, row=10, column=2, values=self.idata, font=("Arial", 30)
        )
        self.ioutput.pack(expand=True, padx=15, pady=15)



    def cCheckInput(self):
        try:
            self.cinputn = int(self.centryn.get())
            self.cinputN = int(self.centryN.get())

            if self.cinputn <= self.cinputN:
                self.cCalculate(self.cinputn, self.cinputN)
            else:
                self.cClearInput()
                messagebox.showerror(
                    title="Error Input", message="(N) MUST BE BIGGER THAN (n)!"
                )
        except:
            self.cClearInput()
            messagebox.showerror(title="Error Input", message="INVALID INPUT!")

    def cClearInput(self):
        self.centryn.delete(0, tk.END)
        self.centryN.delete(0, tk.END)
        
        for i in range(len(self.cdata)):
            self.coutput.delete(row=i, column=1)

    def cCalculate(self, n, N):
        cresults = ProbCalc.classicalProbability(n, N)
        
        for i in range(len(self.cdata)):
            self.coutput.insert(row=i, column=1, value=cresults[i])



    def pCheckInput(self):
        try:
            self.pinputn = int(self.pentryn.get())
            self.pinputr = int(self.pentryr.get())

            if self.pinputr < self.pinputn:
                self.pCalculate(self.pinputn, self.pinputr)
            else:
                self.pClearInput()
                messagebox.showerror(
                    title="Error Input", message="(n) MUST BE BIGGER THAN (r)!"
                )
        except:
            self.pClearInput()
            messagebox.showerror(title="Error Input", message="INVALID INPUT!")

    def pClearInput(self):
        self.pentryn.delete(0, tk.END)
        self.pentryr.delete(0, tk.END)
        
        for i in range(len(self.pdata)):
            self.poutput.delete(row=i, column=1)

    def pCalculate(self, n, r):
        presults = ProbCalc.permcombCalculator(n, r)
        
        for i in range(len(self.pdata)):
            self.poutput.insert(row=i, column=1, value=presults[i])
            
            

    def cpCheckInput(self):
        try:
            self.cpinputA = float(self.cpentryA.get())
            self.cpinputB = float(self.cpentryB.get())
            self.cpoptioninput = self.cpoption.get()
            self.cpinputC = float(self.cpentryC.get())
            

            if (
                (self.cpinputA >= 0 and self.cpinputA <= 1)
                and (self.cpinputB >= 0 and self.cpinputB <= 1)
                and (self.cpinputC >= 0 and self.cpinputC <= 1)
            ):
                if self.cpoptioninput == "Union":
                    if (self.cpinputC >= self.cpinputA) and (self.cpinputC >= self.cpinputB):
                        self.cpCalculate(self.cpinputA, self.cpinputB, 1, self.cpinputC)
                    else:
                        self.cpClearInput()
                        messagebox.showerror(title="Error Input", message="UNION MUST BE GREATER THAN P(A) AND P(B)!")
                elif self.cpoptioninput == "Intersection":
                    if (self.cpinputC <= self.cpinputA) and (self.cpinputC <= self.cpinputB):
                        self.cpCalculate(self.cpinputA, self.cpinputB, 2, self.cpinputC)
                    else:
                        self.cpClearInput()
                        messagebox.showerror(title="Error Input", message="INTERSECTION MUST BE LESS THAN P(A) AND P(B)!")
                
            else:
                self.cpClearInput()
                messagebox.showerror(
                    title="Error Input", message="PLEASE INPUT VALUES BETWEEN 0 AND 1!"
                )
        except:
            self.cpClearInput()
            messagebox.showerror(title="Error Input", message="INVALID INPUT!")

    def cpClearInput(self):
        self.cpentryA.delete(0, tk.END)
        self.cpentryB.delete(0, tk.END)
        self.cpentryC.delete(0, tk.END)
        
        for i in range(len(self.cpdata)):
            self.cpoutput.delete(row=i, column=1)
        
    def cpCalculate(self, A, B, mode, C):
        cpresults = ProbCalc.conditionalProbability(A, B, mode, C)
        
        for i in range(len(self.cpdata)):
            self.cpoutput.insert(row=i, column=1, value=cpresults[i])



    def iCheckInput(self):
        try:
            self.iinputA = float(self.ientryA.get())
            self.iinputB = float(self.ientryB.get())

            if (self.iinputA >= 0 and self.iinputA <= 1) and (
                self.iinputB >= 0 and self.iinputB <= 1
            ):
                self.iCalculate(self.iinputA, self.iinputB)
            else:
                self.iClearInput()
                messagebox.showerror(
                    title="Error Input", message="PLEASE INPUT VALUES BETWEEN 0 AND 1!"
                )
        except:
            self.iClearInput()
            messagebox.showerror(title="Error Input", message="INVALID INPUT!")

    def iClearInput(self):
        self.ientryA.delete(0, tk.END)
        self.ientryB.delete(0, tk.END)
        
        for i in range(len(self.idata)):
            self.ioutput.delete(row=i, column=1)
        
    def iCalculate(self, A, B):
        iresults = ProbCalc.independentProbability(A, B)
        
        for i in range(len(self.idata)):
            self.ioutput.insert(row=i, column=1, value=iresults[i])



probabilitycalculator = App()
probabilitycalculator.mainloop()