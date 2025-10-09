from config.Libaries import *
from config.sys_classes import *
from tkinter import PhotoImage
import random

def map_view(master):
    # ========== الأعلى ==========
    input_frame = Frame(master, padding=10)
    input_frame.pack(fill=X)

    Latitude = Label(input_frame, text="Latitude:")
    Latitude.pack(side=LEFT, padx=5)

    lat_entry = Entry(input_frame, width=10)
    lat_entry.pack(side=LEFT)

    Longitude = Label(input_frame, text="Longitude:")
    Longitude.pack(side=LEFT, padx=5)

    lon_entry = Entry(input_frame, width=10)
    lon_entry.pack(side=LEFT)

    # ========== الخريطة ==========
    map_widget = TkinterMapView(master, width=800, height=500, corner_radius=10)
    map_widget.pack(fill=BOTH, expand=True, padx=10, pady=10)
    map_widget.set_tile_server("https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}")  # خريطة طرق


    # إعداد مبدئي (الرياض)
    map_widget.set_position(24.7136, 46.6753)
    map_widget.set_zoom(5)

    # تحميل أيقونة السيارة
    car_icon = PhotoImage(file=r"Assets\Img\pgs-person.png")

    def search_location():
        try:
            lat = float(lat_entry.get())
            lon = float(lon_entry.get())

            # تحريك الخريطة
            map_widget.set_position(lat, lon)
            map_widget.set_zoom(100)

            # إضافة Marker مع أيقونة السيارة
            map_widget.set_marker(
                lat, lon,
                text=f"R- {random.randint(1,100)} المندوب ",
                icon=car_icon
            )

            # ✅ بعد البحث: تكبير النافذة
            master.state('zoomed')
            # أو استخدم التالي لو تفضل ملء الشاشة بالكامل:
            # master.attributes('-fullscreen', True)
            # master.bind("<Escape>", lambda e: master.attributes('-fullscreen', False))

        except ValueError:
            print("تأكد من أن الإحداثيات أرقام صحيحة")

    search_btn = Button(input_frame, text="بحث", command=search_location)
    search_btn.pack(side=LEFT, padx=10)
