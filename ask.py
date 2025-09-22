import tkinter as tk 
from tkinter import messagebox 
import random 
import webbrowser
import urllib.parse

def pindah_button(button):
    new_x = random.randint(0, window.winfo_width() - button.winfo_width())
    new_y = random.randint(0, window.winfo_height() - button.winfo_height())
    button. place(x=new_x, y=new_y)

def tekan_ya( ):
    messagebox. showinfo("Jawaban", "YAAY, see you there kak faras!")

def tekan_tidak( ):
    pindah_button(no_button)

window = tk.Tk()
window.title("Kak Farasqi's card")
window.geometry("400x600")
window.configure(bg='#FFC0CB')

frame = tk.Frame(window, bg='#FFC0CB', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="Hi, Kak Farass. Before We Go Far, I Want to Say Thank you for your time yesterday.", font=("Helvetica", 16, "bold"), bg='#FFC0CB', fg='#FF69B4', justify=tk.CENTER)
label.pack(pady=20) 

label = tk.Label(frame, text="After our little conversation that day, i thought that we have same interests.", font=("Helvetica", 16, "bold"), bg='#FFC0CB', fg='#FF69B4', justify=tk.CENTER)
label.pack(pady=20)

label = tk.Label(frame, text="So, would you mind if today/tomorrow we get more time to know each other?", font=("Helvetica", 16, "bold"), bg='#FFC0CB', fg='#FF69B4', justify=tk.CENTER)
label.pack(pady=20)

label = tk.Label(frame, text="i'll show and present to you how deserve i am! :D", font=("Helvetica", 16, "bold"), bg='#FFC0CB', fg='#FF69B4', justify=tk.CENTER)
label.pack(pady=20)

yes_button = tk.Button(frame, text="Yes", font=("Helvetica",14), command=tekan_ya, bg='#FF69B4', fg='White', width=8)
yes_button.pack(side=tk.LEFT, padx=10) 

no_button = tk.Button(window, text="No", font=("Helvetica",14), command=tekan_tidak, bg='#ff69B4', fg='White', width=8)
no_button.place(x=50, y = 50)

window.mainloop()




        