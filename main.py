from tkinter import *

window=Tk()

window.title("bmi calculator")
window.configure(bg="white")
label_height=Label(text="enter a height(cm)",bg="white",fg="black")
label_height.grid(column=0,row=0)
label_mass=Label(text="enter a mass(kg)",bg="white",fg="black")
label_mass.grid(column=0,row=2)
height_entry=Entry(bg="white",fg="black")
height_entry.focus()
mass_entry=Entry(bg="white",fg="black")
mass_entry.grid(column=0,row=3)
height_entry.grid(column=0,row=1)

result_label=Label(bg="white",fg="black")
result_label.grid(column=0,row=5)

def input_values():
    a = height_entry.get()
    b = mass_entry.get()

    if a=="" or b=="":
        result_label.config(text="lütfen değer giriniz")

    else:

        try:
            bmi=float(b)/(float(a)/100)**2
            result_label.config(text=f"your bmi is {bmi}")
        except:
            result_label.config(text="sayı gir harf değil")


button=Button(text="calculate",command=input_values,bg="white",fg="black")
button.grid(column=0,row=4)


mainloop()
