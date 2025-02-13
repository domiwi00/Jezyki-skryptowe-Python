import random
import time
import sys

def shuffle(num):
    rnd = random.Random()
    for i in range(len(num)):
        swap(num, i, rnd.randint(0, len(num) - 1))


def swap(num, a, b):
    temp = num[a]
    num[a] = num[b]
    num[b] = temp


def ordered(size, start_value):
    num = [i + start_value for i in range(size)]
    return num


def compare2D(num1, num2, start, end):
    for i in range(start, end):
        if not compare(num1, num2[i]):
            return False
    return True


def compare(num1, num2):
    if len(num1) != len(num2):
        return False
    for i in range(len(num1)):
        if num1[i] == num2[i]:
            return False
    return True


def view(tab, strona, rozmiar):
    rozmiar -= 2
    widoczne = 0
    if strona == "prawo":
        for i in range(1, rozmiar + 1):
            widoczne = 0
            maks = 0
            for j in range(rozmiar, 0, -1):
                if tab[i][j] > maks:
                    maks = tab[i][j]
                    widoczne += 1
            tab[i][rozmiar + 1] = widoczne
    if strona == "lewo":
        for i in range(1, rozmiar + 1):
            maks = 0
            widoczne = 0
            for j in range(1, rozmiar + 1):
                if tab[i][j] > maks:
                    maks = tab[i][j]
                    widoczne += 1
            tab[i][0] = widoczne
    if strona == "gora":
        for i in range(1, rozmiar + 1):
            widoczne = 0
            maks = 0
            for j in range(1, rozmiar + 1):
                if tab[j][i] > maks:
                    maks = tab[j][i]
                    widoczne += 1
            tab[0][i] = widoczne
    if strona == "dol":
        for i in range(1, rozmiar + 1):
            widoczne = 0
            maks = 0
            for j in range(rozmiar, 0, -1):
                if tab[j][i] > maks:
                    maks = tab[j][i]
                    widoczne += 1
            tab[rozmiar + 1][i] = widoczne
    return widoczne


def print_table(result, size):
    for i in range(size):
        if i == 1 or i == size - 1:
            print("-" * (2 * size + 4 + size))
        for j in range(size):
            if j == 1 or j == size - 1:
                print("|  ", end="")
            print(str(result[i][j]).ljust(2), end=" ")
        print()


def save_to_file(result, size, wyjscie):
    with open(f"{wyjscie}", "w") as file:
        for i in range(size):
            if i == 1 or i == size - 1:
                file.write("-" * (2 * size + 4 + size) + "\n")
            for j in range(size):
                if j == 1 or j == size - 1:
                    file.write("| ")
                file.write(str(result[i][j]).ljust(2) if result[i][j] >= 10 else f" {result[i][j]}")
                file.write(" ")
            file.write("\n")


def main():
    try:
        wejscie=sys.argv[1]
        wyjscie=sys.argv[2]
        with open(f"{wejscie}", "r") as file:
            rozmiar = int(file.readline().strip())
            if rozmiar <= 0:
                raise ValueError("Rozmiar planszy nie moze byc mniejszy lub rowny 0.")
    except ValueError:
        print("Plik wejsciowy zawiera cos innego niz pojedyncza liczba calkowita dodatnia.")
        return
    except FileNotFoundError:
        print("Nie ma takiego pliku.")

    start_time = time.time()

    board = [ordered(rozmiar, 1) for _ in range(rozmiar)]
    shuffle(board[0])

    for x in range(1, rozmiar):
        board[x] = ordered(rozmiar, 1)
        while not compare2D(board[x], board, 0, x):
            elapsed_time = time.time() - start_time
            if elapsed_time > 60:
                print("Timeout - Program przekroczyl limit czasu (60s).")
                with open(f"{wyjscie}", "w") as file:
                    file.write(str(0))
                return 0
            shuffle(board[x])

    size = rozmiar + 2
    result = [[0] * size for _ in range(size)]
    for i in range(rozmiar):
        for j in range(rozmiar):
            result[i + 1][j + 1] = board[i][j]

    view(result, "prawo", size)
    view(result, "lewo", size)
    view(result, "gora", size)
    view(result, "dol", size)

    print_table(result, size)
    save_to_file(result, size, wyjscie)

    elapsed_time = time.time() - start_time
    print(f"Czas wykonania: {elapsed_time} s.")


if __name__ == "__main__":
    main()
