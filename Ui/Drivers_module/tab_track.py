from config.Libaries import *
# إستدعاء إعدادات النظام
from config.sys_classes import *

from Ui.Drivers_module.Track_drivers_frame import Track_drivers_frame
from Ui.Drivers_module.View_order_details import View_order_details_frame


def Track_drivers_tab(master):
    
    note_book = Notebook(master, cursor='hand2')
    note_book.pack(fill='both', expand=True)
    
    # شاشة التببع 
    tracke_drivers_and_orders = Frame(note_book)
    Track_drivers_frame(master=tracke_drivers_and_orders)
    note_book.add(tracke_drivers_and_orders, text='📍 شاشة التتبع')
    
    # شاشة بيانات الشحنات 
    view_order_details_frame = Frame(note_book)
    View_order_details_frame(master=view_order_details_frame)
    note_book.add(view_order_details_frame, text='📍 تفاصيل الشحنات')
    