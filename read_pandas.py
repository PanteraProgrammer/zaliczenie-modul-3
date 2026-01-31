import pandas as pd

# wybieram pierwszą kolumnę z dniami
dni = pd.read_csv("temperatury_student01.csv", sep=";", usecols=[0])

# wybieram wszystkie kolumny oprocz pierwszej z dniami
T_df = pd.read_csv("temperatury_student01.csv", sep=";", usecols=range(1,25))

print(dni)
print(T_df.shape) # ksztalt

# liczba pustych pol w całej tabeli
print(T_df.isnull().sum().sum())