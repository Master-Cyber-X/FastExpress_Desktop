# إستدعاء مكاتب الواجعات الرسومية و إعادادات التظام
from config.Libaries import *
# إستدعاء إعدادات النظام
from config.sys_classes import *
#Supabase الأتصال بقاعدة البيانات
from Data.Cloud_Supabase.Supa import Supa


def View_order_details_frame(master):

    # frame_viewers_tools_1 = Frame()
    # frame_viewers_tools_1.pack()




    def fetch_order_data(driver):
        controller_report_treeview.delete(*controller_report_treeview.get_children())
        # supabase جلب البيانات من قاعدة بيانات
        data = Supa.fetch_order_data(driver=driver)
        # add < [0] befor using> sqlite3 جلب البيانات من قاعدة بيانات
        # data = SQL_DB.fetch_order_data(driver=driver)
        for x in data:
            # print(x)
            controller_report_treeview.insert('','end', values=(x))
            # controller_report_treeview.insert('','end', values=(x['id_serial'],x['order_id_shipment'],f"{float(x["price"]):,.2f}",x["customer_phone"],x['customer_name'],x['driver'],(x['date_creation'],x['time_creation']),x['notes']))
    
        # "جلب الشحنات التي تحت المعالجة"
        # controller_report_treeview.delete(*controller_report_treeview.get_children())
        # datalist = SQL_DB.fetch_order_data(driver)
        # countLine = 0
        # # print(datalist)
        # for x in datalist[0]:
        #     countLine +=1
        #     controller_report_treeview.insert('','end', values=(x[0],x[3],f"{x[7]:,.2f}",x[6],x[5],x[8],(x[10],x[11]),x[9],countLine))
        # controller_report_treeview.yview_moveto(1)
        # total_entry.delete(0, END)
        # total_entry.insert(0, datalist[1])
        # total_orders_entry.delete(0, END)
        # total_orders_entry.insert(0, datalist[2])
        # analyzer_data()
    
    # button_search = Button(frame_viewers_tools_2, text='🔍بحث',
    #                         cursor='hand2', bootstyle='info', command=fetch_order_data)
    # button_search.pack(fill='both', pady=4, padx=4, side='right', expand=True)
    
    def fetch_recorder_info():
        'جلب بيانات فاتورة التوصيل'
        item = controller_report_treeview.item(controller_report_treeview.selection(),'values'[0])
        # show_recorder_detials(id=item, option='SHOW')

    def receive_order():
        'تغيير حالة السجل إلى تم التسليم'
        item = controller_report_treeview.item(controller_report_treeview.selection(),'values'[0][0])

        # في حالة انهو لم يتم تعيين السائق
        if item[5] == 'غير معرف':
            messagebox.showwarning('ملاحضة', 'يرجى تعيين المندوب', parent=master)
            return
        
        if item =='':
            messagebox.showwarning('ملاحضة', 'يرجى إختيار السجل أولاء', parent=master)
            return
        
        # sqlite3 تحصيل من
        # SQL_DB.receive_order(id=item[0])
        # supabase تحصيل من
        Supa.receive_order(serial=item[0]) 
        # تحديث السجل
        fetch_order_data(driver=driver_var_controller.get())
        messagebox.showinfo('ملاحضة', f'تم تسليم السجل {item[0]}', parent=master)
        
        

    # button_recevie_recorders = Button(frame_viewers_tools_2, text='💵تسليم',
    #                         cursor='hand2', bootstyle='info', command=receive_order)
    # button_recevie_recorders.pack(fill='both', pady=4, padx=4, side='left', expand=True)
    
    # button_get_all_recorder_info = Button(frame_viewers_tools_2, text='ℹ️معلومات',
    #                         cursor='hand2', bootstyle='info', command=fetch_recorder_info)
    # button_get_all_recorder_info.pack(fill='both', pady=4, padx=4, side='left', expand=True)






    
    def trace_drivers_name(*args):
        'للبحث عن بأسم المندوب'
        driver = driver_var_controller.get()
        fetch_order_data(driver=driver)

    driver_var_controller = StringVar()




    # فريم عرض بيانات التقرير
    frame_viewers_rpeort = LabelFrame(master, text='فريم عرض التحكم بالتقرير')
    frame_viewers_rpeort.pack(fill='both', expand=True)
    
    report_scroller = Scrollbar(frame_viewers_rpeort, orient='vertical', cursor='hand2')
    report_scroller.pack(fill='both', side='right')


    style = Style()
    # شجرة عرض البيانات
    controller_report_treeview = Treeview(frame_viewers_rpeort, cursor='hand2',
                            columns=(0,1,2,3,4,5,6,7,8), show='headings', bootstyle='DANGER', yscrollcommand=report_scroller.set)
    controller_report_treeview.pack(fill='both', side='left', expand=True, padx=1)

    def treeview_setting():
        'إعداد العرض الشجري'
        # Treeview And Scrollerbar إنشاء أتصال بين 
        report_scroller.config(command=controller_report_treeview.yview)

        
        style.configure('Treeview.Heading', font=('Times',13,'bold'))
        style.configure('Treeview', font=('Times',12,'bold'))
        # style.configure('Treeview', rowheight=130)
        style.configure('TButton', font=('Times',13,'bold'))
        style.configure('TLabel', font=('Times',12,'bold'))
        
        controller_report_treeview.heading(0, text='رقم الطلب', anchor='c')
        controller_report_treeview.heading(1, text='رقم فاتورة الشحن', anchor='c')
        controller_report_treeview.heading(2, text='السعر', anchor='c')
        controller_report_treeview.heading(3, text='رقم جوال العميل', anchor='c')
        controller_report_treeview.heading(4, text='أسم العميل', anchor='c')
        controller_report_treeview.heading(5, text='أسم المندوب', anchor='c')
        controller_report_treeview.heading(6, text='تاريخ الإضافة', anchor='c')
        controller_report_treeview.heading(7, text='ملاحضة', anchor='c')
        controller_report_treeview.heading(8, text='#.م', anchor='c')
        
        for x in range(0,9):
            if x == 4:
                controller_report_treeview.column(x, width=220, anchor='ne')
                continue
            if x == 1:
                controller_report_treeview.column(x, width=60)
                continue
            controller_report_treeview.column(x, stretch=False, width=120)


        # for x in range(0,8):
        #     controller_report_treeview.column(x, anchor='center')
    treeview_setting()

    frame_viewers_totals = LabelFrame(master, text='مجاميع')
    frame_viewers_totals.pack(fill='both')

    total_entry = Entry(frame_viewers_totals,justify='right', font=entries_font)  # name customer
    total_entry.pack(side='left')


    total_label = Label(frame_viewers_totals, text='الإجمالي')
    total_label.pack(side='left', padx=6)
    
    total_orders_entry = Entry(frame_viewers_totals,justify='right', font=entries_font)  # name customer
    total_orders_entry.pack(side='left')


    total_orders_label = Label(frame_viewers_totals, text='عدد الشحنات')
    total_orders_label.pack(side='left', padx=6)
    
    total_orders_entry = Entry(frame_viewers_totals,justify='right', font=entries_font)  # name customer
    total_orders_entry.pack(side='left')


    login_orders_label = Label(frame_viewers_totals, text='عدد الشحنات')
    login_orders_label.pack(side='left', padx=6)

    
    login_username_label = Label(frame_viewers_totals, text='👤المستخدم')
    login_username_label.pack(side='right', padx=6)
    
    login_username_entry = Entry(frame_viewers_totals, justify='center')
    login_username_entry.pack(side='right', padx=6)
    # login_username_entry.insert(0, )
    login_username_entry.config(state='readonly')
    
    network_connection_check_l = Label(frame_viewers_totals, text=':حالة الإتصال')
    network_connection_check_l.pack(side='right', padx=6)
    
    network_connection_check_e = Entry(frame_viewers_totals, justify='center')
    network_connection_check_e.pack(side='right', padx=6)
    


    fetch_order_data(driver='الكل')