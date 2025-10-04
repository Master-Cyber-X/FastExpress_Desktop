from config.Libaries import *
# إستدعاء إعدادات النظام
from config.sys_classes import *

#Sqlite3 الأتصال بقاعدة البيانات
# from Data.SQILite import SQL_DB

#Supabase الأتصال بقاعدة البيانات
from Data.Supa import Supa


   
    
def Track_drivers_frame(master):
    'فريم عرض التحصيلات اليومية للمناديب '

    # فريم عرض التحكم بالتقرير
    frame_viewers_tools = LabelFrame(master, text='فريم عرض التحكم بالتقرير')
    frame_viewers_tools.pack(fill='both')


    # frame_viewers_tools_1 = LabelFrame(frame_viewers_tools, text='الفريم الاول')
    # frame_viewers_tools_1.pack(fill='both')




    # customer_label_id_search = Label(frame_viewers_tools_1, text='رقم العضوية')
    # customer_label_id_search.pack(side='right',padx=14)

    # customer_id_entry_search = Entry(frame_viewers_tools_1, justify='right')  # name customer
    # customer_id_entry_search.pack(side='right')
    
    # customer_label_name_search = Label(frame_viewers_tools_1, text='أسم العميل')
    # customer_label_name_search.pack(side='right', padx=10)

    # customer_name_search = Entry(frame_viewers_tools_1, justify='right')  # name customer
    # customer_name_search.pack(side='right', padx=6)
    
    # customer_label_phone_search = Label(frame_viewers_tools_1, text='رقم العميل')
    # customer_label_phone_search.pack(side='right')

    # customer_entry_phone_search = Entry(frame_viewers_tools_1,justify='right')  # name customer
    # customer_entry_phone_search.pack(side='right')
    
    # price_of_customer_order_label_search = Label(frame_viewers_tools_1, text='سعر الفاتورة ')
    # price_of_customer_order_label_search.pack(side='right', padx=10)

    # price_of_customer_order_entry_search = Entry(frame_viewers_tools_1, justify='right')  # name customer
    # price_of_customer_order_entry_search.pack(side='right')


    def fetch_order_data_reports(driver):
        try:
            "Fetch data for items"
            report_collection_treeview.delete(*report_collection_treeview.get_children())
            from_date = from_date_choose_date_search.entry.get()
            to_date = to_date_choose_date_search.entry.get()
            datalist = SQL_DB.fetch_collection_money_report_summary(driver,
                from_date=from_date,
                to_date=to_date
                )
            
            countLine = 0
            report_collection_treeview.yview_moveto(1)
            total_orders_entry.delete(0, END)
            total_orders_entry.insert(0, datalist[2])
            total_entry.delete(0, END)
            total_entry.insert(0, datalist[1])
            if datalist == []:
                return
            for x in datalist[0]:
                countLine +=1
                report_collection_treeview.insert('','end', values=(x[1],x[2],x[0], to_date,from_date ,x[3]))
            
        except Exception as e:
            messagebox.showerror('ملاحضة', f'Error : {e}', parent=master)




    # button_search = Button(frame_viewers_tools_1, text='🔎بحث',
    #                         cursor='hand2', bootstyle='info')
    # button_search.pack(fill='both', pady=4, padx=4, side='right')
    
    def fetch_recorder_info():
        item = report_collection_treeview.item(report_collection_treeview.selection(),'values'[2])
        # show_recorder_detials(id=item, option='SHOW')




    frame_viewers_tools_2 = LabelFrame(frame_viewers_tools, text='الفريم الثاني')
    frame_viewers_tools_2.pack(fill='both')


    button_get_all_recorder_detials = Button(frame_viewers_tools_2, text='ℹ️معلومات',
                            cursor='hand2', bootstyle='info', command=fetch_recorder_info)
    button_get_all_recorder_detials.pack(fill='both', pady=4, padx=4, side='left')




    order_id_in_delivery_system_labal= Label(frame_viewers_tools_2, text='رقم فاتورة التوصيل ')
    order_id_in_delivery_system_labal.pack(side='right')
    
    # رقم الطلب على نظام التوصيل
    order_id_in_delivery_system_entry = Entry(frame_viewers_tools_2,justify='right')  # name customer
    order_id_in_delivery_system_entry.pack(side='right',fill='x', expand=True)

    order_id_from_system_lable = Label(frame_viewers_tools_2, text='رقم فاتورة المتجر ')
    order_id_from_system_lable.pack(side='right')
    
    # رقم فاتورة الشحن أو فاتورة المتجر
    order_id_from_system_entry = Entry(frame_viewers_tools_2,justify='right')  # name customer
    order_id_from_system_entry.pack(side='right',fill='x', expand=True)


    
    choose_driver_name_label_search = Label(frame_viewers_tools_2, text='أسم المندوب')
    choose_driver_name_label_search.pack(side='right', padx=10)
    
    def trace_drivers_name_reports(*args):
        driver = driver_var_controller_report.get()
        fetch_order_data_reports(driver=driver)

    driver_var_controller_report = StringVar()

    
    choose_driver_name_search_report = ttk.Combobox(frame_viewers_tools_2, values=SQL_DB.fetch_list_drivers_name(),
        font=('Times', 12, 'bold'),  cursor='hand2', justify='center', width=13, textvariable=driver_var_controller_report)
    choose_driver_name_search_report.set(value='الكل')
    choose_driver_name_search_report.pack(side='right')
    driver_var_controller_report.trace_add('write', callback=trace_drivers_name_reports)
    
    choose_order_statu_label_search = Label(frame_viewers_tools_2, text='نوع الدفع')
    choose_order_statu_label_search.pack(side='right', padx=10)

    choose_order_statu_search = ttk.Combobox(frame_viewers_tools_2, values=['كاش','أجل','فيزا'],
        font=('Times', 12, 'bold'),  cursor='hand2', justify='center', width=7)
    choose_order_statu_search.set(value='كاش')
    choose_order_statu_search.pack(fill='both',side='right')

    
    from_date_label_search = Label(frame_viewers_tools_2, text='من تاريخ')
    from_date_label_search.pack(side='right', padx=6)
    
    from_date_choose_date_search = DateEntry(frame_viewers_tools_2, dateformat='%Y-%m-%d', width=10 )
    from_date_choose_date_search.pack(fill='both', side='right')
    
    to_date_label_search = Label(frame_viewers_tools_2, text='إلى تاريخ')
    to_date_label_search.pack(side='right', padx=6)

    to_date_choose_date_search = DateEntry(frame_viewers_tools_2, dateformat='%Y-%m-%d', width=10)
    to_date_choose_date_search.pack(fill='both', side='right')




    # فريم عرض بيانات التقرير
    frame_viewers_rpeort = LabelFrame(master, text='فريم عرض التحكم بالتقرير')
    frame_viewers_rpeort.pack(fill='both', expand=True)
    
    report_scroller = Scrollbar(frame_viewers_rpeort, orient='vertical', cursor='hand2')
    report_scroller.pack(fill='both', side='right')


    style = Style()
    # شجرة عرض البيانات
    report_collection_treeview = Treeview(frame_viewers_rpeort, cursor='hand2',
                            columns=(0,1,2,3,4,5,6,7), show='headings', bootstyle='info', yscrollcommand=report_scroller.set)
    report_collection_treeview.pack(fill='both', side='left', expand=True)
    report_scroller.config(command=report_collection_treeview.yview)
    
    style.configure('Treeview.Heading', font=('Times',13,'bold'))
    style.configure('Treeview', font=('Times',12,'bold'))
    style.configure('Treeview', rowheight=130)
    style.configure('TButton', font=('Times',13,'bold'))
    style.configure('TLabel', font=('Times',12,'bold'))

    report_collection_treeview.heading(0, text='الإجمالي', anchor='center')
    report_collection_treeview.heading(1, text='عدد الشحنات الموصلة', anchor='center')
    report_collection_treeview.heading(2, text='عدد الشحنات المعلقة', anchor='center')
    report_collection_treeview.heading(3, text='عدد الشحنات المرتجعة', anchor='center')
    report_collection_treeview.heading(4, text='أسم المندوب', anchor='center')
    report_collection_treeview.heading(5, text='إلى تاريخ', anchor='center')
    report_collection_treeview.heading(6, text='من تاريخ', anchor='center')
    report_collection_treeview.heading(7, text='#.م', anchor='center')



    frame_viewers_totals = LabelFrame(master, text='مجاميع')
    frame_viewers_totals.pack(fill='both')

    total_entry = Entry(frame_viewers_totals,justify='right', font=entries_font)  # name customer
    total_entry.pack(side='left')


    total_label = Label(frame_viewers_totals, text='الإجمالي')
    total_label.pack(side='left', padx=6)
    
    total_orders_entry = Entry(frame_viewers_totals,justify='right', font=entries_font)  # name customer
    total_orders_entry.pack(side='left')


    total_orders_label = Label(frame_viewers_totals, text='عدد العملاء')
    total_orders_label.pack(side='left', padx=6)

    # fetch_order_data_reports(driver='الكل')






