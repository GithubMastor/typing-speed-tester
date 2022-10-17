import tkinter as tk
import csv
import random
import time

############  SENTENCE GETTER  ############
def sentencer():
    with open("sentences.csv", "r") as sentence_csv_file:
        csv_reader = csv.reader(sentence_csv_file)
        # This skips over the first line in the .csv (first_name, last_name)
        next(csv_reader)
        return random.choice([line[0] for line in csv_reader])

############  REGISTER PRESS  ############
active = True
def onKeyPress(event):
    if (event.char.isalnum() or event.char.isspace()) and active==True:
        key_checker(event.char,sent)

############  CHECK PRESS  ############
# class Counter():
#     def __int__(self):
#         self.counter=0
#     def inc(self):
#         self.counter+=1
#     def reset(self):
#         self.counter=0
#     def getval(self):
#         return self.counter




############  CHECK PRESS  ############
cnt = 0
def key_checker(char,sentence):
    global cnt, active, start, end, charpersec, wordpermin

    print(char + '\n' +  sentence[cnt] + '\n' + sentence)
    if cnt == (len(sentence)-2):
        if char == sentence[cnt]:
            text.configure(state='normal')
            text.tag_remove('cur', f"1.{cnt}")
            text.tag_add("o", f"1.{cnt}", )
            text.tag_configure("o", foreground='green')
            text.configure(state='disabled')
            text.pack()
        else:
            text.configure(state='normal')
            text.tag_remove('cur', f"1.{cnt}")
            text.tag_add("x", f"1.{cnt}")
            text.tag_configure("x", foreground='red')
            text.configure(state='disabled')
            text.pack()
        active=False
        end = time.time()
        timed = end - start
        print(timed)
        charpersec = round((len(sent) / timed),2)
        wordpermin = round((charpersec*12),2)
        print(f'Characters Per Second: {charpersec}\nWords Per Minute (average): {wordpermin}')
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
        text.pack()
    else:
        text.configure(state='normal')
        text.tag_remove('cur',f"1.{cnt}")
        text.tag_add("x",f"1.{cnt}")
        text.tag_configure("x",foreground='red')
        text.tag_add("cur",f"1.{cnt+1}",)
        text.tag_configure("cur",background='orange')
        text.configure(state='disabled')
        text.pack()
    cnt+=1




############  WINDOW  ############
sent = sentencer().lower()
window = tk.Tk()
sw = round(window.winfo_screenwidth() / 2)
sh = round(window.winfo_screenheight() / 2)
window.geometry(f'{sw}x{sh}')
window.configure(bg='#FFFFFF')
my_font1=('times', 30, 'bold')

label1 = tk.Label(window,text=('TYPE SENTENCE BELOW:\n\n' + ''),width=30,font=my_font1,bg='#FFFFFF')
label1.configure(bg='#FFFFFF', wraplength=600)
label1.grid(row=0,column=1,columnspan=6)
label1.pack()

text = tk.Text(window,  font=('Sans Serif', 24), height=5, width=round(sw/40),wrap='word')
text.insert(tk.END,chars= sent)
text.configure(state='disabled')
text.pack()

# label2 = tk.Label(window,text=('TYPE SENTENCE BELOW:\n\n' + ''),width=15,font=my_font1,bg='#FFFFFF')
# label2.configure(bg='#FFFFFF', wraplength=600)
# label2.grid(row=2,column=1,columnspan=3)
# label2.pack()

# text2 = tk.Text(window,  font=('Sans Serif', 24), height=5, width=round(sw/40),wrap='word')
# text2.configure(state='disabled')
# text2.pack()

############  TIMER  ############
start = time.time()
print("hello")
end = time.time()
charpersec = 0
wordpermin = 0





############  ############  ############
window.bind('<KeyPress>', onKeyPress)
window.mainloop()