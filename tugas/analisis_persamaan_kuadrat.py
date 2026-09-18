import math

print("Analisis Persamaan Kuadrat")

a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    diskriminan = b ** 2 - 4 * a * c
    print(f"Diskriminan = {diskriminan:.2f}")

    if diskriminan > 0:
        akar1 = (-b + math.sqrt(diskriminan)) / (2 * a)
        akar2 = (-b - math.sqrt(diskriminan)) / (2 * a)

        print(f"Dua akar real: {akar1:.2f} dan {akar2:.2f}")

    elif diskriminan == 0:
        akar = -b / (2 * a)

        print(f"Akar kembar: {akar:.2f}")

    else:
        print("Tidak ada akar real.")