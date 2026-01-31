import numpy as np

# Wybiera pierwszą kolumnę z dniami tygodnia,
dni = np.genfromtxt("temperatury_student01.csv", delimiter=";", skip_header=1, usecols=[0], dtype=str)

# Wybiera wszystko oprócz pierwszej kolumny z dniami tygodnia
T = np.genfromtxt("temperatury_student01.csv", delimiter=";", skip_header=1, usecols=range(1,25))

# funkcja wyprintuj dane jest uruchamiana lokalnia
def wyprintuj_dane():
    print(T)
    print(dni)
    print(T.shape) # ksztalt
    print(np.isnan(T).sum())

def main():
    # Treść głównej funkcji
    wyprintuj_dane()

if __name__ == "__main__":
    main()