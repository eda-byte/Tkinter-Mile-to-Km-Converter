from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=150)
window.config(padx=20,pady=20)
is_equal= Label(text="is equal to",font=("Ariel",12,"bold"))
is_equal.grid(column=0,row=2)

miles_label= Label(text="Miles",font=("Ariel",12,"bold"))
miles_label.grid(column=2,row=1)

km_label= Label(text="Km",font=("Ariel",12,"bold"))
km_label.grid(column=2,row=2)

km_result_label= Label(text="0")
km_result_label.grid(column=1,row=2)
############################################


input = Entry(width=10)
input.grid(column=1,row=1)




def miles_to_km():
  #  print("I got clicked")
  miles=float(input.get())

  km = miles* 1.609

  #input.config(miles)
  km_result_label.config(text=f"{km}")



button =Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=3)##


#Entry






window.mainloop()