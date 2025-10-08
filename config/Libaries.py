# GUi Libraries.
from tkinter import *
import tkinter as tk
import ttkbootstrap as tb
import ttkbootstrap
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap import *
from tkinter import scrolledtext as scrtext
from tkinter import filedialog,messagebox
from tkinter import ttk

# Environment System.
import babel.numbers,webbrowser,random
import os , time,threading,pyautogui,requests
from time import strftime
from geopy.geocoders import Nominatim
from urllib.parse import urlparse, parse_qs
import re
from geopy.geocoders import Nominatim
import re
from urllib.parse import unquote
from geopy.geocoders import Nominatim


# PDF Documentation Generator.
from barcode.writer import ImageWriter
import reportlab,qrcode,barcode
import reportlab.pdfgen.canvas
from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from docxtpl import  DocxTemplate as docx
import pandas as pd
from io import BytesIO

# Documentions Generator
import reportlab
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4,landscape,A5,letter,legal
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import time
import qrcode

# Database Connections sqlite3.
# import sqlite3

# Database Connections Supa.
from supabase import create_client, Client # type: ignore
from Data.Cloud_Supabase.Supa import Supa

# الأتصال بقاعدة البيانات
# from Data.SQILite import SQL_DB



# All libraries in this system installed from pip website