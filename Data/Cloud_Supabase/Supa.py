# إستدعاء المكاتب المطلوبة
from config.Libaries import *

#  ضع هنا بيانات مشروعك
URL = "https://sfsgukmfmqcoupuctgzz.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNmc2d1a21mbXFjb3VwdWN0Z3p6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc0MjkyODQsImV4cCI6MjA3MzAwNTI4NH0.ahRc9kvE3CkwR_F61BEcIuuZNWsLwrnANjQPtwZQWmg"


# supabase إنشاء أتصال مع 
supabase: Client = create_client(URL, KEY)



class Supa:
    'Supabase class for crud sql queires| التعامل مع الإستظافة'
    def generate_order_serial():
        'supabase'
        id = supabase.table('Consignments_management').select('id_serial').order('id_serial', desc=True).execute()
        serial = 0
        ls = []
        for x in id.data:
            ls.append(x['id_serial'])
        if ls[:1] == []:
            serial = 1
        else:
            serial = int(ls[:1][0]) + 1
        return serial
        

    # Supa للتعامل مع قاعدة بيانات  
    def build_table_cloud_Supa():
        pass

    def add_delivery_order(price,customer_name,customer_phone,
                    notes,order_id_shipment,driver,
                    customer_location,customer_street):
        'إضافة طلب توصيل جديدة'
        
        try:
            date= strftime('%Y-%m-%d')
            time = strftime('%H:%M:%S')
            serial = Supa.generate_order_serial()
            data = {
                'id_serial':serial,
                'customer_name':customer_name,
                'customer_phone':customer_phone,
                'delivery_cost_price':price,
                'driver':driver,
                'date_creation':date,
                'time_creation':time,
                'date_end':'Null',
                'time_end':'Null',
                'customer_location':customer_location,
                'customer_street':customer_street,
                'order_id_shipment':order_id_shipment,
                'note':notes,
                'order_status':'إنتظار الإلتقاط',
                }
            # إدخال بيانات الشحنة الجديدة
            supabase.table('Consignments_management').insert([data]).execute()
        except ConnectionError as e:
                messagebox.showerror('ملاحضة', f'تأكد من إتصالك باالإنترنت ثم عاود المحاولة :{e}')
        except Exception as e:
                messagebox.showerror('ملاحضة', f'تأكد من إتصالك باالإنترنت ثم عاود المحاولة :{e}')
                return
        
    
    def receive_order(serial):
        'تعديل حالة السجل إلى تسليم العميل'
        supabase.table('actualbase').update({'order_status':'تم التسليم'}).eq('id_serial',str(serial)).execute()
    
    def fetch_collection_money_reports():
        'بيانات تقرير التحصيلات'
        # try:
        # 'تقوم بإرجاع التقرير المطلوب'
        # if driver == '' or driver =='الكل':
        #     driver = 'driver'
            
        # report =cur.execute(f'SELECT * FROM ActualBase WHERE driver ="{driver}" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}" ORDER BY date_end ASC').fetchall()
        count = 0
        datalist = []
        report = supabase.table('actualbase').select('*').order('id_serial', desc=False).execute()
        for x in report.data:
            count +=1
            datalist.append((x['id_serial'],x['order_id_shipment'],f'{float(x['price']):,.2f}',x['order_status'],x['customer_phone'],x['customer_name'],x['driver'],(x['date_creation'],x['time_creation']),x['notes'],count))
        return datalist
    

    def fetch_order_data(driver):
        driver=driver
        'تقوم بإرجاع السجلات التي تحت المعالجة مثل المرتجع و الشحنات مع المناديب'
        'بيانات تقرير التحصيلات'
        # try:

        report = supabase.table('actualbase').select('*').eq('driver',driver).execute()
        
        'تقوم بإرجاع التقرير المطلوب'
        if driver =='الكل' or driver =='':
            report = supabase.table('actualbase').select('*').execute()
        
        count = 0
        datalist = []
        for x in report.data:
            count +=1
            datalist.append((x['id_serial'],x['order_id_shipment'],f'{float(x['price']):,.2f}',x['customer_phone'],x['customer_name'],x['driver'],(x['date_creation'],x['time_creation']),x['notes'],count))
        return datalist
    
    def delete_recorder(serial):
        supabase.table('actualbase').delete().eq('id_serial',serial).execute()

        # collection_count = cur.execute(f'SELECT COUNT(PRICE) FROM ActualBase WHERE driver ="{driver}" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}"').fetchall()[0][0]
        # collection_sum = f"ريال {cur.execute(f'SELECT SUM(PRICE) FROM ActualBase WHERE driver = "{driver}" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}"').fetchall()[0][0]:,.2f}"
            
        #     return report,collection_count,collection_sum
        # except :
            
            # return cur.execute(f'SELECT * FROM ActualBase WHERE driver ="{driver}" AND order_status =="تم التسليم" AND date_end BETWEEN  "{from_date}" AND "{to_date}"').fetchall(), '0','0.00 ريال'

