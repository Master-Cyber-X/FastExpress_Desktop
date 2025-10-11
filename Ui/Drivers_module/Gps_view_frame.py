from config.Libaries import *
from config.sys_classes import *



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
    mapView = TkinterMapView(master, width=800, height=650, corner_radius=10)
    mapView.pack(fill=BOTH, expand=True, padx=10, pady=10)
    mapView.set_tile_server("https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}")

    # إعداد مبدئي (الرياض)
    mapView.set_position(24.7136, 46.6753)
    mapView.set_zoom(5)
    

    # تحميل أيقونة السيارة
    car_icon = PhotoImage(file=r"Assets\Img\pgs-person.png")

    def animate_zoom(target_zoom, step=0.5, delay=50):
        """تحريك تكبير الخريطة تدريجيًا"""
        current_zoom = mapView.zoom
        if abs(current_zoom - target_zoom) < 0.1:
            mapView.set_zoom(target_zoom)
            return
        new_zoom = current_zoom + step if current_zoom < target_zoom else current_zoom - step
        mapView.set_zoom(new_zoom)
        master.after(delay, lambda: animate_zoom(target_zoom, step, delay))

    def search_location():
        mapView.delete_all_marker()
        try:
            lat = float(lat_entry.get())
            lon = float(lon_entry.get())

            # تحريك الخريطة
            mapView.set_position(lat, lon)

            # 🔥 تكبير تدريجي (أنميشن)
            animate_zoom(15, step=0.3, delay=40)

            # إضافة Marker مع أيقونة السيارة
            mapView.set_marker(
                lat, lon,
                text=f"R- {random.randint(1,100)} المندوب ",
                icon=car_icon
            )

            # تكبير النافذة
            master.state('zoomed')

        except ValueError:
            print("⚠️ تأكد من أن الإحداثيات أرقام صحيحة")
    
    def change_map_graphicals_type(*args):
        mapView.set_tile_server(google_map_graphicals_list[va.get()])
        
        
    va = StringVar()

    ch = Combobox(input_frame, cursor='hand2', values=[i for i in google_map_graphicals_list.keys()], textvariable=va)
    ch.pack(side='right')
    va.trace_add('write', callback=change_map_graphicals_type)
    
    search_btn = Button(input_frame, text="بحث", command=search_location)
    search_btn.pack(side=LEFT, padx=10)
