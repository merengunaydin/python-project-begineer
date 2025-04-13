hM = int(input("Kac sayi girecelsiniz: "))

total = 0

for i in range(0,hM):
    data = int(input(f"{i+1}. sayiyi giriniz: "))
    total = total + data

print(f"Ortalama: {total / hM}")