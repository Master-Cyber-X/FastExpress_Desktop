# import re
# from geopy.geocoders import Nominatim




from config.sys_classes import sys_class
from config.Libaries import *


a = Window(themename='cyborg')
a.geometry('650x650')
a.title('Map')


def test():
    d = sys_class.extract_street_or_pluscode(e.get())
    l.configure(text=d)

e = Entry(a, )
e.pack()

l = Label()
l.pack()

b = Button(a, text='GO', cursor='hand2', command=test)
b.pack()

a.mainloop()