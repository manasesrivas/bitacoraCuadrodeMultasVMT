import bitacora
from tkinter import ttk
import tkinter


class Window(tkinter.Tk):

    def __init__(self):
        super().__init__(baseName=None, className="Cuadro de multas VMT")
        super().geometry("400x400")
        super().wm_attributes("-topmost", True)
        super().resizable(False, False)
        self.var = tkinter.StringVar()
        self.question, self.answer = self.create_widget()

        super().mainloop()

    def create_widget(self):

        ttk.Label(self, text="Escribe el numero de pregunta", padding=20, font=("Arial", 15)).pack()
        
        entry = ttk.Entry(self, textvariable=self.var, font=("Arial", 20))
        entry.bind("<Return>", self.on_return)
        entry.pack()

        question = ttk.Label(self, padding=20, font=("Arial", 20), foreground="red", wraplength=350)
        question.pack_forget()
        
        answer = ttk.Label(self, padding=20, font=("Arial", 20), foreground="green")
        answer.pack_forget()

        return question, answer

    def on_return(self, event):
        self.set_widgets(int(self.var.get()))
        self.var.set("")
        

    def set_widgets(self, index):
        self.question.config(text=bitacora.diccionario[index][0])
        self.question.pack(fill=tkinter.X)

        self.answer.config(text=bitacora.diccionario[index][1])
        self.answer.pack()



if __name__ in "__main__":
    window = Window()