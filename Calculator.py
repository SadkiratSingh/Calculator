from tkinter import *
from tkinter import ttk

class Calculator:
    calc_value=0.0
    div_trigger=False
    mul_trigger=False
    add_trigger=False
    sub_trigger=False

    def button_press(self,value):

        if value=='AC':
            Calculator.div_trigger=False
            Calculator.mul_trigger=False
            Calculator.add_trigger=False
            Calculator.sub_trigger=False
            self.number_entry.delete(0,'end')
        else:
            entry_val=self.number_entry.get()
            entry_val+=value
            self.number_entry.delete(0,'end')
            self.number_entry.insert(0,entry_val)
    
    def is_Float(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def math_button_press(self,value):

        if(self.is_Float(self.number_entry.get())):
            Calculator.div_trigger=False
            Calculator.mul_trigger=False
            Calculator.add_trigger=False
            Calculator.sub_trigger=False
            Calculator.calc_value=float(self.entry_value.get())
            if value=='/':
                Calculator.div_trigger=True
            elif value=='*':
                Calculator.mul_trigger=True
            elif value=='+':
                Calculator.add_trigger=True
            else:
                Calculator.sub_trigger=True
            self.number_entry.delete(0,'end')
    
    def equal_button_press(self):
        if(Calculator.add_trigger or Calculator.sub_trigger or Calculator.div_trigger or Calculator.mul_trigger )and self.is_Float(self.number_entry.get()):
            if Calculator.add_trigger:
                solution=Calculator.calc_value+float(self.entry_value.get())
            elif Calculator.sub_trigger:
                solution=Calculator.calc_value-float(self.entry_value.get())
            elif Calculator.div_trigger:
                solution=Calculator.calc_value/float(self.entry_value.get())
            else:
                solution=Calculator.calc_value*float(self.entry_value.get())
            self.number_entry.delete(0,'end')
            self.number_entry.insert(0,str(solution))

    def __init__(self,root):
        self.entry_value=StringVar(root,value='')
        root.title("Calculator")
        root.geometry("480x220")
        root.resizable(width=False,height=False)

        style=ttk.Style(root)
        style.configure("TButton",
                        font='Serif 11',
                        padding=10)
        style.configure("TEntry",
                        font='Serif 18',
                        padding=10)

        self.number_entry=ttk.Entry(root,textvariable=self.entry_value,width=76)
        self.number_entry.grid(row=0,column=0,columnspan=4,sticky='we')

        self.button7=ttk.Button(root,text='7',command=lambda:self.button_press('7')).grid(column=0,row=1,sticky='we')
        self.button8=ttk.Button(root,text='8',command=lambda:self.button_press('8')).grid(column=1,row=1,sticky='we')
        self.button9=ttk.Button(root,text='9',command=lambda:self.button_press('9')).grid(column=2,row=1,sticky='we')
        self.button_div=ttk.Button(root,text='/',command=lambda:self.math_button_press('/')).grid(column=3,row=1,sticky='we')

        self.button4=ttk.Button(root,text='4',command=lambda:self.button_press('4')).grid(column=0,row=2,sticky='we')
        self.button5=ttk.Button(root,text='5',command=lambda:self.button_press('5')).grid(column=1,row=2,sticky='we')
        self.button6=ttk.Button(root,text='6',command=lambda:self.button_press('6')).grid(column=2,row=2,sticky='we')
        self.button_mul=ttk.Button(root,text='*',command=lambda:self.math_button_press('*')).grid(column=3,row=2,sticky='we')

        self.button3=ttk.Button(root,text='1',command=lambda:self.button_press('1')).grid(column=0,row=3,sticky='we')
        self.button2=ttk.Button(root,text='2',command=lambda:self.button_press('2')).grid(column=1,row=3,sticky='we')
        self.button1=ttk.Button(root,text='3',command=lambda:self.button_press('3')).grid(column=2,row=3,sticky='we')
        self.button_plus=ttk.Button(root,text='+',command=lambda:self.math_button_press('+')).grid(column=3,row=3,sticky='we')

        self.button_clear=ttk.Button(root,text='AC',command=lambda:self.button_press('AC')).grid(column=0,row=4,sticky='we')
        self.button0=ttk.Button(root,text='0',command=lambda:self.button_press('0')).grid(column=1,row=4,sticky='we')
        self.button_equal=ttk.Button(root,text='=',command=lambda:self.equal_button_press()).grid(column=2,row=4,sticky='we')
        self.button_sub=ttk.Button(root,text='-',command=lambda:self.math_button_press('-')).grid(column=3,row=4,sticky='we')

if __name__=='__main__':
    root=Tk()
    calc=Calculator(root)
    root.mainloop()
