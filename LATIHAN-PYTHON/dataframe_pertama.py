import pandas as pd

data = {
    "nama" : ["Andi", "Budi", "Citra"],
    "kota" : ["Jakarta", "Bandung", "Surabaya"],
    "nilai" : [80, 75, 90] 
}

tabel = pd.DataFrame(data)

print(tabel)
print()
print(tabel.describe())