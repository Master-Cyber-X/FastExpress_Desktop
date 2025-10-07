from ttkbootstrap import Window, Frame, Label
from config.Libaries import *

root = Window(themename='cyborg')
root.title('Details')
root.geometry('1450x850+200+50')

scrf = ScrolledFrame(root, bootstyle='secondray')
scrf.pack(fill='both', expand=True)



def shipment_details():
    'تفاصيل الشحنة'
    f0 = LabelFrame(scrf, text='تفاصيل الشحنة', bootstyle='danger')
    f0.pack(fill='both', padx=10, pady=4)

    f00 = Frame(f0, )
    f00.pack(fill='both', side='right')

    l00 = Label(f00, text=':رقم الشحنة', font=('Times',15,'bold'))
    l00.pack(pady=10)

    l01 = Label(f00, text='JED-RYD-90304697', font=('Times',13,'bold'))
    l01.pack(pady=4)

    l02 = Label(f00, text='عدد الطرود', font=('Times',15,'bold'))
    l02.pack(pady=10)

    l03 = Label(f00, text='4', font=('Times',13,'bold'))
    l03.pack(pady=10)

    l04 = Label(f00, text='السعر', font=('Times',15,'bold'))
    l04.pack(pady=10)

    l05 = Label(f00, text='230.00', font=('Times',13,'bold'))
    l05.pack(pady=4, padx=10)

    l06 = Label(f00, text='الوجهه', font=('Times',15,'bold'))
    l06.pack(pady=10)

    l07 = Label(f00, text='RIDHUB', font=('Times',13,'bold'))
    l07.pack(pady=4, padx=10)

shipment_details()




def sender_details():
    'تفاصيل المرسل'
    f0 = LabelFrame(scrf, text='تفاصيل الشحنة', bootstyle='danger')
    f0.pack(fill='both', padx=10, pady=4)

    f00 = Frame(f0, )
    f00.pack(fill='both', side='right')

    l00 = Label(f00, text='أسم المرسل', font=('Times',15,'bold'))
    l00.pack(pady=10)

    l01 = Label(f00, text='عميل-1', font=('Times',13,'bold'))
    l01.pack(pady=4)

    l02 = Label(f00, text=':رقم المرسل', font=('Times',15,'bold'))
    l02.pack(pady=10)

    l03 = Label(f00, text='4', font=('Times',13,'bold'))
    l03.pack(pady=10)

    l04 = Label(f00, text='المدينة', font=('Times',15,'bold'))
    l04.pack(pady=10)

    l05 = Label(f00, text='RIDHUB', font=('Times',13,'bold'))
    l05.pack(pady=4, padx=10)

shipment_details()

root.mainloop()