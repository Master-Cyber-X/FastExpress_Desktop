import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkintermapview import TkinterMapView


class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("البحث عن موقع عبر الإحداثيات")
        self.root.geometry("900x600")

        # ========== الأعلى ==========
        input_frame = tb.Frame(root, padding=10)
        input_frame.pack(fill=X)

        tb.Label(input_frame, text="Latitude:").pack(side=LEFT, padx=5)
        self.lat_entry = tb.Entry(input_frame, width=10)
        self.lat_entry.pack(side=LEFT)

        tb.Label(input_frame, text="Longitude:").pack(side=LEFT, padx=5)
        self.lon_entry = tb.Entry(input_frame, width=10)
        self.lon_entry.pack(side=LEFT)

        search_btn = tb.Button(input_frame, text="بحث", bootstyle=PRIMARY, command=self.search_location)
        search_btn.pack(side=LEFT, padx=10)

        # ========== الخريطة ==========
        self.map_widget = TkinterMapView(root, width=800, height=500, corner_radius=10)
        self.map_widget.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # إعداد مبدئي
        self.map_widget.set_position(24.7136, 46.6753)  # الرياض كموقع افتراضي
        self.map_widget.set_zoom(5)

    def search_location(self):
        try:
            lat = float(self.lat_entry.get())
            lon = float(self.lon_entry.get())

            # تحريك الخريطة
            self.map_widget.set_position(lat, lon)
            self.map_widget.set_zoom(10)

            # إضافة Marker
            self.map_widget.set_marker(lat, lon, text=f"({lat}, {lon})")

        except ValueError:
            print("❌ تأكد من أن الإحداثيات أرقام صحيحة")

if __name__ == "__main__":
    app = tb.Window(themename="darkly")  # يمكنك تغيير الثيم
    MapApp(app)
    app.mainloop()
