import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime as dt
import cv2
import sqlite3
import threading

import sensor

import RPi_I2C_driver 

# import database
def get_time():
    date_time = f"{dt.datetime.now():%A, %d %B %Y\n%X}"

    if 'Monday' in date_time:
        date_time = date_time.replace("Monday","Senin")
    elif 'Tuesday' in date_time:
        date_time = date_time.replace("Tuesday","Selasa")
    elif 'Wednesday' in date_time:
        date_time = date_time.replace("Wednesday","Rabu")
    elif 'Thursday' in date_time:
        date_time = date_time.replace("Thursday","Kamis")
    elif 'Friday' in date_time:
        date_time = date_time.replace("Friday","Jum\'at")
    elif 'Saturday' in date_time:
        date_time = date_time.replace("Saturday","Sabtu")
    elif 'Sunday' in date_time:
        date_time = date_time.replace("Sunday","Minggu")

    if 'January' in date_time:
        date_time = date_time.replace("January", "Januari")
    elif 'February' in date_time:
        date_time = date_time.replace("February", "February")
    elif 'March' in date_time:
        date_time = date_time.replace("March", "March")
    elif 'April' in date_time:
        date_time = date_time.replace("April", "April")
    elif 'May' in date_time:
        date_time = date_time.replace("May", "Mei")
    elif 'June' in date_time:
        date_time = date_time.replace("Juni", "Juni")
    elif 'July' in date_time:
        date_time = date_time.replace("July", "Juli")
    elif 'August' in date_time:
        date_time = date_time.replace("August", "Agustus")
    elif 'September' in date_time:
        date_time = date_time.replace("September", "September")
    elif 'October' in date_time:
        date_time = date_time.replace("October", "Oktober")
    elif 'November' in date_time:
        date_time = date_time.replace("November", "November")
    elif 'December' in date_time:
        date_time = date_time.replace("December", "Desember")
    return date_time

def get_date():

    date_time = f"{dt.datetime.now():%A, %d %B %Y, %X}"

    if 'Monday' in date_time:
        date_time = date_time.replace("Monday","Senin")
    elif 'Tuesday' in date_time:
        date_time = date_time.replace("Tuesday","Selasa")
    elif 'Wednesday' in date_time:
        date_time = date_time.replace("Wednesday","Rabu")
    elif 'Thursday' in date_time:
        date_time = date_time.replace("Thursday","Kamis")
    elif 'Friday' in date_time:
        date_time = date_time.replace("Friday","Jum\'at")
    elif 'Saturday' in date_time:
        date_time = date_time.replace("Saturday","Sabtu")
    elif 'Sunday' in date_time:
        date_time = date_time.replace("Sunday","Minggu")

    if 'January' in date_time:
        date_time = date_time.replace("January", "Januari")
    elif 'February' in date_time:
        date_time = date_time.replace("February", "February")
    elif 'March' in date_time:
        date_time = date_time.replace("March", "March")
    elif 'April' in date_time:
        date_time = date_time.replace("April", "April")
    elif 'May' in date_time:
        date_time = date_time.replace("May", "Mei")
    elif 'June' in date_time:
        date_time = date_time.replace("Juni", "Juni")
    elif 'July' in date_time:
        date_time = date_time.replace("July", "Juli")
    elif 'August' in date_time:
        date_time = date_time.replace("August", "Agustus")
    elif 'September' in date_time:
        date_time = date_time.replace("September", "September")
    elif 'October' in date_time:
        date_time = date_time.replace("October", "Oktober")
    elif 'November' in date_time:
        date_time = date_time.replace("November", "November")
    elif 'December' in date_time:
        date_time = date_time.replace("December", "Desember")
    return date_time

# t1 = threading.Thread(target=sensor.led_blue, args(1, 3))
# t1.start()

timer = 0
timer_sensor = 0
arr = []
suhu = 0.0
detect = False

lcd = RPi_I2C_driver.lcd()

lcd.lcd_clear()
lcd.backlight(1)

window = tk.Tk()

width = 1920
height = 1080

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width / 2 - width / 2)
center_y = int(screen_height / 2 - height / 2)

sensor.welcome_screen()

window.title("TKinter GUI")
window.geometry(f'{width}x{height}+{center_x}+{center_y}')
window.resizable(False, False)
window.attributes('-topmost', 1)
window.attributes('-fullscreen', 1)
window.configure(bg='#fff500')



mainframe = ttk.Frame(window)
mainframe.grid(column=0, row=0, sticky=('N', 'NW', 'NE', 'S'))
window.columnconfigure(1, weight=2)
window.rowconfigure(3, weight=2)


logo1 = tk.PhotoImage(file='logoulm.png')
pp = tk.PhotoImage(file='pfp.png')

label1 = tk.Label(window)
label1['text'] = 'TKinter GUI'
label1['font'] = "Ubuntu Condensed", 35
label1['image'] = logo1
label1['compound'] = 'none'
label1['bg'] = "red"
label1['fg'] = "white"
label1.grid(column=0, row=0, sticky=('N, S, E, W'))

label2 = tk.Label(window)
label2['text'] = 'Selamat Datang di \nUniversitas Lambung Mangkurat'
label2['font'] = "Source Sans Pro", 35
label2['compound'] = 'none'
label2['bg'] = "red"
label2['fg'] = "white"
label2.grid(column=1, row=0, sticky=('N, S, E, W'))

label3 = tk.Label(window)
label3['text'] = 'TKinter GUI'
label3['font'] = "Ubuntu Condensed", 35
label3['image'] = logo1
label3['compound'] = 'none'
label3['bg'] = "red"
label3['fg'] = "white"
label3['width'] = 200
label3.grid(column=2, row=0, sticky=('N, S, E, W'), ipadx= 40)

emptyLabel = tk.Label(window)
emptyLabel['bg'] = '#fff500'
emptyLabel.grid(column=0, row=1, columnspan=3, ipady=90, sticky=('N, S, E, W'))

pfp = tk.Label(window)
pfp['image'] = pp
pfp['width'] = 280
pfp['bg'] = '#fff500'
pfp.grid(column=0, rows=2, sticky=('NE'), columnspan=1)

frame = tk.Frame(window)
frame.grid(column=1, row=2, columnspan=2)

labelInfoNama = tk.Label(frame)
labelInfoNama['text'] = 'Nama'
labelInfoNama['font'] = "Ubuntu Condensed", 35
labelInfoNama['bg'] = '#fff500'
labelInfoNama['anchor'] = 'w'
labelInfoNama['justify'] = 'left'
labelInfoNama.grid(column=0, row=1, sticky=('N, S, E, W'))

labelInfoJabatan = tk.Label(frame)
labelInfoJabatan['text'] = 'Jabatan'
labelInfoJabatan['font'] = "Ubuntu Condensed", 35
labelInfoJabatan['bg'] = '#fff500'
labelInfoJabatan['anchor'] = 'w'
labelInfoJabatan['justify'] = 'left'
labelInfoJabatan.grid(column=0, row=2, sticky=('N, S, E, W'))

labelInfoSuhu = tk.Label(frame)
labelInfoSuhu['text'] = 'Suhu Tubuh'
labelInfoSuhu['font'] = "Ubuntu Condensed", 35
labelInfoSuhu['bg'] = '#fff500'
labelInfoSuhu['anchor'] = 'w'
labelInfoSuhu['justify'] = 'left'
labelInfoSuhu.grid(column=0, row=3, sticky=('N, S, E, W'))

labelInfoTime = tk.Label(frame)
labelInfoTime['text'] = 'Tanggal Absensi'
labelInfoTime['font'] = "Ubuntu Condensed", 35
labelInfoTime['bg'] = '#fff500'
labelInfoTime['anchor'] = 'w'
labelInfoTime['justify'] = 'left'
labelInfoTime.grid(column=0, row=4, sticky=('N, S, E, W'))

labelNamaSep = tk.Label(frame)
labelNamaSep['text'] = ' : '
labelNamaSep['font'] = "Ubuntu Condensed", 35
labelNamaSep['bg'] = '#fff500'
labelNamaSep.grid(column=1, row=1, ipadx = 20)

labelJabatanSep = tk.Label(frame)
labelJabatanSep['text'] = ' : '
labelJabatanSep['font'] = "Ubuntu Condensed", 35
labelJabatanSep['bg'] = '#fff500'
labelJabatanSep.grid(column=1, row=2, ipadx = 20)

labelSuhuSep = tk.Label(frame)
labelSuhuSep['text'] = ' : '
labelSuhuSep['font'] = "Ubuntu Condensed", 35
labelSuhuSep['bg'] = '#fff500'
labelSuhuSep.grid(column=1, row=3, ipadx = 20)

labelTimeSep = tk.Label(frame)
labelTimeSep['text'] = ' : '
labelTimeSep['font'] = "Ubuntu Condensed", 35
labelTimeSep['bg'] = '#fff500'
labelTimeSep.grid(column=1, row=4, ipadx = 20)

labelNama = tk.Label(frame)
labelNama['text'] = ''
labelNama['font'] = "Ubuntu Condensed", 35
labelNama['bg'] = '#fff500'
labelNama['anchor'] = 'w'
labelNama['width'] = 500
labelNama['justify'] = 'left'
labelNama.grid(column=2, row=1)

labelJabatan = tk.Label(frame)
labelJabatan['text'] = ''
labelJabatan['font'] = "Ubuntu Condensed", 35
labelJabatan['bg'] = '#fff500'
labelJabatan['anchor'] = 'w'
labelJabatan['width'] = 500
labelJabatan['justify'] = 'left'
labelJabatan.grid(column=2, row=2)

labelSuhu = tk.Label(frame)
labelSuhu['text'] = ''
labelSuhu['font'] = "Ubuntu Condensed", 35
labelSuhu['bg'] = '#fff500'
labelSuhu['anchor'] = 'w'
labelSuhu['width'] = 500
labelSuhu['justify'] = 'left'
labelSuhu.grid(column=2, row=3)

labelTime = tk.Label(frame)
labelTime['text'] = ''
labelTime['font'] = "Ubuntu Condensed", 35
labelTime['bg'] = '#fff500'
labelTime['anchor'] = 'w'
labelTime['width'] = 500
labelTime['justify'] = 'left'
labelTime.grid(column=2, row=4)

frameDate = tk.Frame(window)
frameDate['height'] = 35
frameDate['width'] = 400
frameDate.place(x = screen_width - 660, y = screen_height - 280)

frameInfoAbsensi = tk.Frame(window)
frameInfoAbsensi['height'] = 50
frameInfoAbsensi['width'] = 400
frameInfoAbsensi['background'] = "#fff500"
frameInfoAbsensi.place(x = screen_width - 1500, y = screen_height - 280)

labelInfoAbsensi = ttk.Label(frameInfoAbsensi)
labelInfoAbsensi['text'] = ""
labelInfoAbsensi['justify'] = "center"
labelInfoAbsensi['font'] = "Source Sans Pro", 30
labelInfoAbsensi['background'] = "#fff500"
labelInfoAbsensi.pack()


labelDate = ttk.Label(frameDate)
labelDate['text'] = get_time()
labelDate['justify'] = "center"
labelDate['font'] = "Source Sans Pro", 30
labelDate['width'] = 28
labelDate['anchor'] = "center"
labelDate['background'] = "#fff500"
labelDate.pack()

# labelDate.grid(column=2, row = 3, columnspan = 2, ipady = 50, ipadx = 10)

labelRunningText = tk.Label(window)
labelRunningText['text'] = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin eget ligula at libero luctus bibendum. Morbi sed ultrices ante.'
labelRunningText['font'] = "Source Sans Pro", 20
labelRunningText['bg'] = "black"
labelRunningText['fg'] = "white"
labelRunningText['justify'] = 'left'
labelRunningText['anchor'] = 'w'
labelRunningText.grid(column=0, row=4, columnspan=3, ipady=10, sticky=('N, S, E, W'))

cap = cv2.VideoCapture(0)
fname = "model/trainingData.yml"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(fname)
conn = sqlite3.connect('usersdatabase.db')
c = conn.cursor()


labelFaceCap = tk.Label(window)


def absen_hari_ini(now, convert_time):
    if now.year == convert_time.year and now.month == convert_time.month and now.day == convert_time.day:
        return True
    else:
        return False

def sensor_run():
    global arr
    global timer_sensor
    if timer_sensor is 1:
        sensor.get_close()
        timer_sensor += 1
    if len(arr) <= 4 and timer_sensor is 2:
        jarak = round(sensor.distance(), 2)
        if jarak < 10.0:
            arr.append(jarak)
    else:
        if timer_sensor is 2:
            global jarak_mean
            global suhu
            global detect
            suhu = "%.2f"%(sensor.temp()+4.5)
            detect = True
            print("1 "+ str(suhu))
            lcd.lcd_display_string("    "+str(suhu)+" C",2)
            jarak_mean = sum(arr) / len(arr)
            labelSuhu.configure(text=suhu)
        elif timer_sensor >= 100:
            arr = []
            timer_sensor = 0
            pass
        timer_sensor += 1


def show_frames():
    global detect
    global suhu
    cv2image=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        ids,conf = recognizer.predict(gray[y:y+h, x:x+w])
        cv2.rectangle(cv2image, (x,y), (x+w, y+h), (0,255,0), 2)
        c.execute("select * from users where id = (?);", (ids,))
        result = c.fetchall()
        users_id = result[0][0]
        name = result[0][1]
        u_jabatan = result[0][2]
        if conf < 50:
            temp = sensor.temp()+3.5
            cv2.putText(cv2image, name, (x+2, y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0), 2)
            labelNama.configure(text=name)
            labelJabatan.configure(text=u_jabatan)
            if detect == True:
                lcd.lcd_display_string(name[:16], 1)
                c.execute("SELECT date from absensi where users_id = (?) order by id desc;", (users_id,))
                result = c.fetchone()
                #if result is None:
                c.execute("INSERT INTO absensi (date, temp, users_id) values (?,?,?)",(dt.datetime.now(), suhu, users_id))
                print("2 "+ str(suhu))
                conn.commit()
                detect = False
                # else:
                    # format_time = "%Y-%m-%d %H:%M:%S.%f"
                    # convert_time = dt.datetime.strptime(result[0], format_time)
                    # if absen_hari_ini(dt.datetime.now(), convert_time) is False or (absen_hari_ini(dt.datetime.now(), convert_time) is True and convert_time.hour >= 8):
                        # c.execute("INSERT INTO absensi (date, temp, users_id) values (?,?,?)",(dt.datetime.now(), suhu, users_id))
                        # print("2 "+ str(suhu))
                        # conn.commit()
                        # detect = False
                    # else:
                        # if dt.datetime.now().hour >= 7 and dt.datetime.now().hour <= 12:
                            # labelInfoAbsensi["text"] = "Anda sudah absen pagi"
                            # detect = False
                        # elif dt.datetime.now().hour >= 16 and dt.datetime.now().hour < 18:
                            # labelInfoAbsensi["text"] = "Anda sudah absen sore"
                            # detect = False
                        # else:
                            # labelInfoAbsensi["text"] = "Anda sudah absen hari ini"
                            # detect = False
                
                        
            if not labelTime.cget("text"):
                labelTime.configure(text=get_date())
            global timer
            timer=0
        else:
            cv2.putText(cv2image, 'No Match', (x+2, y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
            if not labelTime.cget("text"):
                labelTime.configure(text=get_date())
    
    timer = timer + 1
    if timer >= 100:
        labelNama.configure(text='')
        labelJabatan.configure(text='')
        labelTime.configure(text='')
        labelSuhu.configure(text='')
        labelInfoAbsensi.configure(text='')
        detect = True

    imag = Image.fromarray(cv2image)

    imgtk = ImageTk.PhotoImage(image = imag)
    labelFaceCap.imgtk = imgtk
    labelFaceCap.configure(image = imgtk)


labelFaceCap['width'] = 500
labelFaceCap['height'] = 480
labelFaceCap.place(x = screen_width - 660, y = screen_height - 800)


def update():
    labelDate.config(text= get_time())
    window.after(1, sensor_run)
    window.after(1, show_frames)
    window.after(1, update)


update()
show_frames()
sensor_run()

window.mainloop()

conn.close()
sensor.GPIO.cleanup()
lcd.lcd_clear()
lcd.backlight(0)

