import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from app.parse_function import parse_function
from app.integrals import calculate_integral
from app.plot import show_graphs


class StartScreen:
    vertices = []
    start_x, start_y, canvas, root, repetitions = None, None, None, None, 1
    entry = None
    entry1 = None
    label1 = None
    label_result = None
    label_func = None
    func = None

    
    def on_select(self, v):
        """Запись движения ползунка"""
        self.repetitions = v

    def run(self):
        print(self.func.get())
        func1 = parse_function(self.func.get())
        if not func1:
            showerror("Ошибка!", "Ошибка в исходной формуле!")
            return
        self.repetitions = int(self.repetitions)
        calc_dots, res, err = calculate_integral(func1, self.vertices, self.repetitions)
        self.root.destroy()
        show_graphs(calc_dots, res, err, "Result for %d dots: %.4f" % (self.repetitions, res[-1]), "Error for %d dots: %.4f" % (self.repetitions, err[-1]))


    def add_new(self):
        self.vertices.append((float(self.entry.get()), float(self.entry1.get())))
        text = '     Points:\n'
        idx = 0
        for i in self.vertices:
            idx += 1
            text += f"№{idx}: x: {i[0]}, y: {i[1]}\n"
        self.label1['text'] = text

    def clear(self):
        self.vertices = []
        self.label1['text'] = ''


    def launch(self):
        """Отрисовка экрана"""
        self.root = tk.Tk()
        self.root.title("Rusile | Math-lab-2")
        self.root.config(cursor="pencil")
        self.root.geometry(
            f"{800}x{600}"
        )
        self.label_func = ttk.Label(text="Write function: ")
        self.label_func.pack()
        self.func = ttk.Entry()
        self.func.pack()
        self.label1 = ttk.Label()
        self.label1.pack()
        self.labelx = ttk.Label(text="X: ")
        self.labelx.pack()
        self.entry = tk.Entry()
        self.entry.pack()
        self.labely = ttk.Label(text="Y: ")
        self.labely.pack()
        self.entry1 = tk.Entry()
        self.entry1.pack()
        tk.Button(text="submit", command=self.add_new).pack()
        tk.Button(text="clear", command=self.clear).pack()
        scale = tk.Scale(
            self.root, from_=1, to=200, orient="horizontal", command=self.on_select
        )
        scale.pack()
        
        run_button = tk.Button(self.root, text="Run", command=self.run)
        run_button.pack()

        self.label_result = ttk.Label()
        self.label_result.pack()

        self.root.mainloop()
