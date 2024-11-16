import tkinter as tk

class SekilCizmeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Şekil Çizme Uygulaması")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.label = tk.Label(root, text="Çizmek istediğiniz şekli girin (kare, dikdörtgen, daire, üçgen):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Çiz", command=self.ciz)
        self.button.pack()

    def ciz(self):
        sekil = self.entry.get().lower()
        self.canvas.delete("all")

        if sekil == "kare":
            self.canvas.create_rectangle(100, 100, 300, 300, outline="black", fill="blue")
        elif sekil == "dikdörtgen":
            self.canvas.create_rectangle(50, 150, 350, 250, outline="black", fill="green")
        elif sekil == "daire":
            self.canvas.create_oval(100, 100, 300, 300, outline="black", fill="red")
        elif sekil == "üçgen":
            self.canvas.create_polygon(200, 50, 50, 350, 350, 350, outline="black", fill="yellow")
        else:
            self.canvas.create_text(200, 200, text="Geçersiz şekil adı!", fill="red", font=("Helvetica", 16))

if __name__ == "__main__":
    root = tk.Tk()
    app = SekilCizmeApp(root)
    root.mainloop()
