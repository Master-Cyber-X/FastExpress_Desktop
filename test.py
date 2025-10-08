from ttkbootstrap import Window, Frame, Label
from config.Libaries import *

root = Window(themename='cyborg')
root.title('Details')
root.geometry('1450x850+200+50')

scrf = ScrolledFrame(root, bootstyle='secondray')
scrf.pack(fill='both', expand=True)

# إعدادات ال
py = 10
px = 10
pxv = 30


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

# shipment_details()




def sender_details():
    'تفاصيل المرسل'
    
    b = LabelFrame(scrf, text='بيانات المرسل', bootstyle='danger')
    b.pack(fill='both', padx=px, pady=py)
    
    
    f00 = Frame(b)  # SubFrame> # SubFrame
    f00.pack(fill='both')
    l00 = Label(f00, text='أسم المرسل', font=('Times',15,'bold'))
    l00.pack( padx=px, pady=py, side='right')

    f01 = Frame(b)  # SubFrame> # SubFrame
    f01.pack(fill='both')
    l01 = Label(f01, text='محمد حسن عبدالعزيز الفالحي', font=('Times',13,'bold'))
    l01.pack( padx=pxv, pady=py, side='right')




    f02 = Frame(b)  # SubFrame> # SubFrame
    f02.pack(fill='both')
    l02 = Label(f02, text=':رقم المرسل', font=('Times',15,'bold'))
    l02.pack(padx=px, pady=py, side='right')

    f03 = Frame(b)
    f03.pack(fill='both')
    l03 = Label(f03, text='0587675676', font=('Times',13,'bold'))
    l03.pack(padx=pxv, pady=py, side='right')


    f04 = Frame(b)
    f04.pack(fill='both')
    l04 = Label(f00, text='المدينة', font=('Times',15,'bold'))
    l04.pack(padx=px, pady=py, side='right')

    f05 = Frame(b)
    f05.pack(fill='both')
    l05 = Label(f00, text='RIDHUB', font=('Times',13,'bold'))
    l05.pack(padx=pxv, pady=py, side='right')

# shipment_details()

sender_details()

root.mainloop()