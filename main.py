import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el número")
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.points = 0
        
        # Ajusta el tamaño de la ventana principal y el tamaño de fuente
        self.root.geometry("600x500")  # Ancho x Alto
        self.root.option_add('*Font', 'Helvetica 20')

        # Marco principal para centrar el contenido
        main_frame = tk.Frame(root)
        main_frame.pack(expand=True)

        self.label = tk.Label(main_frame, text="Adivina el número (1-100):")
        self.label.pack()

        chatGptText = tk.Label(main_frame, text="Hecho por iker y Chatgpt", pady=5)
        chatGptText.pack()

        self.entry = tk.Entry(main_frame)
        self.entry.pack()
        self.entry.bind('<Return>', self.check_guess)  # Asocia Enter con la función check_guess

        self.button = tk.Button(main_frame, text="Adivinar", command=self.check_guess)
        self.button.pack()

        self.points_label = tk.Label(main_frame, text=f"Puntos: {self.points}")
        self.points_label.pack()

        self.result_label = tk.Label(main_frame, text="")
        self.result_label.pack()

    def check_guess(self, event=None):  # El evento es opcional para poder asociarlo con Entry y el botón
        self.attempts += 1
        guess = int(self.entry.get())
        if guess < self.target_number:
            self.result_label.config(text=f"Intento #{self.attempts}: Demasiado bajo. ¡Inténtalo de nuevo!")
        elif guess > self.target_number:
            self.result_label.config(text=f"Intento #{self.attempts}: Demasiado alto. ¡Inténtalo de nuevo!")
        else:
            self.points += random.randint(1, 4)  # Añadir 5 puntos al adivinar
            self.result_label.config(text=f"¡Felicidades! Adivinaste el número {self.target_number} en {self.attempts} intentos.")
            self.points_label.config(text=f"Puntos: {self.points}")
            self.button.config(state="disabled")
            self.entry.config(state="disabled")
            self.root.after(5000, self.restart_game)  # Reiniciar el juego después de 5 segundos
    
    def input(key):
        if key == 'q' or key == 'escape':
            quit()
            points_file = open("points.txt", "w+")
            points_file.write(self.points)

    def restart_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="Nuevo juego. Adivina el número (1-100):")
        self.button.config(state="normal")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)  # Limpia la entrada

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

