from config.Libaries import *
# إستدعاء إعدادات النظام
from config.sys_classes import *

#Sqlite3 الأتصال بقاعدة البيانات
# from Data.SQILite import SQL_DB

#Supabase الأتصال بقاعدة البيانات
from Data.Supa import Supa


def analyzer_data_frame(master):
    'فريم تحليل البيانات'
    
    marging_py = 10
    pg_font = ('times',13,'bold')



    meter_size = 230


    global analyzer_data
    # الفريم الاساسي
    basic_frame_analyzer = Frame(master,) # فريم اساسي
    basic_frame_analyzer.pack(fill='both', expand=True) 
    
    

###########################################################################
    personal_info = LabelFrame(basic_frame_analyzer,text='بيانات معلومات المندوب', borderwidth=3) # فريم اداوت  البحث
    personal_info.pack(fill='both')
    
    # user_name = Label(personal_info, text='أسم المتخدم')
    # user_name.grid(row=0, column=1)

    def analyzer_data(*args):
        from_date = from_date_choose_date_search.entry.get()
        to_date = to_date_choose_date_search.entry.get()
        
        # تحليل حسب اليوم|حسب تاريخ
        track_option_type = track_option_type_id.get()

        if track_option_type != 'اليوم':
            from_date = from_date_choose_date_search.entry.get() 
            to_date = to_date_choose_date_search.entry.get()

        # لتحليل البيانات
        # try:
            data = SQL_DB.data_analyzer(from_date,to_date,track_option_type)
            if data == []:
                return

            val0 = data[0][0]
            val1 = data[0][1]
            val2 = data[0][2]
            val3 = data[0][6]
            val4 = data[0][11]
            val5 = data[0][12] # إجمالي المنصرفات مالية
            val6 = data[0][13] # إجمالي المنصرفات عددية
            
            
            for c0 in range(int(val0+1)):
                total_action.configure(amountused=c0, amounttotal=data[0][1])
                total_action.update()

            for c1 in range(int(val1+1)):
                total_data_entries.configure(amountused=c1, amounttotal=data[0][0])
                total_data_entries.update()
            
            for c3 in range(int(val3+1)):
                total_order_with_drivers.configure(amountused=c3, amounttotal=data[0][0])
                total_order_with_drivers.update()

            
            for c4 in range(int(val4+1)):
                total_order_int_store.configure(amountused=c4, amounttotal=data[0][0])
                total_order_int_store.update()
                            
            for c2 in range(int(val2+1)):
                total_collection.configure(amountused=c2, amounttotal=data[0][0])
                total_collection.update()

            for c5 in range(int(val6+1)):
                total_expenses_count.configure(amountused=c5, amounttotal=data[0][0])
                total_expenses_count.update()
            
            # for c5 in range(int(val5+1)):
                # total_expenses_amount.configure(amountused=c5, amounttotal=data[0][3])
                # total_expenses_amount.update()
            
            

            # إجمالي حركات
            # total_action.configure(amountused=data[0][0], amounttotal=data[0][1])
            # إجمالي العددي للحركات على البرنامج
            # total_data_entries.configure(amountused=data[0][1], amounttotal=data[0][0])
            # إجمالي العددي للشحنات التي تم تحصيلاها
            # total_collection.configure(amountused=data[0][2], amounttotal=data[0][0])
            # إجمالي العددي للشحنات التي في استلام المناديب
            # total_order_with_drivers.configure(amountused=data[0][6], amounttotal=data[0][0])
            # إجمالي العددي للشحنات في المخزن
            # total_order_int_store.configure(amountused=data[0][11], amounttotal=data[0][0])
            
            # إجماليات المالية
            total_action_amount.configure(amountused=data[0][3], amounttotal=data[0][3])
            # إجمالي الشحنات الموجودة في المستودع و مع المناديب
            total_order_unrecevied_amount.configure(amountused=data[0][7], amounttotal=data[0][3])
            # جاري توصيلة مع المناديب
            total_order_with_drivers_amount.configure(amountused=data[0][9], amounttotal=data[0][3])
            # إجمالي التحصيلات
            total_collection_amount.configure(amountused=data[0][5], amounttotal=data[0][3])
            # إجمالي الشحنات في المستودع
            total_order_int_store_amount.configure(amountused=data[0][8], amounttotal=data[0][3])

            total_expenses_amount.configure(amountused=data[0][12], amounttotal=data[0][3])
            
            # total_orders_received.configure(amountused=data[0][4][0][0])
            # data = Data.fetch_analyzer(user_id=track_driver_id.get())
            # print(data[3][0][0], type(data[3][0][0]))
            # print(data[2],data[3][0][0])
        #     return True
        # except ZeroDivisionError as e:
        #     print(f"Data Analyzer Is Crashed.{e}")
        

    
    # button_reset_date = Button(personal_info, text='معلومات',
    #                         cursor='hand2', bootstyle='info',)
    # button_reset_date.pack(fill='both', pady=4, padx=4, side='left')
    
    track_option_type_id = StringVar(value='اليوم')
    track_option_type = Combobox(personal_info, values=['اليوم','الكل'], justify='center',
                        state='readonly', textvariable=track_option_type_id, cursor='hand2')
    # e_driver_name.grid(row=0, column=0)
    track_option_type.pack(side='left')
    track_option_type.set(value='اليوم')

    
    track_option_type_id.trace('w', callback=analyzer_data)
    
    
    from_date_label_search = Label(personal_info, text='من تاريخ')
    from_date_label_search.pack(side='right', padx=6)
    
    from_date_choose_date_search = DateEntry(personal_info, dateformat='%Y-%m-%d', width=10 )
    from_date_choose_date_search.pack(fill='both', side='right')
    
    to_date_label_search = Label(personal_info, text='إلى تاريخ')
    to_date_label_search.pack(side='right', padx=6)

    to_date_choose_date_search = DateEntry(personal_info, dateformat='%Y-%m-%d', width=10)
    to_date_choose_date_search.pack(fill='both', side='right')




###########################################################################

    piechart_info = ScrolledFrame(basic_frame_analyzer) # فريم عرض الاداء
    piechart_info.pack(fill='both', expand=True)
    

############################################################################


    # إدعدادات المتر
    thickness = 30
    
    # فريم المجاميع
    piechart_info_total = LabelFrame(piechart_info, text='لمحة عن الحركة اليومية') # فريم إجمالي الحركات
    piechart_info_total.pack(fill='both', expand=True, padx=1, pady=1)
    

    total_action = tb.Meter(piechart_info_total,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='إجمالي الحركات',
                            bootstyle='primary',
                            textleft='حركة',
                            meterthickness=thickness
                            )
    total_action.grid(row=0, column=0,padx=10)
    # total_action.pack(side='left')
    


    total_data_entries = tb.Meter(piechart_info_total,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='إجمالي المدخلات',
                            textleft='حركة',
                            bootstyle='success',
                            meterthickness=thickness
                            )
    total_data_entries.grid(row=0, column=1)
    # total_data_entries.pack(side='left')

    total_order_with_drivers = tb.Meter(piechart_info_total,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='جاري توصيلة',
                            bootstyle='INFO',
                            textleft='حركة',
                            meterthickness=thickness
                            )
    total_order_with_drivers.grid(row=0, column=2)
    # total_order_with_drivers.pack(side='left')
    
    total_order_int_store = tb.Meter(piechart_info_total,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='شحنات في المستودع',
                            bootstyle='warning',
                            textleft='حركة',
                            meterthickness=thickness
                            )
    # total_order_int_store.pack(side='left')
    total_order_int_store.grid(row=0, column=3)

    total_collection = tb.Meter(piechart_info_total,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='إجمالي التحصيلات',
                            textleft='حركة',
                            meterthickness=thickness,
                            bootstyle='SUCCESS'
                            )
    total_collection.grid(row=0, column=4)
    # total_collection.pack(side='left')

    # total_orders_received = tb.Meter(piechart_info_total,
    #                         metersize=meter_size,
    #                         amounttotal=1200,
    #                         amountused=0,
    #                         subtext='إجمالي التسليم',
    #                         meterthickness=thickness
    #                         )
    # # total_orders_received.grid(row=0, column=3)
    # total_orders_received.pack(side='left')

    total_expenses_count = tb.Meter(piechart_info_total,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='إجمالي المنصرفات',
                            textleft='حركة',
                            meterthickness=thickness,
                            bootstyle='DANGRES'
                            )
    total_expenses_count.grid(row=0, column=5, )
    
    # total_orders_in_serveices.pack(side='left')

    r,c = 7,7
    for x in range(r):
        piechart_info_total.grid_rowconfigure(x, weight=1, pad=2)
    for v in range(c):
        piechart_info_total.grid_columnconfigure(v, weight=1)
            
    
    # piechart_info_total.rowconfigure(0, weight=0)
    # piechart_info_total.columnconfigure(0, weight=0,)
    # piechart_info_total.columnconfigure(0, weight=1)
    # piechart_info_total.columnconfigure(0, weight=2)
    # piechart_info_total.columnconfigure(3, weight=3) exceptability
    # piechart_info_total.columnconfigure(4, weight=4)
    # piechart_info_total.columnconfigure(5, weight=5)








##########################################################################################################################################


    # المجاميع المالية
    
    piechart_info_total_amount = LabelFrame(piechart_info, text='لمحة عن الحركة المالية') # فريم إجمالي الحركات
    piechart_info_total_amount.pack(fill='both', expand=True, padx=1, pady=1)


    total_action_amount = tb.Meter(piechart_info_total_amount,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='إجمالي الإيرادات',
                            bootstyle='info',
                            textleft='ريال',
                            meterthickness=thickness
                            )
    total_action_amount.grid(row=0, column=0,padx=10)
    # total_action_amount.pack(side='left')

    total_order_unrecevied_amount = tb.Meter(piechart_info_total_amount,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='إجمالي الشحنات الكلية',
                            bootstyle='success',
                            textleft='ريال',
                            meterthickness=thickness
                            )
    total_order_unrecevied_amount.grid(row=0, column=1)
    # total_order_unrecevied_amount.pack(side='left')

    total_order_with_drivers_amount = tb.Meter(piechart_info_total_amount,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='جاري توصيلة',
                            bootstyle='INFO',
                            textleft='ريال',
                            meterthickness=thickness
                            )
    total_order_with_drivers_amount.grid(row=0, column=2)
    # total_order_with_drivers_amount.pack(side='left')

    total_order_int_store_amount = tb.Meter(piechart_info_total_amount,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='في المستودع',
                            bootstyle='warning',
                            textleft='ريال',
                            meterthickness=thickness
                            )
    total_order_int_store_amount.grid(row=0, column=3)
    # total_order_int_store_amount.pack(side='left')



    total_collection_amount = tb.Meter(piechart_info_total_amount,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='إجمالي التحصيلات',
                            meterthickness=thickness,
                            textleft='ريال',
                            bootstyle='info'
                            )
    total_collection_amount.grid(row=0, column=4)
    # total_collection_amount.pack(side='left')

    # total_orders_received_amount = tb.Meter(piechart_info_total_amount,
    #                         metersize=meter_size,
    #                         amounttotal=1200,
    #                         amountused=0,
    #                         subtext='إجمالي الإجل',
    #                         meterthickness=thickness,
    #                         textleft='ريال',
    #                         )
    # # total_orders_received_amount.grid(row=0, column=4)
    # total_orders_received_amount.pack(side='left')

    total_expenses_amount = tb.Meter(piechart_info_total_amount,
                            metersize=meter_size,
                            amounttotal=1200,
                            amountused=0,
                            subtext='إجمالي الإلغاءات',
                            meterthickness=thickness,
                            textleft='ريال',
                            )
    total_expenses_amount.grid(row=0, column=5)
    # total_orders_cancellection_amount.pack(side='left')
    
    r,c = 7,7
    for x in range(r):
        piechart_info_total_amount.grid_rowconfigure(x, weight=1, pad=2)
    for v in range(c):
        piechart_info_total_amount.grid_columnconfigure(v, weight=1)
            
    # def update_analyzer():
    #     analyzer_data()
    #     piechart_info.after(2000,analyzer_data())
    # update_analyzer()

    # analyzer_data()
    


    
    
    
    
    
    
    