# Chipta narxi
asosiy_narx = 100

yosh = int(input("Yoshingizni kiriting: "))

chegirma_foizi = 0

if yosh < 7:
    chegirma_foizi = 50
if yosh >= 7 and yosh <= 17:
    chegirma_foizi = 20
if yosh > 60:
    chegirma_foizi = 30

chegirma_som = (chegirma_foizi / 100) * asosiy_narx
yakuniy_narx = asosiy_narx - chegirma_som

if chegirma_foizi > 0:
    print(f"Yakuniy narx: {yakuniy_narx} so'm ({chegirma_foizi}% chegirma qo'llanildi)")
else:
    print(f"Yakuniy narx: {asosiy_narx} so'm (Chegirma qo'llanilmadi)")