# إستدعاء مكاتب الواجعات الرسومية و إعادادات التظام
from config.Libaries import *
# إستدعاء إعدادات النظام
from config.sys_classes import *

# # تحميل ملف الترجمة
# from config.Translations import translations



def Drivers_Managemens_window():
        'شاشة إدارة السائقن'        
        # drivers_list = SQL_DB.fetch_list_drivers_name()
        root = Toplevel()
        root.iconbitmap(sys_icon)
        root.title('👤إدارة المناديب')
        root.geometry('1000x650+300+200')
        root.wm_attributes('-topmost', True)
        sys_class.centering_window(window=root)
        
        f0 = LabelFrame(root, text='تحكم')
        f0.pack(fill='both')

        f01 = LabelFrame(f0, text='إدخال بيانات')
        f01.pack(fill='both', side='right', expand=True)
        
        l0 = Label(f01, text='أسم المندوب')
        l0.pack(fill='both',)

        e0 = Entry(f01)
        e0.pack(fill='both',)
    
        l1 = Label(f01, text='رقم الجوال')
        l1.pack(fill='both',)
    
        e1 = Entry(f01)
        e1.pack(fill='both', )

        l2 = Label(f01, text='رقم الهوية')
        l2.pack(fill='both')
    
        e2 = Entry(f01)
        e2.pack(fill='both', )

        f02 = LabelFrame(f0, text='تحكم')
        f02.pack(fill='both', side='left', padx=3)
        
        def add_new_driver():
            Supa.add_new_driver(id_serial=random.randint(0,121), name=e0.get(),phone=e1.get(),id=e2.get())
            messagebox.showinfo('ملاحضة', 'تم إضافة مندوب جديد', parent=root)
            
            # تنظيف الحقول
            e2.delete(0, END)
            e1.delete(0, END)
            e0.delete(0, END)
            view_drivers.yview(1)

            
            fetch_drivers_data()


        
        b0 = Button(f02, text='➕إضافة', cursor='hand2', bootstyle='info', width=24,
                    command=add_new_driver)
        b0.pack(fill='both', padx=3, pady=3, expand=True)

        b1 = Button(f02, text='🗑️حذف', cursor='hand2', bootstyle='info',)
        b1.pack(fill='both', padx=3, pady=3)
        
        b2 = Button(f02, text='✏️تعديل', cursor='hand2', bootstyle='info',)
        b2.pack(fill='both', padx=3, pady=3)




        f1 = LabelFrame(root, text='بيانات')
        f1.pack(fill='both', expand=True)

        scroDriver = Scrollbar(f1, orient='vertical', cursor='hand2')
        scroDriver.pack(fill='both', side='right')

        view_drivers = Treeview(f1, show='headings', columns=(0,1,2,3,4), cursor='hand2', yscrollcommand=scroDriver.set)
        view_drivers.pack(fill='both', side='left', expand=True)

        scroDriver.config(command=view_drivers.yview)
        
        view_drivers.heading(0, text='رقم الهوية')
        view_drivers.heading(1, text='رقم الجوال')
        view_drivers.heading(2, text='الاسم')
        view_drivers.heading(3, text='رقم الراتب')
        view_drivers.heading(4, text='#.م')
        
        def fetch_drivers_data():
            view_drivers.delete(*view_drivers.get_children())
            c = 0
            for y in Supa.get_driver_list():
                c+=1
                view_drivers.insert('', 'end', values=(y[4],y[2],y[1],y[0],c))
                
        fetch_drivers_data()
        
        root.mainloop()