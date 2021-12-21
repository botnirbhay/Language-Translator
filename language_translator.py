#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pywin32


# In[7]:


from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import googletrans
import textblob
import pyttsx3
def transit():
    trans_text.delete(1.0,END)
    try:
        # we get languages keys from disctionary 
        for key,values in languages.items():
            if(values==original_combo.get()):
                originallang=key
        for key,values in languages.items():
            if(values==trans_combo.get()):
                translan_key=key 
        # converting original text to textblob
        words=textblob.TextBlob(original_text.get(1.0,END))  
        words=words.translate(from_lang=originallang,to=translan_key)
        trans_text.insert(1.0,words)
        # Initialising the speech engine
        engine=pyttsx3.init()
        voices=engine.getProperty("voices")
        #for voice in voices:
           # engine.setProperty('voice',voice.id) # note there are only few languages which can be spoken as the package is provided
            # by google 
        engine.say(words)
        # passing text to engine 
        
        # running the engine
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Translator",e)
def clear():
    original_text.delete(1.0,END)
    trans_text.delete(1.0,END)
languages=googletrans.LANGUAGES
language_list=list(languages.values())
window=Tk()
window.title('T R A N S I F Y')
bg=PhotoImage(file="C:/Users/hanju/OneDrive/Desktop/pythonlaball/translate.png")
lb=Label(window,image=bg)
lb.place(x=0,y=0,relwidth=1,relheight=1)
original_text=Text(window,height=10,width=40,bg='yellow')
original_text.grid(row=0,column=0,pady=20,padx=10)
buttontrans=Button(window,text=" Translate :)",font=("Helvetica",24),command=transit)
buttontrans.grid(row=0,column=2,pady=20,padx=10)
buttontrans.grid(row=0,column=1,pady=20,padx=10)
trans_text=Text(window,height=10,width=40,bg='green')
trans_text.grid(row=0,column=2,pady=20,padx=10)
original_combo=ttk.Combobox(window,width=50,value=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)
trans_combo=ttk.Combobox(window,width=50,value=language_list)
trans_combo.current(38)
trans_combo.grid(row=1,column=2)
clearbut=Button(window,text="clear",command=clear)
clearbut.grid(row=2,column=1)
#window.configure(bg="black")
window.resizable(False, False)
window.mainloop()


# In[ ]:





# In[ ]:




