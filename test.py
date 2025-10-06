from config.sys_classes import sys_class
from config.Libaries import *
import matplotlib.pyplot as pt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# a = Window(themename='cyborg')
# a.geometry('650x650')
# a.title('Map')


# def test():
#     d = sys_class.extract_street_or_pluscode(e.get())
#     l.configure(text=d)

# e = Entry(a, )
# e.pack()

# l = Label()
# l.pack()

# b = Button(a, text='GO', cursor='hand2', command=test)
# b.pack()

# a.mainloop()

from tkinter import *
from ttkbootstrap import Window
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# إنشاء النافذة
a = Window(themename='cyborg')
a.geometry('800x600')
a.title('Map')

canvas_widget = None
fig = None
plot1 = None

# دالة لإنشاء أو تحديث مخطط الأعمدة
def draw_chart():
    global canvas_widget, fig, plot1

    # البيانات
    x = ['A', 'B', 'C', 'D']
    try:
        y = [101, 211, 30, int(e.get())]  # القيمة من الإدخال
    except:
        y = [101, 21, 30, 20]  # قيمة افتراضية في حال الإدخال غير صالح

    # حذف الرسم السابق
    if canvas_widget is not None:
        canvas_widget.get_tk_widget().destroy()

    # إنشاء الشكل بخلفية سوداء
    fig = Figure(figsize=(5, 6), dpi=100, facecolor='black')
    plot1 = fig.add_subplot(111, facecolor='black')

    # رسم الأعمدة
    colors = ['cyan', 'magenta', 'yellow', 'lime']
    plot1.bar(x, y, color=colors, width=0.6, edgecolor='white')

    # تزيين الرسم
    plot1.set_title('Sales Data (Bar Chart)', color='white', fontsize=14)
    plot1.set_xlabel('Category', color='white')
    plot1.set_ylabel('Value', color='white')
    plot1.tick_params(colors='white')
    for spine in plot1.spines.values():
        spine.set_color('white')

    # عرض القيم فوق الأعمدة
    for i, v in enumerate(y):
        plot1.text(i, v + 2, str(v), color='white', ha='center', fontsize=10)

    # ربط الشكل بـ tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)
# دالة لتحديث الحجم تلقائيًا
def on_resize(event):
    if canvas_widget is not None:
        canvas_widget.get_tk_widget().config(width=event.width, height=event.height)
        # draw_chart()






# عناصر الواجهة
top_frame = Frame(a)
top_frame.pack(fill=X, pady=10)

Label(top_frame, text='أدخل رقمًا لتحديث آخر عمود:', font=('Arial', 10)).pack(side=LEFT, padx=5)
e = Entry(top_frame, width=10)
e.pack(side=LEFT, padx=10)

b = Button(top_frame, text='عرض الرسم', cursor='hand2', command=draw_chart)
b.pack(side=LEFT, padx=10)

# إطار الرسم
frame = Frame(a)
frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# تحديث الرسم عند تغيير الحجم
a.bind("<Configure>", on_resize)

# تشغيل التطبيق
a.mainloop()

