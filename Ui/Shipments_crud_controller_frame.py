from config.Libaries import *
# إستدعاء إعدادات النظام
from config.sys_classes import *

#Sqlite3 الأتصال بقاعدة البيانات
from Data.SQILite import SQL_DB

#Supabase الأتصال بقاعدة البيانات
from Data.Supa import Supa




def Controller_and_view_recorder_frame(master,home_img_logo):
    "(عرض بيانات,إدخال,تعديل,تسليم)فريم تحكم بالشحنات"
    
    frame_controller_app = LabelFrame(master, text='فريم التحكم')
    frame_controller_app.pack(side='left', fill='both')
    
    # فريم عرض التحكم بالتقرير
    frame_viewers_tools = LabelFrame(master, text='فريم عرض التحكم بالتقرير')
    frame_viewers_tools.pack(fill='both')


    frame_viewers_tools_1 = LabelFrame(frame_viewers_tools, text='الفريم الاول')
    frame_viewers_tools_1.pack(fill='both')


    global frame,img_lable
    'فريم إدخال البيانات'
    # frame = Frame(master, width=130)
    # frame.pack(fill='both')
    

    # # فريم الساعه والاعدادات
    frame_info = Frame(frame_controller_app)
    frame_info.pack(fill='both')

    frame_info_1 = Frame(frame_info)
    frame_info_1.pack(fill='both', side='left',)
    
    frame_info_2 = Frame(frame_info)
    frame_info_2.pack(fill='both', side='right', expand=True)

    # فريم إدخال البيانات
    frame_data_entry = LabelFrame(frame_controller_app, text='فريم إدخال البيانات')
    frame_data_entry.pack(fill='both', expand=True)

    # frame_info.config(frame)

    # تغيير ألوان الظام
    def change_theme():
        t = Toplevel()
        t.iconbitmap(sys_icon)
        t.title('تغيير الثيم')
        t.geometry('650x150')
        t.wm_attributes('-topmost', True)
        sys_class.centering_window(window=t)
        var = StringVar()
        def trace_themem_choosing(*args):
            SQL_DB.switch_theme_color(theme_name=choose_theme.get(),old_theme_name=SQL_DB.get_theme())
            # page.style.theme_use(choose_theme.get())

        
        choose_theme = ttk.Combobox(t, values=SQL_DB.get_list_theme(),
            font=('Times', 12, 'bold'), textvariable=var, cursor='hand2', justify='center', width=13)
        choose_theme.set(value=SQL_DB.get_theme())
        choose_theme.pack(fill='both')
        var.trace_add('write', callback=trace_themem_choosing)
        t.mainloop()

    def drivers_manager():
        global drivers_list
        drivers_list = SQL_DB.fetch_list_drivers_name()
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
            SQL_DB.add_new_driver(id=e2.get(),name=e0.get(),phone=e1.get())
            messagebox.showinfo('ملاحضة', 'تم إضافة مندوب جديد', parent=t)
            t.focus_set()
            # choose_driver_name.set(value=[])
            choose_driver_name.configure(value=SQL_DB.fetch_list_drivers_name())
            choose_driver_name.update()
            choose_driver_name_search.configure(value=SQL_DB.fetch_list_drivers_name())
        
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
            for y in SQL_DB.fetch_drivers_data():
                c+=1
                view_drivers.insert('', 'end', values=(y[0],y[1],y[2],c))
        fetch_drivers_data()
        
        t.mainloop()
    


    def date_time_update():
        try:
            times = strftime('%H:%M:%S')
            dates = strftime('%Y-%m-%d')
            balance_of_user_entry.delete(0, END)
            balance_of_user_entry.insert(0, SQL_DB.get_balance_total_report())
            
            date_time_label.config(text=f'{dates} {times}')
            date_time_label.after(1000, date_time_update)
            
        except:
            pass

    date_time_label = Label(frame_info_1, font=('times',11,'bold'))
    date_time_label.pack(pady=3, padx=3)



    



    my_menu_bar = Menubutton(frame_info_1, text='⚙️ إعدادات', cursor='hand2',
                                bootstyle='info-outline')
    my_menu_bar.pack(fill='both', pady=5)

    file_menu = Menu(my_menu_bar, cursor='hand2')
    file_menu.add_radiobutton(label='👥 المناديب', command=drivers_manager)
    file_menu.add_separator()
    file_menu.add_radiobutton(label='🔄تغير الثيم', command=change_theme)
    # file_menu.add_separator()
    # file_menu.add_radiobutton(label='🚪إغلاق النظام', command=lambda:page.destroy())
    my_menu_bar['menu'] = file_menu



    f1 = Frame(frame_info_2)
    f1.pack(side='right')

    f2 = Frame(frame_info_2)
    f2.pack(side='left', fill='both', expand=True)

    last_inoice_lable = Label(f1,text='مسلسل', font=('times',12,'bold'))
    last_inoice_lable.pack(pady=3)
    
    last_inoice_entry = Entry(f2, width=5)
    last_inoice_entry.pack(fill='both', padx=3)
    last_inoice_entry.insert(0, f'#{int(SQL_DB.generate_order_serial())-1}')
    

    balance_of_user_lable = Label(f1, text='رصيد الخزنة', font=('times',12,'bold'))
    balance_of_user_lable.pack(pady=3)
    
    balance_of_user_entry = Entry(f2, width=5)
    balance_of_user_entry.pack(fill='both',pady=3)
    try:
        balance_of_user_entry.insert(0, SQL_DB.get_balance_total_report())
    except:
        balance_of_user_entry.insert(0, '0.00')


    def enable_copy_paste(widget):
        print('Vaild')
        'بسمح لخاصة النسخ واللصق في حالة ان اللغة غير إنجليزي'
        # اختصارات النسخ
        widget.bind("<Control-c>", lambda e: widget.event_generate("<<Copy>>"))
        widget.bind("<Control-C>", lambda e: widget.event_generate("<<Copy>>"))
        
        # اختصارات القص
        widget.bind("<Control-x>", lambda e: widget.event_generate("<<Cut>>"))
        widget.bind("<Control-X>", lambda e: widget.event_generate("<<Cut>>"))
        
        # اختصارات اللصق
        widget.bind("<Control-v>", lambda e: widget.event_generate("<<Paste>>"))
        widget.bind("<Control-V>", lambda e: widget.event_generate("<<Paste>>"))



    # customer_label_id = Label(frame_data_entry, text='رقم العضوية')
    # customer_label_id.pack()
    
    # customer_id_entry = Entry(frame_data_entry,justify='right')  # name customer
    # # customer_id_entry.pack(fill='both')
    
    customer_label_name = Label(frame_data_entry, text='أسم العميل')
    customer_label_name.pack()

    customer_name = Entry(frame_data_entry, justify='right')  # name customer
    customer_name.pack(fill='both', padx=7)
    
    customer_label_phone = Label(frame_data_entry, text='رقم العميل')
    customer_label_phone.pack()
    enable_copy_paste(customer_label_phone)
    # sys_class.enable_copy_paste(customer_label_phone)

    customer_entry_phone = Entry(frame_data_entry, justify='right')  # name customer
    customer_entry_phone.pack(fill='both', padx=7)

    frame_invoice_linked = LabelFrame(frame_data_entry, text='بيانات الفاتورة المرتطبة', border=14)
    frame_invoice_linked.pack(fill='both', expand=True)

    order_id_in_store_lable = Label(frame_invoice_linked, text='رقم فاتورة المتجر/الشحن ')
    order_id_in_store_lable.pack()
    
    order_id_in_store_entry = Entry(frame_invoice_linked, width=12,justify='right')  # name customer
    order_id_in_store_entry.pack(fill='both', padx=3)
    
    price_of_customer_order_label = Label(frame_invoice_linked, text='سعر الفاتورة ')
    price_of_customer_order_label.pack()

    price_of_customer_order_entry = Entry(frame_invoice_linked, justify='right')  # name customer
    price_of_customer_order_entry.pack(fill='both', padx=3)
    
    choose_driver_name_label = Label(frame_data_entry, text='أسم المندوب')
    choose_driver_name_label.pack()

    # global choose_driver_name
    choose_driver_name = ttk.Combobox(frame_data_entry, values=list(SQL_DB.fetch_list_drivers_name()),
        font=('Times', 12, 'bold'),  cursor='hand2', justify='center',)
    choose_driver_name.set(value='غير معرف')
    choose_driver_name.pack(fill='both', padx=7)
    
    customer_location_label = Label(frame_data_entry, text='موقع العميل/رابط')
    customer_location_label.pack()
    
    def update_street_name(*args):
        location = trace_location_name.get()
        street = sys_class.extract_street_or_pluscode(location)
        customer_street_entry.delete(0, END)
        customer_street_entry.insert(0, street)
        
    
    trace_location_name = StringVar()
    
    customer_location_entry = Entry(frame_data_entry, justify='right', textvariable=trace_location_name)
    customer_location_entry.pack(fill='both', padx=7)
    trace_location_name.trace_add('write', callback=update_street_name)

    customer_street_label = Label(frame_data_entry, text='أسم الحي')
    customer_street_label.pack()
    
    customer_street_entry = Entry(frame_data_entry, justify='right')
    customer_street_entry.pack(fill='both', padx=7)


    nots_lable = Label(frame_data_entry, text='ملاحضة')
    nots_lable.pack()
    
    nots_entry = Entry(frame_data_entry,)  # name customer
    nots_entry.pack(fill='both', padx=7)

    
    def add_data():
        # To Sqlite3 | Supa
        price = price_of_customer_order_entry.get()
        try:
            # Try convert entry to int.
            int(price)
        except ValueError:
            pass
            # messagebox.showwarning('ملاحضة', 'يجب إدخال قيمة رقمية')
            # print('You cannot convert to int.')
        try:
            # Try convert entry to float.
            float(price)
        except ValueError:
            pass
            # print('You cannot convert to float.')
            

            # messagebox.showwarning('ملاحضة', 'يجب إدخال قيمة رقمية')
            # return

        if price_of_customer_order_entry.get() =='':
            messagebox.showwarning('ملاحضة', 'يجب إدخال سعر', parent=master)
            return 
        if price_of_customer_order_entry.get() == 0:
            messagebox.showwarning('ملاحضة', 'يجب إدخال سعر', parent=master)
            return
        
        # SQL_DB.add_new_order(
        #     price=price_of_customer_order_entry.get(),
        #     customer_name=customer_name.get(),
        #     customer_phone=customer_entry_phone.get(),
        #     driver=choose_driver_name.get(),
        #     payment_status='غير مدفوعة',
        #     payment_type=choose_payment_type.get(),
        #     order_id_shipment=order_id_in_store_entry.get(),
        #     order_status='جاري التوصيل',
        #     notes=nots_entry.get()
        #     )
        try:
            Supa.add_new_order(
                price=price_of_customer_order_entry.get(),
                customer_name=customer_name.get(),
                customer_phone=customer_entry_phone.get(),
                driver=choose_driver_name.get(),
                payment_status='غير مدفوعة',
                customer_location=customer_location_entry.get(),
                order_id_shipment=order_id_in_store_entry.get(),
                order_status='جاري التوصيل',
                notes=nots_entry.get()
            )
        except ConnectionError as e:
            messagebox.showerror('ملاحضة', f'تأكد من إتصالك باالإنترنت ثم عاود المحاولة :{e}', parent=master)
            return
        
        except Exception as e:
            messagebox.showerror('ملاحضة', f'تأكد من إتصالك باالإنترنت ثم عاود المحاولة :{e}', parent=master)
            return
        
        update_controller_view_items()
        balance_of_user_entry.delete(0, END)
        balance_of_user_entry.insert(0, SQL_DB.get_balance_total_report())
        
        
        
        last_inoice_entry.delete(0, END)
        last_inoice_entry.insert(0, f'#{int(SQL_DB.generate_order_serial())-1}')
    
        # messagebox.showinfo('ملاحضة', f'تم تسجيل فاتورة جديدة {int(SQL_DB.generate_order_serial())-1}')

        messagebox.showinfo('ملاحضة', f'تم تسجيل فاتورة جديدة {int(Supa.generate_order_serial())-1}', parent=master)
        fetch_order_data('driver')
        # Supa.fetch_collection_money_report()
        entries_clearing()

    def entries_clearing():
        price_of_customer_order_entry.delete(0, END)
        customer_name.delete(0, END)
        customer_entry_phone.delete(0, END)
        customer_entry_phone.delete(0, END)
        choose_driver_name.set('غير معرف')
        customer_location_entry.delete(0, END)
        order_id_in_store_entry.delete(0, END)
        nots_entry.delete(0, END)
    

    frame_data_entry_button = LabelFrame(frame_data_entry)
    frame_data_entry_button.pack(fill='both')

    button_add = Button(frame_data_entry_button, text='➕إضافة طلب', cursor='hand2', bootstyle='info',
                            command=lambda:threading.Thread(target=add_data()).start())
    button_add.pack(fill='both', pady=4, padx=4)







    
    def delete_recorder():
        # id_serial العصر المراد حذف عن طريق 
        item_selection = controller_report_treeview.item(controller_report_treeview.selection(),'values')[0]
        
        # تأكيد حذف السجل
        ask_delete = messagebox.askyesno('ملاحضة' ,'هل تريد مسحل السجل', icon='info', parent=master)
        if ask_delete == FALSE:
            return
        # supabase العصر المراد حذف من  
        Supa.delete_recorder(serial=item_selection)
        

        # SQL_DB.delete_recorder(id_serial=item_selection)
        d = messagebox.showinfo('ملاحضة', f'تم حذف السجل {item_selection}', parent=master)
        
        update_controller_view_items()
        balance_of_user_entry.delete(0, END)
        balance_of_user_entry.insert(0, SQL_DB.get_balance_total_report())
        
    button_delete_recorder = Button(frame_data_entry_button, text='🗑حذف السجل', cursor='hand2', bootstyle='info', command=delete_recorder)
    button_delete_recorder.pack(fill='both', pady=4, padx=4,)
    

    
    def edit_recorder():
        item_selection = controller_report_treeview.item(controller_report_treeview.selection(),'values')
        # show_recorder_detials(id=item_selection, option='EDIT')
    
    button_edit_recorder = Button(frame_data_entry_button, text='🖊️تعديل السجل', cursor='hand2', bootstyle='info', command=edit_recorder)
    button_edit_recorder.pack(fill='both', pady=4, padx=4,)

    # img = Image.open('Shopping_Cart_Icon.png').resize((400,400))
    # img_logo = ImageTk.PhotoImage(img)
    

    
    img_lable = tk.Label(frame_data_entry,
                    compound='center',image=home_img_logo)
    img_lable.pack(fill='both', expand=True, padx=2, pady=5)
    
    # threading.Thread(target=date_time_update()).start()
    date_time_update()












    ###################################'التحكم بالسجلات'################################################
    global controller_report_treeview,driver_var_controller
    # d = note_book.index(note_book.select())

    'عرض وتحكم بالسجلات'    
    global update_controller_view_items



    customer_label_id_search = Label(frame_viewers_tools_1, text='رقم العضوية')
    # customer_label_id_search.pack(side='right',padx=14)

    customer_id_entry_search = Entry(frame_viewers_tools_1, justify='right', font=entries_font)  # name customer
    # customer_id_entry_search.pack(side='right')
    
    customer_label_name_search = Label(frame_viewers_tools_1, text='أسم العميل')
    customer_label_name_search.pack(side='right', padx=10)

    customer_name_search = Entry(frame_viewers_tools_1, justify='right', font=entries_font)  # name customer
    customer_name_search.pack(side='right', padx=6)
    
    customer_label_phone_search = Label(frame_viewers_tools_1, text='رقم العميل')
    customer_label_phone_search.pack(side='right')

    customer_entry_phone_search = Entry(frame_viewers_tools_1,justify='right', font=entries_font)  # name customer
    customer_entry_phone_search.pack(side='right')
    
    price_of_customer_order_label_search = Label(frame_viewers_tools_1, text='سعر الفاتورة ')
    # price_of_customer_order_label_search.pack(side='right', padx=10)

    price_of_customer_order_entry_search = Entry(frame_viewers_tools_1, justify='right', font=entries_font)  # name customer
    # price_of_customer_order_entry_search.pack(side='right')


    frame_viewers_tools_2 = LabelFrame(frame_viewers_tools, text='الفريم الثاني')
    frame_viewers_tools_2.pack(fill='both')

    button_print_reprot = Button(frame_viewers_tools_1, text='🖨️طباعة',
                            cursor='hand2', bootstyle='info', command=NONE)
    button_print_reprot.pack(fill='both', pady=4, padx=4, side='left', expand=True)
    

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
    
    button_search = Button(frame_viewers_tools_2, text='🔍بحث',
                            cursor='hand2', bootstyle='info', command=fetch_order_data)
    button_search.pack(fill='both', pady=4, padx=4, side='right', expand=True)
    
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
        fetch_order_data(driver=driver_var_controller.get())
        messagebox.showinfo('ملاحضة', f'تم تسليم السجل {item[0]}', parent=master)
        
        

    button_recevie_recorders = Button(frame_viewers_tools_2, text='💵تسليم',
                            cursor='hand2', bootstyle='info', command=receive_order)
    button_recevie_recorders.pack(fill='both', pady=4, padx=4, side='left', expand=True)
    
    button_get_all_recorder_info = Button(frame_viewers_tools_2, text='ℹ️معلومات',
                            cursor='hand2', bootstyle='info', command=fetch_recorder_info)
    button_get_all_recorder_info.pack(fill='both', pady=4, padx=4, side='left', expand=True)







    order_id_in_store_lable_search = Label(frame_viewers_tools_1, text='رقم فاتورة المتجر ')
    order_id_in_store_lable_search.pack(side='right')
    
    order_id_in_store_entry_search = Entry(frame_viewers_tools_1,justify='right', font=entries_font)  # name customer
    order_id_in_store_entry_search.pack(side='right')
    
    choose_driver_name_label_search = Label(frame_viewers_tools_1, text='أسم المندوب')
    choose_driver_name_label_search.pack(side='right', padx=10)
    
    def trace_drivers_name(*args):
        driver = driver_var_controller.get()
        fetch_order_data(driver=driver)

    driver_var_controller = StringVar()

    global choose_driver_name_search
    choose_driver_name_search = ttk.Combobox(frame_viewers_tools_1, values=SQL_DB.fetch_list_drivers_name(),
        font=('Times', 12, 'bold'),  cursor='hand2', justify='center', width=13, textvariable=driver_var_controller)
    choose_driver_name_search.set(value='الكل')
    choose_driver_name_search.pack(side='right')
    driver_var_controller.trace_add('write', callback=trace_drivers_name)
    
    choose_payment_label_search = Label(frame_viewers_tools_1, text='نوع الدفع')
    # choose_payment_label_search.pack(side='right', padx=10)

    choose_payment_type_search = ttk.Combobox(frame_viewers_tools_1, values=['كاش','أجل','فيزا'],
        font=('Times', 12, 'bold'),  cursor='hand2', justify='center', width=7)
    choose_payment_type_search.set(value='كاش')
    # choose_payment_type_search.pack(fill='both',side='right')

    
    from_date_label_search = Label(frame_viewers_tools_1, text='من تاريخ')
    # from_date_label_search.pack(side='right', padx=6)
    
    from_date_choose_date_search = DateEntry(frame_viewers_tools_1, dateformat='%Y-%m-%d', width=10 )
    # from_date_choose_date_search.pack(fill='both', side='right', expand=True)
    
    to_date_label_search = Label(frame_viewers_tools_1, text='إلى تاريخ')
    # to_date_label_search.pack(side='right', padx=6)

    to_date_choose_date_search = DateEntry(frame_viewers_tools_1, dateformat='%Y-%m-%d', width=10)
    # to_date_choose_date_search.pack(fill='both', side='right', expand=True)





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
            controller_report_treeview.column(x, width=220)
            continue
        controller_report_treeview.column(x, stretch=False, width=120)

    fetch_order_data('driver')
    for x in range(0,8):
        controller_report_treeview.column(x, anchor='center')

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
    
    network_connection_check_e.config(state='readonly')
    
    def nentwork_checker():
        # فحص الإتصال بالإنترنت مع مع كل ثانية
        try:
            response = requests.get(url='https://www.google.com/', timeout=1)
            # print(response.status_code)
            
            if response.status_code == 200:
                print('Get:200')
                network_connection_check_e.config(state='normal')
                network_connection_check_e.delete(0, END)
                network_connection_check_e.insert(0, "متصل")
                network_connection_check_e.config(state='desable', bootstyle='SUCCESS')
            if response.status_code != 200:
                
                network_connection_check_e.config(state='normal')
                network_connection_check_e.delete(0, END)
                network_connection_check_e.insert(0, "غير متصل")
                network_connection_check_e.config(state='desable', bootstyle='DANGER')
            
            login_username_label.after(3000, nentwork_checker)
            return True if response.status_code != 200 else False
        except requests.ConnectionError as e:
            login_username_label.after(3000, nentwork_checker)
            return False
            
    # print(nentwork_checker())  
    
    # page.after(3000, nentwork_checker)
            # network_connection_check_l.after(3000, nentwork_checker)
            # print(e)

    # if nentwork_checker() == True:
    #     network_connection_check_e.config(state='normal')
    #     network_connection_check_e.delete(0, END)
    #     network_connection_check_e.insert(0, "متصل")
    #     network_connection_check_e.config(state='desable', bootstyle='SUCCESS')
    # if nentwork_checker() == False:
    #     network_connection_check_e.config(state='normal')
    #     network_connection_check_e.delete(0, END)
    #     network_connection_check_e.insert(0, "غير متصل")
    #     network_connection_check_e.config(state='desable', bootstyle='DANGER')
    
    # nentwork_checker()
    
    def update_controller_view_items():
        'تحديث السجلات'
        fetch_order_data(driver=choose_driver_name_search.get())

    # fetch_order_data(driver='الكل')
