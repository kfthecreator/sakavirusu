import tkinter as tk
import random
import time
import winsound  # Windows için ses çalma

# Aktif pencereleri ve yönlerini takip etmek için liste
windows = []

class MovingWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hihihi!")
        
        # Rastgele başlangıç boyutu ve konumu
        width = random.randint(200, 400)
        height = random.randint(100, 300)
        x = random.randint(0, 1000)
        y = random.randint(0, 600)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
        # Mesaj
        label = tk.Label(self.window, text="Beni kapat! :P", font=("Arial", 14))
        label.pack(pady=20)
        
        # Rastgele başlangıç yönü (hız)
        self.dx = random.choice([-15, 15])  # X yönünde hız
        self.dy = random.choice([-15, 15])  # Y yönünde hız
        
        # İlk rastgele renk
        self.change_color()
        
        # Kapatma işlemi
        def on_close():
            self.window.destroy()
            if self in windows:
                windows.remove(self)
            for _ in range(4):
                create_and_move_window()
        
        self.window.protocol("WM_DELETE_WINDOW", on_close)
        windows.append(self)


    def change_color(self):
        bg_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Arka plan rengi
        fg_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Metin rengi
        self.window.configure(bg=bg_color)
        for widget in self.window.winfo_children():  # Label gibi çocuk widget'lar
            widget.configure(bg=bg_color, fg=fg_color)

    def move(self):
        try:
            if not self.window.winfo_exists():
                return
            
            # Mevcut konumu al
            x = self.window.winfo_x()
            y = self.window.winfo_y()
            width = self.window.winfo_width()
            height = self.window.winfo_height()
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            
            # Yeni konumu hesapla
            new_x = x + self.dx
            new_y = y + self.dy
            
            # Kenarlara çarpma kontrolü ve ses
            if new_x <= 0 or new_x + width >= screen_width:
                self.dx = -self.dx  # X yönünü tersine çevir
                new_x = max(0, min(new_x, screen_width - width))
                winsound.Beep(1000, 100)  # 1000 Hz, 100 ms beep sesi
            if new_y <= 0 or new_y + height >= screen_height:
                self.dy = -self.dy  # Y yönünü tersine çevir
                new_y = max(0, min(new_y, screen_height - height))
                winsound.Beep(1000, 100)  # 1000 Hz, 100 ms beep sesi

            
            # Yeni konumu uygula
            self.window.geometry(f"+{int(new_x)}+{int(new_y)}")
            # Her hareket ettiğinde rengi değiştir
            self.change_color()
            self.window.update()
        except tk.TclError:
            # Pencere kapandığında oluşabilecek hataları yakala
            if self in windows:
                windows.remove(self)

def create_and_move_window():
    new_window = MovingWindow()
    new_window.window.update()

def main():
    # İlk pencereyi oluştur
    create_and_move_window()
    
    while True:
        # Tüm pencereleri hareket ettir
        for window in windows[:]:  # Kopya liste ile döngü
            window.move()
        
        time.sleep(0.05)  # Hareket hızını kontrol et

if __name__ == "__main__":
    main()