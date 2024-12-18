import tkinter as tk
import random


def determine_winner(player_choice):
    choices = ['Papier', 'Kamień', 'Nożyce']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "Remis!"
    elif (player_choice == 'Papier' and computer_choice == 'Kamień') or \
            (player_choice == 'Kamień' and computer_choice == 'Nożyce') or \
            (player_choice == 'Nożyce' and computer_choice == 'Papier'):
        result = "Wygrałeś!"
    else:
        result = "Przegrałeś!"

    player_label.config(text=f"Twój wybór: {player_choice}")
    computer_label.config(text=f"Wybór komputera: {computer_choice}")
    result_label.config(text=f"Wynik: {result}")


window = tk.Tk()
window.title("Papier-Kamień-Nożyce")

window.geometry("500x400")

player_label = tk.Label(window, text="Twój wybór: ", font=("Arial", 18))
player_label.pack(pady=10)

computer_label = tk.Label(window, text="Wybór komputera: ", font=("Arial", 18))
computer_label.pack(pady=10)

result_label = tk.Label(window, text="Wynik: ", font=("Arial", 20, "bold"))
result_label.pack(pady=20)

paper_button = tk.Button(
    window, text="Papier", font=("Arial", 16), width=15, height=2,
    command=lambda: determine_winner("Papier")
)

paper_button.pack(pady=10)
rock_button = tk.Button(
    window, text="Kamień", font=("Arial", 16), width=15, height=2,
    command=lambda: determine_winner("Kamień")
)
rock_button.pack(pady=10)

scissors_button = tk.Button(
    window, text="Nożyce", font=("Arial", 16), width=15, height=2,
    command=lambda: determine_winner("Nożyce")
)
scissors_button.pack(pady=10)

window.mainloop()
