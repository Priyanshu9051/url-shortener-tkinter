from tkinter import *
import pyshorteners as py


def shorten():
    shortener = py.Shortener()
    short_url = shortener.tinyurl.short(url_entry.get())
    print(shorturl_entry.insert(0, short_url))


root = Tk()
root.title("URL Converter")
root.geometry("200x200")
frame = Frame()
url_label = Label(frame, text="enter the long URL")
url_entry = Entry(frame)
shorturl_label = Label(frame, text="Output short URL")
shorturl_entry = Entry(frame)
button = Button(frame, text="convert", command=shorten)

url_label.grid(row=0, column=0, columnspan=2)
url_entry.grid(row=1, column=0, columnspan=2)
shorturl_label.grid(row=3, column=0, columnspan=2)
shorturl_entry.grid(row=4, column=0, columnspan=2)
button.grid(row=5, column=0, columnspan=2)
frame.pack()
mainloop()
