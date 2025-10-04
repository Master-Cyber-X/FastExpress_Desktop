# إستدعاء المكاتب المطلوبة
from config.Libaries import *

# إستدعاء إعدادات النظام
from config.sys_classes import *

# إستدعاء واجهات رسومية
from Ui.Shipments_crud_controller_frame import Controller_and_view_recorder_frame
from Ui.Shipments_report_frame import Shipment_viewer_report_frame
from Ui.Shipments_collection_full_report_frame import Collection_money__full_report_frame
from Ui.Drivers_report_collections_assignments_return_shipment_frame import Driver_Collections_money_report_frame
from Ui.Data_analyzer_frame import analyzer_data_frame


# الأتصال بقاعدة البيانات
from Data.SQILite import SQL_DB


def MyApp(user):
    # page = tb.Window(themename=SQL_DB.get_theme())
    page = tb.Window(themename='CustomTheme')
    page.title('🏠 سريع إكسبريس')
    page.geometry('1610x980+160+0')
    # توسيط الواجهه في نص شاشة الكمبوتبر
    sys_class.centering_window(window=page)
    page.iconbitmap(sys_icon)
    
    menuList = Menubutton(page, text='إدارة التوصيل', cursor='hand2')
    menuList.pack()
    


    def open_window(master,title):
        'لفتح الفريمات في نوافذ | For open frame in side window'
        a = Toplevel()
        a.geometry('1510x880+160+0')
        a.title(title)
        # To launcher frame in window
        master(a) 
        a.mainloop()

    menu_option = Menu(menuList, cursor='hand2')
    menuList['menu']=menu_option

    menu_option.add_radiobutton(label='🏠 إدارة الشحنات', command=lambda:open_window(Controller_and_view_recorder_frame,'🏠 إدارة الشحنات'))
    menu_option.add_radiobutton(label='🧾 تقرير الشحنات', command=lambda:open_window(Shipment_viewer_report_frame,'🧾 تقرير الشحنات'))
    menu_option.add_radiobutton(label='💸تقرير التحصيل', command=lambda:open_window(Collection_money__full_report_frame,'💸تقرير التحصيل'))


    page.mainloop()
    
    
MyApp(user=500)