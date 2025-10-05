# إستدعاء مكاتب الواجعات الرسومية و إعادادات التظام
from config.Libaries import *
# إستدعاء إعدادات النظام
from config.sys_classes import *
#Supabase الأتصال بقاعدة البيانات
from Data.Supa import Supa

def Drivers_Managemens_window():
        'شاشة إدارة السائقن'
        root = Toplevel()
        root.title('👤إدارة المناديب')
        root.geometry('650x650+50+20')

        
        # drivers_list = SQL_DB.fetch_list_drivers_name()
        t = Toplevel()
        t.iconbitmap(sys_icon)
        t.title('إدارة المناديب')
        t.geometry('700x650+300+200')
        t.wm_attributes('-topmost', True)
        sys_class.centering_window(window=t)
        
        f0 = LabelFrame(t, text='تحكم')
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
        f02.pack(fill='both', side='left', padx=3, expand=True)
        
        def add_new_driver():
            # SQL_DB.add_new_driver(id=e2.get(),name=e0.get(),phone=e1.get())
            messagebox.showinfo('ملاحضة', 'تم إضافة مندوب جديد', parent=t)
            t.focus_set()
            # choose_driver_name.set(value=[])
            # choose_driver_name.configure(value=SQL_DB.fetch_list_drivers_name())
            choose_driver_name.update()
            # choose_driver_name_search.configure(value=SQL_DB.fetch_list_drivers_name())
        
        b0 = Button(f02, text='➕إضافة', cursor='hand2', bootstyle='info',
                    command=add_new_driver)
        b0.pack(fill='both', padx=3, pady=3, expand=True)

        b1 = Button(f02, text='🗑️حذف', cursor='hand2', bootstyle='info',)
        b1.pack(fill='both', padx=3, pady=3)
        
        b2 = Button(f02, text='✏️تعديل', cursor='hand2', bootstyle='info',)
        b2.pack(fill='both', padx=3, pady=3)




        f1 = LabelFrame(t, text='بيانات')
        f1.pack(fill='both', expand=True)

        scroDriver = Scrollbar(f1, orient='vertical', cursor='hand2')
        scroDriver.pack(fill='both', side='right')

        view_drivers = Treeview(f1, show='headings', columns=(0,1,2,3), cursor='hand2')
        view_drivers.pack(fill='both', side='left', expand=True)
        
        view_drivers.heading(0, text='رقم الهوية')
        view_drivers.heading(1, text='رقم الجوال')
        view_drivers.heading(2, text='الاسم')
        view_drivers.heading(3, text='#.م')
        
        def fetch_drivers_data():
            view_drivers.delete(*view_drivers.get_children())
            c = 0
            # for y in SQL_DB.fetch_drivers_data():
            #     c+=1
            #     view_drivers.insert('', 'end', values=(y[0],y[1],y[2],c))
        fetch_drivers_data()
        
        t.mainloop()
    

