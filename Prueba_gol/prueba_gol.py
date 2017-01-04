##movimiento de imagen
from tkinter import *
tk = Tk()
cont=0
canvas = Canvas(tk, width=800, height=300)
canvas.pack()
my_image2 = PhotoImage(file="arco.gif")
canvas.create_image(0,0,anchor=NW, image=my_image2)
my_image = PhotoImage(file="balon.gif")
canvas.create_image(550,0,anchor=NW, image=my_image)

def moveimage(event):
    if  event.keysym == 'Left':
        cont+1
        canvas.move(2, -2, 0)
        c=cont+1
        print (cont+c)
    
    else:
        canvas.move(2, 2, 0)
             
canvas.bind_all('<KeyPress-Left>', moveimage)
canvas.bind_all('<KeyPress-Right>', moveimage)
tk.mainloop()

