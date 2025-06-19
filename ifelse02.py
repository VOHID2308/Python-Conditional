parol = input("Parol kiriting: ")

harf_bor = ("a" in parol or "A" in parol)
raqam_bor = ("0" in parol or "1" in parol)

if len(parol) >= 8 and harf_bor and raqam_bor:
    print("Parol qabul qilindi.")
else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")