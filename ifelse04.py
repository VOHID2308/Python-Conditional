hisob = 5000.00

kiritish = float(input("Qancha pull yechib olmoqchisiz : "))

if kiritish >= 0:
    if kiritish <= hisob:
        hisob -= kiritish
        print(f"Pul yechildi. qolgan balans : {hisob} som ")
    else: 
        print(f" Mablag' yetarli emas. sizning balansizngiz: {hisob} som ")
else:
    print("Manfiy summa kiritib bolmaydi.")