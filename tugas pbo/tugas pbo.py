# List nama
nama_list = ["Julia", "Hanan", "Eril", "Dwi", "Azizah", "Zayn", "Ogawa", "Apriyani"]

# Loop for untuk memeriksa setiap nama dalam list
for nama in nama_list:
    if len(nama) % 2 == 0:
        print(f"{nama} memiliki jumlah huruf genap")
    else:
        print(f"{nama} memiliki jumlah huruf ganjil")
    print("---")
