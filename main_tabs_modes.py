# إستدعاء المكاتب المطلوبة
from config.Libaries import *

# إستدعاء إعدادات النظام
from config.sys_classes import *

# إستدعاء واجهات رسومية
from Ui.Consignmets_Report_Module.Shipments_crud_controller_frame import Controller_and_view_recorder_frame
from Ui.Consignmets_Report_Module.Shipments_report_frame import Shipment_viewer_report_frame
from Ui.Consignmets_Report_Module.Shipments_collection_full_report_frame import Collection_money__full_report_frame
from Ui.Drivers_module.Drivers_report_collections_assignments_return_shipment_frame import Drivers_report_collections_asaginment_back_shipment_frame
from Ui.statistics.Data_analyzer_frame import analyzer_data_frame
from Ui.Drivers_module.tab_track import Track_drivers_tab


def MyApp(user):
    'تشغيل الظام'
    # page = tb.Window(themename=SQL_DB.get_theme())
    page = tb.Window(themename='cyborg')
    page.title('سريع إكسبريس')
    page.geometry('1610x980+160+0')
    # توسيط الواجهه في نص شاشة الكمبوتبر
    sys_class.centering_window(window=page)
    page.iconbitmap(sys_icon)
    
    # # تعريف الصور الخاصة بالازرار او الخلفيات
    img = Image.open('Assets\\Img\\erp.png').resize((250,250))
    # img = Image.open('Module\\sys_Image\\good-morning-morning-flowers.gif')
    home_img_logo = ImageTk.PhotoImage(img)


    # تاب الصفحه الرئيسية
    note_book = Notebook(page, cursor='hand2')
    note_book.pack(fill='both', expand=True)
    
    # "(إدخال,تعديل,تسليم)تحكم بالشحنات"
    controller_add_del_edit_tab = Frame(note_book)
    Controller_and_view_recorder_frame(master=controller_add_del_edit_tab,home_img_logo=home_img_logo)
    
    # تقرير كل الحالات
    report_all_cases_shipment = Frame(note_book)
    Shipment_viewer_report_frame(master=report_all_cases_shipment)
    
    # تقرير التحصيلات بيانات كامله
    report_collections_report = Frame(note_book)
    Collection_money__full_report_frame(master=report_collections_report)
    
    # تقرير تحصيلات المناديب
    drivers_collections_report = Frame(note_book)
    Drivers_report_collections_asaginment_back_shipment_frame(master=drivers_collections_report)
    
    # شاشة التببع 
    tracke_drivers_and_orders = Frame(note_book)
    Track_drivers_tab(master=tracke_drivers_and_orders)
    
    # تحليل البيانات
    data_analyzer = Frame(note_book)
    analyzer_data_frame(master=data_analyzer)
    
    # إضافة الفريمات
    note_book.add(controller_add_del_edit_tab, text='🏠 إدارة الشحنات')
    note_book.add(report_all_cases_shipment, text='🧾 تقرير الشحنات')
    note_book.add(report_collections_report, text='💸تقرير التحصيل')
    note_book.add(drivers_collections_report, text='👤تقرير المناديب')
    note_book.add(tracke_drivers_and_orders, text='📍 شاشة التتبع')
    note_book.add(data_analyzer, text='📊 تحليل البيانات')
    
    page.mainloop()
    

MyApp(user=500)