from config.Libaries import *
# إستدعاء إعدادات النظام
from config.sys_classes import *

#Sqlite3 الأتصال بقاعدة البيانات
# from Data.SQILite import SQL_DB

#Supabase الأتصال بقاعدة البيانات
from Data.Supa import Supa



def Shipment_viewer_report_frame(master):
    'فريم عرض تقرير شامل'
    global report_treeview

    # فريم عرض التحكم بالتقرير
    frame_viewers_tools = LabelFrame(master, text='فريم عرض التحكم بالتقرير')
    frame_viewers_tools.pack(fill='both')


    frame_viewers_tools_1 = LabelFrame(frame_viewers_tools, text='الفريم الاول')
    frame_viewers_tools_1.pack(fill='both')




    customer_label_id_search = Label(frame_viewers_tools_1, text='رقم العضوية')
    customer_label_id_search.pack(side='right',padx=14)

    customer_id_entry_search = Entry(frame_viewers_tools_1, justify='right')  # name customer
    customer_id_entry_search.pack(side='right')
    
    customer_label_name_search = Label(frame_viewers_tools_1, text='أسم العميل')
    customer_label_name_search.pack(side='right', padx=10)

    customer_name_search = Entry(frame_viewers_tools_1, justify='right')  # name customer
    customer_name_search.pack(side='right', padx=6)
    
    customer_label_phone_search = Label(frame_viewers_tools_1, text='رقم العميل')
    customer_label_phone_search.pack(side='right')

    customer_entry_phone_search = Entry(frame_viewers_tools_1,justify='right')  # name customer
    customer_entry_phone_search.pack(side='right')
    
    price_of_customer_order_label_search = Label(frame_viewers_tools_1, text='سعر الفاتورة ')
    price_of_customer_order_label_search.pack(side='right', padx=10)

    price_of_customer_order_entry_search = Entry(frame_viewers_tools_1, justify='right')  # name 
    price_of_customer_order_entry_search.pack(side='right')


    def fetch_order_data_reports(driver):
        "جلب تقرير شامل لكل الحالات"
        report_treeview.delete(*report_treeview.get_children())
        data = Supa.fetch_collection_money_reports()
        for x in data:
            report_treeview.insert('','end', values=(x))
            # report_treeview.insert('','end', values=(x['id_serial'],x['order_id_shipment'],f"{x["price"]:,.2f}",x["order_status"],x['customer_phone'],x['customer_name'],x['driver'],(x['date_creation'],x['time_creation']),x['notes'],countLine))
            # report_treeview.insert('','end', values=(x['id_serial'],x['order_id_shipment'],f"{float(x["price"]):,.2f}",x["order_status"],x['customer_phone'],x['customer_name'],x['driver'],))
            
        # try:
            # report_treeview.delete(*report_treeview.get_children())
            # datalist = Data.fetch_order_data_reports(driver,order_status=choose_order_status.get(),
            #                                          to_date=to_date_choose_date_search.entry.get(),from_date=from_date_choose_date_search.entry.get())
            # countLine = 0
            # if datalist == []:
            #     return
            # for x in datalist[0]:
            #     countLine +=1
            #     report_treeview.insert('','end', values=(x[0],x[3],f"{x[7]:,.2f}",x[2],x[6],x[5],x[8],(x[10],x[11]),x[9],countLine))
            # report_treeview.yview_moveto(1)
            # total_entry.delete(0, END)
            # total_entry.insert(0, datalist[1])
            # total_orders_entry.delete(0, END)
            # total_orders_entry.insert(0, datalist[2])
        # except :
        #     pass




    # button_search = Button(frame_viewers_tools_1, text='بحث',
    #                         cursor='hand2', bootstyle='info')
    # button_search.pack(fill='both', pady=4, padx=4, side='right')
    
    def fetch_recorder_info():
        item = report_treeview.item(report_treeview.selection(),'values'[0])
        # show_recorder_detials(id=item, option='SHOW')

    button_get_all_recorder_info = Button(frame_viewers_tools_1, text='ℹ️معلومات',
                            cursor='hand2', bootstyle='info', command=fetch_recorder_info)
    button_get_all_recorder_info.pack(fill='both', pady=4, padx=4, side='left')
    
    def get_invoice_as_pdf():
        item = report_treeview.item(report_treeview.selection(),'values'[0])[0]
        sys_class.generator_invoice_as_pdf_size_width_57mm(id=item,option='EXPORT')
    
    button_get_all_recorder_info_as_pdf = Button(frame_viewers_tools_1, text='🧾PDF فاتورة',
                            cursor='hand2', bootstyle='info', command=get_invoice_as_pdf)
    button_get_all_recorder_info_as_pdf.pack(fill='both', pady=4, padx=4, side='left')





    frame_viewers_tools_2 = LabelFrame(frame_viewers_tools, text='الفريم الثاني')
    frame_viewers_tools_2.pack(fill='both')



    order_id_in_store_lable_search = Label(frame_viewers_tools_2, text='رقم فاتورة المتجر ')
    order_id_in_store_lable_search.pack(side='right')
    
    order_id_in_store_entry_search = Entry(frame_viewers_tools_2,justify='right')  # name customer
    order_id_in_store_entry_search.pack(side='right', fill='both', expand=True)
    
    choose_driver_name_label_search = Label(frame_viewers_tools_2, text='أسم المندوب')
    choose_driver_name_label_search.pack(side='right', padx=10)
    
    def trace_drivers_name_reports(*args):
        order_status = order_status_var_controller_report.get()
        driver = driver_var_controller_report.get()
        fetch_order_data_reports(driver=driver)

    driver_var_controller_report = StringVar()
    order_status_var_controller_report = StringVar()

    
    choose_driver_name_search_report = ttk.Combobox(frame_viewers_tools_2, values=SQL_DB.fetch_list_drivers_name(),
        font=('Times', 12, 'bold'),  cursor='hand2', justify='center', width=13, textvariable=driver_var_controller_report)
    choose_driver_name_search_report.set(value='الكل')
    choose_driver_name_search_report.pack(side='right')
    driver_var_controller_report.trace_add('write', callback=trace_drivers_name_reports)
    
    choose_order_status_lable = Label(frame_viewers_tools_2, text='حالة الفاتورة')
    choose_order_status_lable.pack(side='right', padx=10)

    choose_order_status = ttk.Combobox(frame_viewers_tools_2, values=['جاري التوصيل','ملغية','تم التسليم','الكل'],
        font=('Times', 12, 'bold'),  cursor='hand2', justify='center', width=12, textvariable=order_status_var_controller_report)
    choose_order_status.set(value='الكل')
    choose_order_status.pack(fill='both',side='right')
    order_status_var_controller_report.trace_add('write', callback=trace_drivers_name_reports)
    
    # choose_payment_label_search = Label(frame_viewers_tools_2, text='نوع الدفع')
    # choose_payment_label_search.pack(side='right', padx=10)

    # choose_payment_type_search = ttk.Combobox(frame_viewers_tools_2, values=['كاش','أجل','فيزا'],
    #     font=('Times', 12, 'bold'),  cursor='hand2', justify='center', width=7)
    # choose_payment_type_search.set(value='كاش')
    # choose_payment_type_search.pack(fill='both',side='right')

    
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
    report_treeview = Treeview(frame_viewers_rpeort, cursor='hand2',
                            columns=(0,1,2,3,4,5,6,7,8,9), show='headings', bootstyle='info', yscrollcommand=report_scroller.set)
    report_treeview.pack(fill='both', side='left', expand=True)
    report_scroller.config(command=report_treeview.yview)
    
    style.configure('Treeview.Heading', font=('Times',13,'bold'))
    style.configure('Treeview', font=('Times',12,'bold'))
    # style.configure('Treeview', rowheight=130)
    style.configure('TButton', font=('Times',13,'bold'))
    style.configure('TLabel', font=('Times',12,'bold'))

    
    report_treeview.heading(0, text='رقم الطلب')
    report_treeview.heading(1, text='رقم فاتورة الشحن')
    report_treeview.heading(2, text='السعر')
    report_treeview.heading(3, text='حالة السجل')
    report_treeview.heading(4, text='رقم جوال العميل')
    report_treeview.heading(5, text='أسم العميل')
    report_treeview.heading(6, text='أسم المندوب')
    report_treeview.heading(7, text='تاريخ التسجيل')
    report_treeview.heading(8, text='ملاحضة')
    report_treeview.heading(9, text='#.م')

    for x in range(0,10):
        report_treeview.column(x, anchor='center')
        if x == 9:
            report_treeview.column(9, anchor='c', width=102)
        if x == 7:
            report_treeview.column(7, width=300)




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

    # fetch_order_data_reports(driver='الكل')