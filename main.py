def powitanie(imie):
	print(f"Cześć, {imie}! To świetny dzień na naukę!")
def odejmij_liczby(a, b):
    return a - b
if __name__ == "__main__":
    imie = input("Podaj swoje imię: ")
    powitanie(imie)

    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

    wynik = dodaj_liczby(a, b)
    print(f"Wynik odejmowania {a} i {b} to: {wynik}")


