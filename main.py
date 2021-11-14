from tkinter import *

write = None
code = None
canWriteCode = True

window = Tk()

window.title('Register System')
window.resizable(False, False)

lbl_message = Label(window,
                    text = 'Define your password:',
                    font = ('Consola', 20))

ety_entry = Entry(window,
                  font = ('Consola', 30))

def Press_Button():
    global code
    global canWriteCode

    if canWriteCode == True:
        if len(ety_entry.get()) != 0:
            entry = ety_entry.get()

            code = entry
            
            lbl_message.config(text = 'Type your password:')           
            try:
                btn_ok.config(text = 'Ok')
            except:
                pass

            ety_entry.delete(0, END)    
            
            canWriteCode = False
        else:
            pass
    else:
        write = ety_entry.get()

        if write == code:
            lbl_message.config(text = 'Correct password!')
        else:
            lbl_message.config(text = 'Try again...')
    pass

btn_ok = Button(window,
                text = 'Define',
                font = ('Consola', 20),
                command = Press_Button)

lbl_message.pack()
ety_entry.pack()
btn_ok.pack()

window.mainloop()