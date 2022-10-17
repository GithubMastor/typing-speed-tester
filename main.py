import tkinter as tk
import csv
import random
import time
from PIL import Image, ImageTk

############  SENTENCE GETTER  ############
def sentencer():
    with open("sentences.csv", "r") as sentence_csv_file:
        csv_reader = csv.reader(sentence_csv_file)
        next(csv_reader)
        return random.choice([line[0] for line in csv_reader])

############  REGISTER PRESS  ############
active = True
def onKeyPress(event):
    if (event.char.isalnum() or event.char.isspace() or event.char =='-' or event.char ==','or event.char =="'") and active==True:
        key_checker(event.char,sent)


############  RESET  ############
def reset():
    global cnt, active, start, end, charpersec, wordpermin, incorrect, sent
    sent = sentencer().lower()

    label1.config(text=('TYPE SENTENCE BELOW:\n\n' + ''))
    text.configure(state='normal')
    text.delete("1.0", "end")
    text.insert(tk.END,chars= sent)
    text.configure(state='disabled')
    label2.config(text=('Char/Sec:                  \nWord/Min:                  \n% Correct:                  '),  justify='left')

    cnt,charpersec,wordpermin,incorrect=0,0,0,0
    active=True


############  CHECK PRESS  ############
cnt = 0
incorrect = 0
def key_checker(char,sentence):
    global cnt, active, start, end, charpersec, wordpermin, incorrect
    if cnt == (len(sentence)-2):
        if char == sentence[cnt]:
            text.configure(state='normal')
            text.tag_remove('cur', f"1.{cnt}")
            text.tag_add("o", f"1.{cnt}", )
            text.tag_configure("o", foreground='green')
            text.configure(state='disabled')
            text.grid(row=1, column=0, columnspan=1)
        else:
            text.configure(state='normal')
            text.tag_remove('cur', f"1.{cnt}")
            text.tag_add("x", f"1.{cnt}")
            text.tag_configure("x", foreground='red')
            text.configure(state='disabled')
            text.grid(row=1, column=0, columnspan=1)
        active=False
        end = time.time()
        timed = end - start
        print(timed)
        charpersec = round((len(sent) / timed),2)
        wordpermin = round((charpersec*12),2)
        percor = round(((len(sent)-incorrect)/len(sent))*100,2)
        print(f'Characters Per Second: {charpersec}\nWords Per Minute (average): {wordpermin}\n% Correct: {percor}%')
        label2.config(text=(f'Char/Sec:   {charpersec}\nWord/Min: {wordpermin}\n% Correct: {percor}%'))
    elif char == sentence[cnt]:
        if cnt==0:
            start = time.time()
            print("hello")
        text.configure(state='normal')
        text.tag_remove('cur',f"1.{cnt}")
        text.tag_add("o",f"1.{cnt}",)
        text.tag_configure("o",foreground='green')
        text.tag_add("cur",f"1.{cnt+1}",)
        text.tag_configure("cur",background='orange')
        text.configure(state='disabled')
        text.grid(row=1, column=0, columnspan=1)
    else:
        text.configure(state='normal')
        text.tag_remove('cur',f"1.{cnt}")
        text.tag_add("x",f"1.{cnt}")
        text.tag_configure("x",foreground='red')
        text.tag_add("cur",f"1.{cnt+1}",)
        text.tag_configure("cur",background='orange')
        text.configure(state='disabled')
        text.grid(row=1, column=0, columnspan=1)
        incorrect+=1

    cnt+=1




############  WINDOW  ############

sent = sentencer().lower()
window = tk.Tk()
window.iconbitmap('favicon.ico')
window.title('          Typing Speed Test')
sw = round(window.winfo_screenwidth() / 2)
sh = round(window.winfo_screenheight() / 3)
window.geometry(f'{sw}x{sh}')
window.configure(bg='#FFFFFF')
my_font1=('times', 30, 'bold')

label1 = tk.Label(window,text=('TYPE SENTENCE BELOW:\n\n' + ''),width=30,font=my_font1,bg='#FFFFFF')
label1.configure(bg='#FFFFFF', wraplength=600)
label1.grid(row=0,column=0,columnspan=1)


text = tk.Text(window,  font=('Sans Serif', 24), height=4, width=round(sw/40),wrap='word')
text.insert(tk.END,chars= sent)
text.configure(state='disabled')
text.grid(row=1,column=0,columnspan=1)


label2 = tk.Label(window,text=('Char/Sec:                  \nWord/Min:                  \n% Correct:                  '),width=30,font=my_font1,bg='#FFFFFF', justify='left')
label2.configure(bg='#FFFFFF', wraplength=400)
label2.grid(row=1,column=1,columnspan=1)

button1 = tk.Button(window, text='Browse Files',width=20,command = lambda:reset())
btn_img = Image.open('button_reset.png')
imz = ImageTk.PhotoImage(btn_img)
button1.configure(image=imz, width=imz.width(), bg='#FFFFFF',borderwidth=0)
button1.grid(row=2,column=0,columnspan=1, padx=10, pady=10)

############  TIMER  ############
start = time.time()
print("hello")
end = time.time()
charpersec = 0
wordpermin = 0





############  ############  ############
window.bind('<KeyPress>', onKeyPress)
window.mainloop()