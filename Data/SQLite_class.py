import sqlite3, time
from time import strftime





class SQL_DB:
    def __init__(self,db_name):
        self.con = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.con.cursor()
        
        
    # Connection to sqlite3 database
    

    """
    كلاس قاعدة البيانات المظام\n
    إضافة,
    حذف,
    تعديل,
    """
    def tables_creation():
         "تقوم ببناء جداول النظام "
         'Talbes Builde , Creation Talbles If The Table Deleted'
         cur.execute('''CREATE TABLE IF NOT EXISTS MotherBase(       
            id_serial INT, payment_status TEXT,order_status TEXT,order_id_shipment TEXT,
            payment_type TEXT, customer_name TEXT, customer_phone TEXT, price INT,
            driver TEXT,notes TEXT, date_creation TEXT,time_creation TEXT,date_end TEXT, time_end TEXT
                     )
        ''')
         cur.execute('''CREATE TABLE IF NOT EXISTS ActualBase(     
            id_serial INT,payment_status TEXT,order_status TEXT,order_id_shipment TEXT,payment_type TEXT,customer_name TEXT,customer_phone TEXT,price INT,driver TEXT,
            notes TEXT,date_creation TEXT, time_creation TEXT, date_end TEXT, time_end TEXT
                     )
        ''')
         cur.execute('CREATE TABLE IF NOT EXISTS Thems(id INT ,name TEXT, choose_theme TEXT)')

         # إنشاء قاعدة بيانات السائقين
         cur.execute('CREATE TABLE IF NOT EXISTS DriversBase(id INT , name TEXT, phone TEXT)')
         con.commit()
         
         # إنشاء قاعدة بيانات المنصرفات
         cur.execute('''
                     CREATE TABLE IF NOT EXISTS Expenses(
                         serial INT ,
                         expenses_type TEXT,
                         drivre TEXT,
                         price TEXT,
                         odometer_count TEXT,
                         note TEXT,
                         date_creation TEXT,
                         time_creation TEXT
                         )''')
         con.commit()




    def add_new_driver(id,name,phone):
        # إضافة سائق جديد
        cur.execute(f'INSERT INTO DriversBase VALUES ("{id}","{name}","{phone}")')
        con.commit()

    def receive_order(id):
        # تغيير حالة السجل إلى تم التسليم
        date_end = strftime('%Y-%m-%d')
        time_end = strftime('%H:%M:%S')
        'Update status of order to receive by customer'
        cur.execute(f'UPDATE ActualBase SET order_status="تم التسليم", date_end="{date_end}", time_end="{time_end}" WHERE id_serial="{id}"')
        con.commit()


    def fetch_drivers_data():
        return cur.execute('SELECT * FROM DriversBase').fetchall()

    def fetch_list_drivers_name():
        'ترجع أسماء المناديب المسجلة'
        list_driver = []
        for x in cur.execute('SELECT name FROM DriversBase').fetchall():
            list_driver.append(f'{x[0]}')
        list_driver.append('غير معرف')
        list_driver.append('الكل')
        return list_driver


        def add_thems():
            'إضافة الثيمات في اول تشغيل للبرنامج'
            list_theme = [
                'flatly','cyborg','solar','darkly','superhero','vapor','morph',
                'yeti','cosmo','litera','simplex','minty','sandstone','journal',
                'lumen','pulse','cerculean'	
            ]
            count = 0
            for v in list_theme:
                c = 'Fales'
                count +=1
                if count == 16:
                    c = 'True'
                cur.execute(f'INSERT INTO Thems VALUES("{count}","{v}","{c}")')
            print('FFFF')
            con.commit()

    def get_theme():

        theme_name = 'vapor'
        try:
            d = cur.execute('SELECT count(id) FROM Thems').fetchall()[0][0]
            if d == 0:
                theme_name = ''
            for t in cur.execute('SELECT name FROM Thems WHERE choose_theme = "True"'):
                theme_name = t[0]
            return theme_name
        except:
            return 'vapor'

    def get_list_theme():
        list_theme_name = []
        for t in cur.execute('SELECT name FROM Thems'):
            list_theme_name.append(t[0])
        return list_theme_name
    
    def switch_theme_color(theme_name,old_theme_name):
        # print('New Theme: ', theme_name,'Old Theme: ', old_theme_name)
        if theme_name == old_theme_name or theme_name =='' or old_theme_name == '':
             return
        cur.execute(f'UPDATE Thems set choose_theme = "False" WHERE name = "{old_theme_name}"')
        # con.commit()
        cur.execute(f'UPDATE Thems set choose_theme = "True" WHERE name = "{theme_name}"')
        con.commit()

    def generate_order_serial():
            cur.execute('SELECT id_serial FROM MotherBase')
            id_ = cur.fetchall()
            info = (id_)
            if info == []:
                order_id=1
            else:
                for s in cur.execute('SELECT id_serial FROM MotherBase'):
                        order_id= (f'{s[0]+1}')
            return order_id

    def add_new_order(price,customer_name,customer_phone,
                    notes,payment_type,order_id_shipment,driver,payment_status,
                    order_status):
        date= strftime('%Y-%m-%d')
        time = strftime('%H:%M:%S')

        # إدخال بيانات في قاعدة البيانات أساسية
        serial = int(SQL_DB.generate_order_serial())
        cur.execute(f'''INSERT INTO MotherBase (
            id_serial ,payment_status ,order_status ,order_id_shipment ,payment_type ,
            customer_name ,customer_phone ,price ,driver ,notes , date_creation , time_creation
                    )
                    VALUES(
                    "{serial}","{payment_status}","{order_status}","{order_id_shipment}",
                    "{payment_type}","{customer_name}",
                    "{customer_phone}","{price}","{driver}","{notes}","{date}","{time}"
                    )''')
        con.commit()


        # إدخال بيانات في قاعدة البيانات الفعلية
        cur.execute(f'''INSERT INTO ActualBase (
            id_serial ,payment_status ,order_status ,order_id_shipment ,payment_type ,
            customer_name ,customer_phone ,price ,driver,notes , date_creation , time_creation
                    )
                    VALUES(
                    "{serial}","{payment_status}","{order_status}","{order_id_shipment}","{payment_type}",
                    "{customer_name}","{customer_phone}","{price}","{driver}","{notes}","{date}","{time}"
                    )''')
        con.commit()



    def edit_orders(id_serial,customer_name,customer_phone,price,order_id_shipment,driver,payment_type,notes):
        # تعديل بيانات في قاعدة البيانات الفعلية
        cur.execute(f'''UPDATE ActualBase SET
            customer_name ="{customer_name}", customer_phone = "{customer_phone}",price  ="{price}",order_id_shipment = "{order_id_shipment}",driver = "{driver}",payment_type = "{payment_type}",notes = "{notes}"
            WHERE id_serial ="{id_serial}"
                    ''')
        con.commit()

        
        
    def fetch_order_data(driver):
        'تقوم بإرجاع السجلات التي تحت المعالجة مثل المرتجع و الشحنات مع المناديب'
        try:
            if driver == '' or driver =='الكل':
                driver = 'driver'
            count =cur.execute(f'SELECT COUNT(PRICE) FROM ActualBase WHERE order_status !="تم التسليم" AND  driver ="{driver}"').fetchall()[0][0],
            sums = f"ريال {cur.execute(f'SELECT SUM(PRICE) FROM ActualBase WHERE order_status !="تم التسليم" AND  driver ="{driver}"').fetchall()[0][0]:,.2f}",
            data = cur.execute(f'SELECT * FROM ActualBase WHERE order_status !="تم التسليم" AND  driver ="{driver}"').fetchall(),

            datalist = []
            countLine = 0
            for x in data[0]:
                countLine+=1
                t = (x[0],x[3],f"{x[7]:,.2f}",x[6],x[5],x[8],(x[10],x[11]),x[9],countLine)
                
                datalist.append(t)
            return datalist,count,sums
        except:
            return cur.execute(f'SELECT * FROM ActualBase WHERE order_status !="تم التسليم" AND  driver ="{driver}"').fetchall(), '0.00 ريال','0'






    def fetch_collection_money_report(driver, from_date, to_date):
        'بيانات تقرير التحصيلات'
        try:
            'تقوم بإرجاع التقرير المطلوب'
            if driver == '' or driver =='الكل':
                driver = 'driver'
                
            report =cur.execute(f'SELECT * FROM ActualBase WHERE driver ="{driver}" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}" ORDER BY date_end ASC').fetchall()
            collection_count = cur.execute(f'SELECT COUNT(PRICE) FROM ActualBase WHERE driver ="{driver}" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}"').fetchall()[0][0]
            collection_sum = f"ريال {cur.execute(f'SELECT SUM(PRICE) FROM ActualBase WHERE driver = "{driver}" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}"').fetchall()[0][0]:,.2f}"
            
            return report,collection_count,collection_sum
        except :
            return cur.execute(f'SELECT * FROM ActualBase WHERE driver ="{driver}" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}"').fetchall(), '0','0.00 ريال'




    def fetch_collection_money_report_summary(driver,from_date,to_date):
        try:
            if driver =='الكل':
                list_driver = SQL_DB.fetch_list_drivers_name()
                counter = 0
                datalist = []
                for x in list_driver:
                    data = cur.execute(f'SELECT SUM(price), COUNT(price) FROM ActualBase WHERE date_end BETWEEN "{from_date}" AND "{to_date}"AND order_status ="تم التسليم" AND driver ="{x}"').fetchall()
                    counter +=1
                    if data[0][0] == None:
                        counter-=1
                        continue
                    datalist.append((x, data[0][0],data[0][1],counter))
                    
                return datalist,f"ريال {cur.execute(f'SELECT SUM(PRICE) FROM ActualBase WHERE driver = "driver" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}"').fetchall()[0][0]:,.2f}",cur.execute(f'SELECT COUNT(PRICE) FROM ActualBase WHERE driver ="driver" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}"').fetchall()[0][0]
            
            count = 0 
            if driver !='الكل':
                datalist = []
                data = cur.execute(f'SELECT SUM(price), COUNT(price) FROM ActualBase WHERE date_end BETWEEN "{from_date}" AND "{to_date}"AND order_status ="تم التسليم" AND driver ="{driver}"').fetchall()
                count+=1
                if data[0][0] == None:
                    return
                datalist.append((driver,data[0],data[0],count))
                return datalist
        except:
            if driver =='الكل':
                list_driver = SQL_DB.fetch_list_drivers_name()
                counter = 0
                datalist = []
                for x in list_driver:
                    data = cur.execute(f'SELECT SUM(price), COUNT(price) FROM ActualBase WHERE date_end BETWEEN "{from_date}" AND "{to_date}"AND order_status ="تم التسليم" AND driver ="{x}"').fetchall()
                    counter +=1
                    if data[0][0] == None:
                        counter-=1
                        continue
                    datalist.append((x, data[0][0],data[0][1],counter))
                return datalist,'00.0 ريال','0'






    def fetch_order_data_reports(driver,order_status,from_date,to_date):
            'بيانات إدرة الشحنات'
        # try:
            'جلب بيانات تقرير الشحنات بكل حالاتها'
            if driver == '' or driver =='الكل':
                driver = 'driver'
            
            if  order_status == 'الكل':
                order_status = 'order_status'
                
            # if order_status == 'جاري التوصيل' and driver == 'غير معرف':
            #     data = cur.execute(f'SELECT * FROM ActualBase WHERE driver !="{driver}" AND order_status ="{order_status}"').fetchall()
            #     sum = cur.execute(f'SELECT SUM(PRICE) FROM ActualBase WHERE driver !="غير معرف" AND order_status ="جاري التوصيل"').fetchall()[0][0]
            #     if sum == None:
            #         sum = '00.0ريال'
            #         print('Pro')
            #     count = cur.execute(f'SELECT COUNT(PRICE) FROM ActualBase WHERE driver !="{driver}" AND order_status ="{order_status}"').fetchall()
            #     return data,sum,count
            
            # sum = '00.0ريال'
            
            data = cur.execute(f'SELECT * FROM ActualBase WHERE driver ="{driver}" AND order_status ="{order_status}" AND date_creation BETWEEN "{from_date}" AND "{to_date}"').fetchall()
            
            sum = cur.execute(f'SELECT SUM(PRICE) FROM ActualBase WHERE driver ="{driver}" AND order_status ="{order_status}" AND date_creation BETWEEN "{from_date}" AND "{to_date}"').fetchall()
            count = cur.execute(f'SELECT COUNT(PRICE) FROM ActualBase WHERE driver ="{driver}" AND order_status ="{order_status}"').fetchall()[0][0]
            
            if sum[0][0] != None:
                sum = f"ريال {cur.execute(f'SELECT SUM(PRICE) FROM ActualBase WHERE driver ="{driver}" AND order_status ="{order_status}" AND date_creation BETWEEN "{from_date}" AND "{to_date}"').fetchall()[0][0]:,.2f}"
            if sum[0][0] == None:
                sum = '00.0 ريال'
            if count == None:
                count = '0'
            return data,sum,count

        # except :
        #     return cur.execute(f'SELECT * FROM ActualBase WHERE driver ="{driver}"').fetchall(), '0.00 ريال','0'



    def get_balance_total_report():
        'Fetch sum of recive mony from drivre' 
        date = strftime('%Y-%m-%d')
        try:
            return f"ريال {cur.execute(f'SELECT SUM(PRICE) FROM ActualBase WHERE  order_status ="تم التسليم" AND date_creation LIKE "%{date}%" OR date_end LIKE "%{date}%"').fetchall()[0][0]:,.2f}"
        except:
            return 'ريال0.00'

    def fetch_all_recorder_detials(id):
        return cur.execute(f'SELECT * FROM ActualBase WHERE id_serial ="{id}"').fetchall()

    def delete_recorder(id_serial):
         """
         Delete Recorder from Table (ActualBase)
         """
         cur.execute(f'DELETE  FROM ActualBase WHERE id_serial ="{id_serial}"')
         con.commit()

    def data_analyzer(from_date,to_date,type_analyzer):
            
            from_d = from_date
            t_date = to_date
            option = type_analyzer

            if option =='الكل':
                from_date = 'date_creation'
                to_date = 'date_creation'
                from_d = 'date_end'
                t_date = 'date_end'
            
            listdata = []
            
            
            # جلب البيانات الحركات اليومية إدخال
            total_add_count = 0
            count_add = cur.execute(f'SELECT COUNT(id_serial) FROM ActualBase WHERE date_creation BETWEEN "{from_date}" AND "{to_date}" AND order_status ="جاري التوصيل"').fetchall()
            if count_add[0][0] !=None:
                total_add_count = count_add[0][0]
            
            # جلب البيانات الحركات اليومية إدخال
            total_end_count = 0
            count_end = cur.execute(f'SELECT COUNT(id_serial) FROM ActualBase WHERE date_end BETWEEN "{from_d}" AND "{t_date}"').fetchall()
            if count_end != None:
                total_end_count = count_end[0][0]
            # print(total_end_count)
            
           
            # print(int(total_add_count)+int(total_end_count) )
            
            # جلب البيانات المالية الاموال التي تم تحصيلها حسب التاريخ  
            total_add_sum = 0
            total_add_sums = cur.execute(f'SELECT SUM(price) FROM ActualBase WHERE date_creation BETWEEN "{from_date}" AND "{to_date}" AND order_status ="جاري التوصيل"').fetchall()
            if total_add_sums[0][0] != None:
                total_add_sum = total_add_sums[0][0]
            

            # عدد الشحنات مع المناديب
            total_order_with_driver = 0
            total_order_with_drivers = cur.execute('SELECT COUNT(price),SUM(price) FROM Expenses').fetchall()
            
            if total_order_with_drivers[0][0] != None:
                total_order_with_driver = total_order_with_drivers[0][0]
            
            
            # إجمالي الشحنات مع المناديب
            total_order_with_driver_sum = 0
            total_order_with_driver_count = 0
            total_order_with_driver_sums = cur.execute(f'SELECT SUM(price), COUNT(price) FROM ActualBase WHERE  date_creation BETWEEN "{from_date}" AND "{to_date}" AND order_status ="جاري التوصيل" AND driver !="غير معرف"').fetchall()
            if total_order_with_driver_sums[0][0] != None:
                total_order_with_driver_sum = total_order_with_driver_sums[0][0]
                total_order_with_driver_count = total_order_with_driver_sums[0][1]



            # إجمالي الشحنات التي في المستودع
            total_order_with_driver_or_in_store_sum = 0
            total_order_with_driver_or_in_stores = cur.execute(f'SELECT SUM(price),COUNT(price) FROM ActualBase WHERE  date_creation BETWEEN "{from_date}" AND "{to_date}" AND order_status ="جاري التوصيل"').fetchall()
            if total_order_with_driver_or_in_stores[0][0] != None:
                total_order_with_driver_or_in_store_sum = total_order_with_driver_or_in_stores[0][0]
            
            # إجمالي الشحنات التي في المستودع
            total_order_in_store_sum = 0
            total_order_in_store_count = 0
            total_order_in_store_sums = cur.execute(f'SELECT SUM(price),COUNT (price) FROM ActualBase WHERE  date_creation BETWEEN "{from_date}" AND "{to_date}" AND order_status ="جاري التوصيل" AND driver ="غير معرف"').fetchall()
            if total_order_in_store_sums[0][0] != None:
                total_order_in_store_sum = total_order_in_store_sums[0][0]
                total_order_in_store_count = total_order_in_store_sums[0][1]
            

            # إجمالي الشحنات المحصلة
            total_end_sum = 0
            total_end_sums = cur.execute(f'SELECT SUM(id_serial),COUNT(price) FROM ActualBase WHERE  date_end BETWEEN "{from_d}" AND "{t_date}" AND order_status ="تم التسليم"').fetchall()
            if total_end_sums[0][0] != None:
                total_end_sum = total_end_sums[0][0]
            
            # إجمالي المنصرفات عدديه و ماليه
            total_expenses_sum = 0
            total_expenses_sums = cur.execute(f'SELECT SUM(price),COUNT(price) FROM Expenses').fetchall()
            if total_expenses_sums[0][0] != None:
                total_expenses_sum = total_expenses_sums[0][0]
                total_expenses_count = total_expenses_sums[0][1]

            total_atcion = int(total_add_count)+int(total_end_count)+int(total_expenses_count)
            
            
            total_atcion_sum = float(total_add_sum)+float(total_end_sum)
            
            # عمل كل القيمة المعمول عليهاتحليل
            listdata.append((total_atcion,total_add_count,
                             total_end_count,total_atcion_sum,total_add_sum,
                             total_end_sum,total_order_with_driver,
                             total_order_with_driver_or_in_store_sum,total_order_in_store_sum,
                             total_order_with_driver_sum,total_order_with_driver_count,
                             total_order_in_store_count,total_expenses_sum,total_expenses_count))
                    
            print(listdata)
            
            return listdata
        
        # except:
        #     pass
        # return total_atcion,total_add_count,total_end_count,total_atcion_sum,total_add_sum,total_end_sum
        # return total_atcion,total_add_count,total_end_count, total_atcion_sum

            
    def generate_order_serial_expenses():
            cur.execute('SELECT serial FROM Expenses')
            id_ = cur.fetchall()
            info = (id_)
            if info == []:
                order_id=1
            else:
                for s in cur.execute('SELECT serial FROM Expenses'):
                        order_id= (f'{s[0]+1}')
            return order_id


    def add_expenses(
        serial,epxenses_type,drivre,price,note,odometer_count):
        serial=SQL_DB.generate_order_serial_expenses()
        date_creation = strftime('%Y-%m-%d')
        time_creation = strftime('%H:%M:%C')
        
        cur.execute(f'INSERT INTO Expenses VALUES("{serial}","{epxenses_type}","{drivre}","{price}","{odometer_count}","{note}","{date_creation}","{time_creation}")')
        con.commit()

    def fetch_expenses_report():
        'جلب تقرير المصروفات'
        data = cur.execute('SELECT * FROM Expenses').fetchall()
        sums = cur.execute('SELECT SUM(price) FROM Expenses').fetchall()
        count = cur.execute('SELECT COUNT(price) FROM Expenses').fetchall()
        datalist = []
        counter = 0
        for x in data:
            counter += 1
            datalist.append((x[0],x[5],x[3],x[2],x[4],x[1],(x[6],x[7]), counter))
        return datalist,f"ريال {sums[0][0]}",count[0][0]




a = SQL_DB(db_name='Data\\Data.db')
print(a.generate_order_serial())