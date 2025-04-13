text = input("Enter a sentence: ")

f = open("output.txt", "w")
f.write(text)
f.close()

f = open("output.txt", "r")
icerik = f.read()
print(f"Dosyadaki içerik: {icerik}")
f.close()