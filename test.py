from config.Libaries import *
from config.sys_classes import *


root = Window(themename='cyborg')
root.title('MapView')
root.geometry('1400x800+200+20')


# تحميل أيقونة السيارة
car_icon = PhotoImage(file=r"Assets\Img\pgs-person.png")

f = LabelFrame(root, text='Tools')
f.pack(fill='both')

def search_location_lat_lon():
    
    mapView.delete_all_marker()
    
    Lat = float(e0.get())
    Lon = float(e1.get())
    
    mapView.set_position(Lat,Lon)
    
    mapView.set_marker(
                        Lat, Lon,
                text=f"R- {random.randint(1,100)} المندوب ",
                icon=car_icon
    )


def slide_zoom(e):
    mapView.set_zoom(sc.get())
    print(sc.get())

def search_location():
    mapView.set_address(e2.get())


def change_map_graphicals_type(*args):
    mapView.set_tile_server(google_map_graphicals_list[va.get()])
    
    
va = StringVar()

ch = Combobox(f, cursor='hand2', values=[i for i in google_map_graphicals_list.keys()], textvariable=va)
ch.pack(side='right')
va.trace_add('write', callback=change_map_graphicals_type)

    
l0 = Label(f, text='Latitude').pack(side='left')

e0 = Entry(f, width=22)
e0.pack(padx=3,side='left', pady=4)

l1 = Label(f, text='Longtiude').pack(side='left')

e1 = Entry(f, width=22)
e1.pack(padx=3,side='left', pady=4)

l2 = Label(f, text='Address').pack(side='left')

e2 = Entry(f, width=22)
e2.pack(padx=3,side='left', pady=4)

b = Button(f, text='Search', cursor='hand2', command=search_location_lat_lon)
b.pack(fill='both', padx=2,side='left')

sc = Scale(f, from_=0, to=20, value=30, length=220, cursor='hand2',orient='horizontal', command=slide_zoom)
sc.pack(fill='both', side='left', padx=10)


# Map Viewer
mapView = TkinterMapView(root, width=1000, height=500)
mapView.pack(fill='both', expand=True, pady=14)

# mapView.get_position()

root.mainloop()