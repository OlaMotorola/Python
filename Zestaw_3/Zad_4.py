while True:
    user_input = input("Podaj liczbę rzeczywistą (lub 'stop' aby zakończyć): ")

    if user_input.lower() == 'stop':
        print("Zakończono program.")
        break

    try:
        x = float(user_input)
        print(f"Liczba: {x}, Trzecia potęga: {x ** 3}")
    except ValueError:
        print("Błąd: Proszę podać poprawną liczbę rzeczywistą.")
