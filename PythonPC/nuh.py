import tkinter as tk
import random
import time

def create_window():
    while True:
        # Rastgele bir pencere oluştur
        window = tk.Tk()
        window.title("Hihihi!")
        
        # Pencerenin boyutunu ve yerini rastgele ayarla
        width = random.randint(200, 400)
        height = random.randint(100, 300)
        x = random.randint(0, 1000)
        y = random.randint(0, 600)
        window.geometry(f"{width}x{height}+{x}+{y}")
        
        # Mesaj ekle
        label = tk.Label(window, text="SÜRPRİZ! Kapatamazsın :P", font=("Arial", 14))
        label.pack(pady=20)
        
        # Pencereyi kapatmayı zorlaştır (ama tamamen imkansız değil)
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Kapat tuşunu devre dışı bırakır
        
        window.update()
        time.sleep(0.5)  # Yeni pencere açmadan önce kısa bir bekleme

# Programı başlat
create_window()