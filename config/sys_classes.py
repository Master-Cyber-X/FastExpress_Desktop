# from Data.SQILite import SQL_DB
from config.Libaries import *


sys_icon = 'Assets\\Img\\Company_Logo.ico'
sys_icon_home = 'Assets\\Img\\Courier Software.jpeg'

entries_font  = ('Times',11,'bold')
    

    
    # img = Image.open('Assets\\Img\\Courier Software.jpeg').resize((1610,980))
    # # img = Image.open('Module\\sys_Image\\good-morning-morning-flowers.gif')
    # home_img_logo = ImageTk.PhotoImage(img)

    # img_lable = Label(page,
    #                 compound='center',image=home_img_logo)
    # img_lable.pack(fill='both', expand=True)


class sys_class:
    
    def generator_invoice_as_pdf_size_width_57mm(id,option):
        'PDF :إنشاء فانورة'
        try:
            os.remove('Module\\output.pdf')
        except:
            pass
        # جلب بيانات الفاتورة من قاعدة البيانات
        data = SQL_DB.fetch_all_recorder_detials(id=id)


        qr_img = sys_class.generater_qrcode_png(data, file_name='all_data.png') # جلب كل بيانات الفاتورة ووضعها في كو ار كود.
        qr_id = sys_class.generater_barcode_png(str(data[0][0]), file_name='id_serial.png') # صناعة باركود اي دي الفاتورة
        
        
        pdfmetrics.registerFont(TTFont('Arabic','Module\\Template\\Fonts\\Arabic_8.ttf'))
        def ar(text):
            return get_display(reshape(text))

        my_file = 'Module\\output.pdf'
        
        if option == "EXPORT":
            my_file = filedialog.asksaveasfilename(initialdir='', initialfile=f'{data[0][0]}', filetypes=[('PDF FILES','*.pdf')], defaultextension='pdf')
            if my_file == '':
                return
        

        PAGE_WIDTH = mm
        
        c = Canvas(filename=my_file,pagesize=A4)
        
        c.drawImage(image='Module\\sys_Image\\Company_Logo.jpg', x=170, y=740, width=50, height=50)
        c.setFont('Arabic', 17,)

        c.drawString(text=ar('SARIA EXPRESS'), x=220, y=775)
        c.drawString(text=ar('سريع إكسبريس'), x=230, y=755)
        
        c.setFont('Arabic', 17)

        c.drawString(text=ar('تفاصيل الطلب'), x=230, y=700)
        c.drawImage(image=f'{qr_img}', width=150, height=150 , x=195, y=540)
        
        c.drawString(text='-'*28, x=175, y=530)
        
        c.setFont('Arabic', 14)
        c.drawString(text=ar('رقم الفاتورة :'), x=300, y=500)
        c.drawString(text=ar(f'{data[0][0]}'), x=180, y=500)
        
        c.drawString(text=ar('حالة الطلب :'), x=310, y=480)
        
        c.drawString(text=ar(f'{data[0][2]}'), x=180, y=480)
        
        c.drawString(text=ar('تاريخ الأدخال :'), x=308, y=460)
        c.drawString(text=f"{data[0][10]}", x=180, y=460)
        
        c.drawString(text=ar('وقت الأدخال :'), x=308, y=440)
        c.drawString(text=f"{data[0][11]}", x=180, y=440)
        
        c.setFont('Arabic', 17)
        c.drawString(text='-'*28, x=175, y=420)
        c.setFont('Arabic', 14)
        
        c.drawString(text=ar('أسم العميل :'), x=308, y=400)
        c.drawString(text=ar(f"{data[0][5]}"), x=180, y=400)
        
        c.drawString(text=ar('رقم الجوال :'), x=308, y=380)
        c.drawString(text=ar(f'{f"{data[0][6]}"}'), x=180, y=380)
        
        c.drawString(text=ar('أسم المندوب :'), x=300, y=360)
        c.drawString(text=ar(f"{data[0][8]}"), x=210, y=360)
        
        c.setFont('Arabic', 17)
        c.drawString(text=ar('تفاصيل الشحنة'), x=230, y=330)
        c.setFont('Arabic', 14)
        
        c.setFont('Arabic', 17)
        c.drawString(text='-'*28, x=175, y=300)
        c.setFont('Arabic', 14)
        
        c.drawString(text=ar('م#.   \t    السعر    \t  أسم المنتج'), x=190, y=280)
        count = 260
        
        sums = 0
        for x in range(1,4):
            c.setFont('Arabic', 13)
            count-=20
            sums += 83
            c.drawString(text=ar(f'{x}:منتج-'), x=190, y=count)
            c.drawString(text=f"{count}", x=290, y=count)
            c.drawString(text=f"{x}", x= 370, y=count)
        count = count
        
        c.setFont('Arabic', 17)
        c.drawString(text='-'*28, x=180, y=count-20)
        c.setFont('Arabic', 14)
        
        c.drawString(text=ar('الإجمالي:'), x=340, y=count-40)
        c.drawString(text=f"{data[0][7]}", x=210, y=count-40)
        
        # Barcode in last invoice.
        c.drawImage(image=f'{qr_id}', width=259, height=60 , x=150, y=count-140)

        c.drawString(text=ar('تاريخ الطباعة :'), x=325, y=count-160)
        c.drawString(text=f"{time.strftime('%Y-%m-%d %p %I:%M:%C')}", x=180, y=count-160)
        c.drawString(text="", x=180, y=count-160)

        
        c.save()

                
        def clear_cashe():
            try:
                time.sleep(2)
                os.remove(r'Module\all_data.png')
                # os.remove(r'Module\qrcode_viewer.png')
                os.remove(r'Module\id_serial.png.png')
            except Exception as e:
                print(f'{e}')


        if my_file !='Module\\output.pdf':
            asked = messagebox.askyesnocancel('ملاحضة', 'تم الحفظ هل تود فتح الملف؟')
            if asked != False:
                clear_cashe()
                webbrowser.open(url=f'{my_file}', new=1)

        if option== 'PRINT':
            try:
                os.startfile(my_file, 'print')
                time.sleep(2)
                clear_cashe()
            except Exception as e:
                if 'No application is associated with the specified file for this operation' in str(e):
                    messagebox.showerror('ملاحضة', f'Please install Adobe and set it as your default browser for print \n Full Error :{str(e)[:87]}.')
                return
            try:
                os.remove('Module\\output.pdf')
            except Exception as e:
                print(f'{e}')


    def build_folder_and_file():
        pass
        # Working in one case the user delete system folder or file.

        # Create a folder that name "Data"
        # if os.path.exists('Module') == False:
        #     os.mkdir('Module')
            
        # # Create database file if not exists.
        # if os.path.exists('Module\\DataBase\\data.db') == False:
        #     with open(os.path.join('Module\\DataBase', 'data.db'), 'w') as file:
        #         pass


    def generater_barcode_png(data,path_saved='Module\\',file_name='barcode_viewer'):
        # Define the barcode data (e.g., EAN-13 requires 12 digits + 1 check digit)
        data = data
        options = {
        'transparent': True,  # Set background to transparent
        'write_text': False,  # Hide the human-readable text (digits)
        'module_width': 0.2,  # Adjust barcode bar width if needed
        'module_height': 15.0, # Adjust barcode bar height if needed
        'quiet_zone': 0, # Set barcode border
        }
        # Get the Code128 barcode object, specifying ImageWriter for image output
        ean = barcode.Code128(data, writer=ImageWriter())
        # Save the barcode as a PNG image
        saved = ean.save(f'{path_saved}{file_name}', options=options)
        return f'{saved}'.replace('\\','\\\\')


    def generater_qrcode_png(data,path_saved='Module\\',file_name='qrcode_viewer.png'):
        
        qr = qrcode.make(data, border=0)
        
        qr.save(f'{path_saved}{file_name}')
        
        return f"{path_saved}\\{file_name}"


    def centering_window(window):
        'سوف تقوم هاذه الداله بجعل النافذ في النتصف'
        window.update_idletasks()
        width  = window.winfo_width()
        height = window.winfo_height()
        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        x = (screenwidth - width) //2
        y = (screenheight - height) //2
        window.geometry(f'{width}x{height}+{x}+{y}')

    def enable_copy_paste(widget):
        print('Vaild')
        'بسمح لخاصة النسخ واللصق في حالة ان اللغة غير إنجليزي'
        # اختصارات النسخ
        widget.bind("<Control-c>", lambda e: widget.event_generate("<<Copy>>"))
        widget.bind("<Control-C>", lambda e: widget.event_generate("<<Copy>>"))
        
        # اختصارات القص
        widget.bind("<Control-x>", lambda e: widget.event_generate("<<Cut>>"))
        widget.bind("<Control-X>", lambda e: widget.event_generate("<<Cut>>"))
        
        # اختصارات اللصق
        widget.bind("<Control-v>", lambda e: widget.event_generate("<<Paste>>"))
        widget.bind("<Control-V>", lambda e: widget.event_generate("<<Paste>>"))


    # def extract_street_from_link(link):
    #     # 1) استخراج الإحداثيات من رابط خرائط Google
    #     parsed = urlparse(link)
    #     if "/maps/place/" in link and "@".encode() in link.encode():
    #         # نمط جديد من الروابط
    #         coords = link.split('@')[1].split(',')[:2]
    #         lat, lon = coords
    #     else:
    #         # النمط اللي فيه query parameter q=
    #         query = parse_qs(parsed.query)
    #         if "q" in query:
    #             coords = query["q"][0].split(',')
    #             lat, lon = coords[0], coords[1]
    #         else:
    #             return "لم أتمكن من استخراج الإحداثيات من الرابط"
        
    #     # 2) استخدام geopy لاستخراج العنوان
    #     geolocator = Nominatim(user_agent="street_extractor")
    #     location = geolocator.reverse((lat, lon), language="ar")
        
    #     if location and "road" in location.raw["address"]:
    #         return location.raw["address"]["road"]
    #     return location.address  # يرجع العنوان كامل إذا الشارع غير محدد

    # # مثال على الاستخدام
    # link = "https://www.google.com/maps/place/24.7136,46.6753"
    # street_name = extract_street_from_link(link)
    # print(" اسم الشارع:", street_name)
    

    # def extract_coordinates(link: str):
    #     """
    #     يحاول استخراج (lat, lon) من رابط Google Maps بأنماط مختلفة
    #     """
    #     # نمط: .../@24.7136,46.6753,...
    #     match = re.search(r'@([-0-9.]+),([-0-9.]+)', link)
    #     if match:
    #         return match.group(1), match.group(2)
        
    #     # نمط: ...q=24.7136,46.6753
    #     match = re.search(r'q=([-0-9.]+),([-0-9.]+)', link)
    #     if match:
    #         return match.group(1), match.group(2)

    #     # نمط: .../place/24.7136,46.6753
    #     match = re.search(r'/([-0-9.]+),([-0-9.]+)', link)
    #     if match:
    #         return match.group(1), match.group(2)

    #     return None, None

    # def extract_coordinates(link: str):
    #     """
    #     يحاول استخراج (lat, lon) من رابط Google Maps بأنماط مختلفة
    #     """
    #     # نمط: .../@24.7136,46.6753,...
    #     match = re.search(r'@([-0-9.]+),([-0-9.]+)', link)
    #     if match:
    #         return match.group(1), match.group(2)
        
    #     # نمط: ...q=24.7136,46.6753
    #     match = re.search(r'q=([-0-9.]+),([-0-9.]+)', link)
    #     if match:
    #         return match.group(1), match.group(2)

    #     # نمط: .../place/24.7136,46.6753
    #     match = re.search(r'/([-0-9.]+),([-0-9.]+)', link)
    #     if match:
    #         return match.group(1), match.group(2)

    #     return None, None


    # def extract_street_from_link(link: str):
    #     lat, lon = extract_coordinates(link)
    #     if not lat or not lon:
    #         return " لم أستطع استخراج الإحداثيات من الرابط"

    #     geolocator = Nominatim(user_agent="street_extractor")
    #     location = geolocator.reverse((lat, lon), language="ar")

    #     if location and "road" in location.raw["address"]:
    #         return location.raw["address"]["road"]
    #     return location.address if location else " لم أجد العنوان"


    def extract_street_or_pluscode(link: str):
        """
        يستخرج (اسم الشارع) من رابط Google Maps
        """
        link = unquote(link)  # فك أي ترميز %20 إلخ
        geolocator = Nominatim(user_agent="maps_extractor")

        lat, lon, plus_code = None, None, None

        # 1) أنماط الإحداثيات
        match = re.search(r'@([-0-9.]+),([-0-9.]+)', link)
        if match:
            lat, lon = match.group(1), match.group(2)
        
        if not lat:
            match = re.search(r'q=([-0-9.]+),([-0-9.]+)', link)
            if match:
                lat, lon = match.group(1), match.group(2)

        if not lat:
            match = re.search(r'/([-0-9.]+),([-0-9.]+)', link)
            if match:
                lat, lon = match.group(1), match.group(2)

        # 2) Plus Code
        if not lat:
            match = re.search(r'/maps/place/([^/]+)', link)
            if match and "+" in match.group(1):
                plus_code = match.group(1)
                loc = geolocator.geocode(plus_code)
                if loc:
                    lat, lon = loc.latitude, loc.longitude

        # 3) إذا ما فيه لا إحداثيات ولا Plus Code
        if not lat or not lon:
            return " لم أستطع استخراج إحداثيات أو Plus Code من الرابط"

        # 4) Reverse Geocoding
        location = geolocator.reverse((lat, lon), language="ar")
        street = None
        if location and "road" in location.raw["address"]:
            street = location.raw["address"]["road"]
        elif location:
            street = location.address
            
        if plus_code:
            return f"{street}"
        else:
            return f"{street}"