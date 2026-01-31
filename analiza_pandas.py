import pandas as pd

T_df = pd.read_csv("temperatury_student01.csv", sep=";", usecols=range(1,25))

print(T_df.min().min())     # wartosc minimalna
print(T_df.max().max())     # wartosc maksymalna
print(T_df.stack().mean())  # wartosc srednia

# wybieram wartosci do odrzcenia
mask_bad = (T_df < -30) | (T_df > 50)
print(mask_bad.sum().sum()) # liczba wartosci odrzuconych