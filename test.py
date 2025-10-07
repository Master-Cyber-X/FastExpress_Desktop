from config.Libaries import *


class cs():
    def cust_LFR(master,name,):
        return LabelFrame(master=master, text=name)
    def cust_L(master,name):
        return Label(master=master, text=name)
    


root = Window(themename='cyborg')
root.title('Details')
root.geometry('1450x650+200+50')

f0 = cs.cust_L(root, name='')

root.mainloop()