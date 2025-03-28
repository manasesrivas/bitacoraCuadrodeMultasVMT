import bitacora
from tkinter import ttk
import tkinter


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__(baseName=None, className="Cuadro de multas VMT")
        super().geometry("400x400")
        self.var = tkinter.StringVar()
        self.label = self.create_widget()
        super().wm_attributes("-topmost", True)
        super().mainloop()

    def create_widget(self):
        ttk.Label(self, text="Escribe el numero de pregunta", padding=20, font=("Arial", 15)).pack()
        
        entry = ttk.Entry(self, textvariable=self.var, font=("Arial", 20))
        entry.bind("<Return>", self.on_return)
        entry.pack()

        label = ttk.Label(self, padding=20, font=("Arial", 20), foreground="green")
        label.pack_forget()
        return label

    def on_return(self, event):
        self.set_text_label(int(self.var.get()))
        self.var.set("")
        

    def set_text_label(self, index):
        self.label.config(text=bitacora.diccionario[index][1])
        self.label.pack()


if __name__ in "__main__":
    window = Window()