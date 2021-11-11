import tkinter as tk

class Aplicacion:
    def _init_(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Estofado", command=self.ventana2)
        opciones1.add_command(label="Ceviche", command=self.ventana3)
        opciones1.add_command(label="Lomo saltado", command=self.fijarazul)
        opciones1.add_command(label="pollo a la brasa", command=self.fijarazul)
        opciones1.add_command(label="Ceviche", command=self.fijarrosado)
        menubar1.add_cascade(label="platos de comida", menu=opciones1)        
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="Limonada", command=self.ventanabebidas)
        opciones2.add_command(label="Chicha", command=self.ventanabebidas)
        opciones2.add_command(label="jugo de piña", command=self.ventanabebidas)
        menubar1.add_cascade(label="bebidas", menu=opciones2)        
        self.ventana1.mainloop()

    def ventana2(self):
        self.ventana2=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana2, width=700, height=500, background="black")
        self.canvas1.grid(column=0, row=0)
        archi1=tk.PhotoImage(file="CEVICHES.png")
        self.canvas1.create_image(30, 100, image=archi1, anchor="nw")
        self.ventana2.mainloop() 
        
        

    def ventana3(self):
        self.ventana3=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana3, width=700, height=500, background="black")
        self.canvas1.grid(column=0, row=0)
        archi1=tk.PhotoImage(file="ESTOFADO.png")
        self.canvas1.create_image(30, 100, image=archi1, anchor="nw")
        self.ventana3.mainloop() 
        
        

    def fijarazul(self):
        self.ventana1.configure(background="blue")
        
    def fijarrosado(self):
        self.ventana1.configure(background="pink")

    def ventanabebidas(self):
        self.ventana1.geometry("900x480")

    def ventanabebidas(self):
        self.ventana1.geometry("900x480")

    def ventanabebida(self):
        self.ventana1.geometry("900x480")

aplicacion1=Aplicacion()