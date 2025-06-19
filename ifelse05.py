email = input("E-mailni kiriting: ")

if '@' in email and ('.com' in email or '.uz' in email or '.net' in email or '.org' in email):
    print("Email qabul qilindi")
else:
    print("Email noto'g'ri formatda")
