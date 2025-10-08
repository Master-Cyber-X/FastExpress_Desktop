from ttkbootstrap import Window, Frame, Label
from config.Libaries import *

root = Window(themename='flatly')
root.title('Details')
root.geometry('1450x850+200+50')

scrf = ScrolledFrame(root, bootstyle='secondray')
scrf.pack(fill='both', expand=True)

# إعدادات ال
py = 10
px = 10
pxv = 30

head_ft = font=('Times',17,'bold') # Head Title Font
val_ft = font=('Times',13,'bold')  # Value Title Font





def sender_details():
    'تفاصيل المرسل'
    b = LabelFrame(scrf, text='بيانات المرسل', bootstyle='PRIMARY')
    b.pack(fill='both', padx=px, pady=py)
    

    def Right_Frame():
        b0 = Frame(b, bootstyle='danger')
        # b0.pack(fill='both', padx=px, pady=py, side='right')
        b0.grid(row=0, column=2)
        
        f00 = Frame(b0)  # SubFrame> # SubFrame
        f00.pack(fill='both')
        l00 = Label(f00, text='أسم المرسل', font=head_ft)
        l00.pack( padx=px, pady=py, side='right')

        f01 = Frame(b0)  # SubFrame> # SubFrame
        f01.pack(fill='both')
        l01 = Label(f01, text='محمد حسن عبدالعزيز الفالحي', font=val_ft)
        l01.pack( padx=pxv, pady=py, side='right')


        f02 = Frame(b0)  # SubFrame> # SubFrame
        f02.pack(fill='both')
        l02 = Label(f02, text='رقم المرسل', font=head_ft)
        l02.pack(padx=px, pady=py, side='right')

        f03 = Frame(b0)
        f03.pack(fill='both')
        l03 = Label(f03, text='0587675676', font=val_ft)
        l03.pack(padx=pxv, pady=py, side='right')
    


    def Center_Frame():
        b0 = Frame(b, bootstyle='danger')
        # b0.pack(fill='both', padx=px, pady=py)
        b0.grid(row=0, column=1)
        
        f04 = Frame(b0)
        f04.pack(fill='both')
        l04 = Label(f04, text='المدينة', font=head_ft)
        l04.pack(padx=px, pady=py, side='right')

        f05 = Frame(b0)
        f05.pack(fill='both')
        l05 = Label(f05, text='الرياض', font=val_ft)
        l05.pack(padx=pxv, pady=py, side='right')
        
        f06 = Frame(b0)
        f06.pack(fill='both')
        l04 = Label(f06, text='العنوان', font=head_ft)
        l04.pack(padx=px, pady=py, side='right')

        f07 = Frame(b0)
        f07.pack(fill='both')
        l05 = Label(f07, text='الرياض-حي الزهور', font=val_ft)
        l05.pack(padx=pxv, pady=py, side='right')

    def Left_Frame():
        b0 = Frame(b, bootstyle='danger')
        # b0.pack(fill='both', padx=px, pady=py, side='left')
        b0.grid(row=0, column=0)

        f04 = Frame(b0)
        f04.pack(fill='both')
        l04 = Label(f04, text='خطوط الطول', font=head_ft)
        l04.pack(padx=px, pady=py, side='right')

        f05 = Frame(b0)
        f05.pack(fill='both')
        l05 = Label(f05, text='24.54343774677', font=val_ft)
        l05.pack(padx=pxv, pady=py, side='right')
        
        f06 = Frame(b0)
        f06.pack(fill='both')
        l04 = Label(f06, text='خطوط العرض', font=head_ft)
        l04.pack(padx=px, pady=py, side='right')

        f07 = Frame(b0)
        f07.pack(fill='both')
        l05 = Label(f07, text='24.134979718', font=val_ft)
        l05.pack(padx=pxv, pady=py, side='right')

    Right_Frame()
    Left_Frame()
    Center_Frame()

    b.columnconfigure(1, weight=1)



def receiver_details():
    'تفاصيل المستلم'
    b = LabelFrame(scrf, text='بيانات المستلم', bootstyle='PRIMARY')
    b.pack(fill='both', padx=px, pady=py)
    

    def Right_Frame():
        b0 = Frame(b, bootstyle='danger')
        # b0.pack(fill='both', padx=px, pady=py, side='right')
        b0.grid(row=0, column=2)
        
        f00 = Frame(b0)  # SubFrame> # SubFrame
        f00.pack(fill='both')
        l00 = Label(f00, text='أسم المستلم', font=head_ft)
        l00.pack( padx=px, pady=py, side='right')

        f01 = Frame(b0)  # SubFrame> # SubFrame
        f01.pack(fill='both')
        l01 = Label(f01, text='خالد حمد المالكي', font=val_ft)
        l01.pack( padx=pxv, pady=py, side='right')


        f02 = Frame(b0)  # SubFrame> # SubFrame
        f02.pack(fill='both')
        l02 = Label(f02, text='رقم المستلم', font=head_ft)
        l02.pack(padx=px, pady=py, side='right')

        f03 = Frame(b0)
        f03.pack(fill='both')
        l03 = Label(f03, text='0597967914', font=val_ft)
        l03.pack(padx=pxv, pady=py, side='right')
    


    def Center_Frame():
        b0 = Frame(b, bootstyle='danger')
        # b0.pack(fill='both', padx=px, pady=py)
        b0.grid(row=0, column=1)
        
        f04 = Frame(b0)
        f04.pack(fill='both')
        l04 = Label(f04, text='المدينة', font=head_ft)
        l04.pack(padx=px, pady=py, side='right')

        f05 = Frame(b0)
        f05.pack(fill='both')
        l05 = Label(f05, text='الرياض', font=val_ft)
        l05.pack(padx=pxv, pady=py, side='right')
        
        f06 = Frame(b0)
        f06.pack(fill='both')
        l04 = Label(f06, text='العنوان', font=head_ft)
        l04.pack(padx=px, pady=py, side='right')

        f07 = Frame(b0)
        f07.pack(fill='both')
        l05 = Label(f07, text='جدة-حي الزهور', font=val_ft)
        l05.pack(padx=pxv, pady=py, side='right')

    def Left_Frame():
        b0 = Frame(b, bootstyle='danger')
        # b0.pack(fill='both', padx=px, pady=py, side='left')
        b0.grid(row=0, column=0)

        f04 = Frame(b0)
        f04.pack(fill='both')
        l04 = Label(f04, text='خطوط الطول', font=head_ft)
        l04.pack(padx=px, pady=py, side='right')

        f05 = Frame(b0)
        f05.pack(fill='both')
        l05 = Label(f05, text='24.54343774677', font=val_ft)
        l05.pack(padx=pxv, pady=py, side='right')
        
        f06 = Frame(b0)
        f06.pack(fill='both')
        l04 = Label(f06, text='خطوط العرض', font=head_ft)
        l04.pack(padx=px, pady=py, side='right')

        f07 = Frame(b0)
        f07.pack(fill='both')
        l05 = Label(f07, text='24.134979718', font=val_ft)
        l05.pack(padx=pxv, pady=py, side='right')

    Right_Frame()
    Left_Frame()
    Center_Frame()

    b.columnconfigure(1, weight=1)


sender_details()
receiver_details()




root.mainloop()