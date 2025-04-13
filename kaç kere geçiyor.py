string = input("Bir cümle giriniz: ")

aranan = input("Aranacak harfi giriniz: ")

count = 0

string = string.lower

for harf in string:
    if(harf == aranan):
        count += 1

print(f"{aranan} harfi {count} kere geciyor.")

