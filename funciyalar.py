def juft_yoki_toq():
    try:
        a = int(input("Son kiriting: "))
        if a % 2 == 0:
            print("Juft son")
        else:
            print("Toq son")
    except ValueError:
        print("Butun son kiriting!")


def eng_kattasi():
    try:
        a = int(input("1-son: "))
        b = int(input("2-son: "))
        c = int(input("3-son: "))
        print("Eng katta son:", max(a, b, c))
    except ValueError:
        print("Butun son kiriting!")


def baholash():
    try:
        a = int(input("Ball kiriting: "))
        if 90 <= a <= 100:
            print("A")
        elif 80 <= a < 90:
            print("B")
        elif 70 <= a < 80:
            print("C")
        elif 60 <= a < 70:
            print("D")
        elif 0 <= a < 60:
            print("F")
        else:
            print("0-100 oralig‘ida kiriting")
    except ValueError:
        print("Butun son kiriting!")


def yigindi():
    try:
        n = int(input("N kiriting: "))
        s = 0
        for i in range(1, n + 1):
            s += i
        print("Yig‘indi:", s)
    except ValueError:
        print("Butun son kiriting!")


def faktorial():
    try:
        n = int(input("Son kiriting: "))
        f = 1
        for i in range(1, n + 1):
            f *= i
        print("Faktorial:", f)
    except ValueError:
        print("Butun son kiriting!")


def juft_sonlar():
    print("1 dan 100 gacha juft sonlar:")
    for i in range(2, 101, 2):
        print(i)


def tub_son():
    try:
        a = int(input("Son kiriting: "))
        if a <= 1:
            print("Tub son emas")
        else:
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    print("Tub son emas")
                    break
            else:
                print("Tub son")
    except ValueError:
        print("Butun son kiriting!")


def raqamlar_yigindisi():
    try:
        a = int(input("Son kiriting: "))
        s = 0
        for digit in str(abs(a)):
            s += int(digit)
        print("Raqamlar yig‘indisi:", s)
    except ValueError:
        print("Butun son kiriting!")

def palindrom_son():
    try:
        a = int(input("3 xonali Son kiriting "))
        if a <= 999 and a>=100:
            True
        else:
            False

        b = a%10
        c = a//100
        if b == c:
            print("palindrom son")
        else:
            print("Palindrom emas")
    except ValueError:
        print("3 xonali son kiriting")


# 🔥 MENU
while True:
    print("\n--- MENU ---")
    print("1. Juft yoki Toq")
    print("2. Eng katta son")
    print("3. Baholash tizimi")
    print("4. 1 dan N gacha yig‘indi")
    print("5. Faktorial")
    print("6. 1-100 juft sonlar")
    print("7. Tub son tekshirish")
    print("8. Raqamlar yig‘indisi")
    print("9. Palindrom sonlar")
    print("0. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        juft_yoki_toq()
    elif tanlov == "2":
        eng_kattasi()
    elif tanlov == "3":
        baholash()
    elif tanlov == "4":
        yigindi()
    elif tanlov == "5":
        faktorial()
    elif tanlov == "6":
        juft_sonlar()
    elif tanlov == "7":
        tub_son()
    elif tanlov == "8":
        raqamlar_yigindisi()
    elif tanlov == "9":
        palindrom_son()
    elif tanlov == "0":
        print("Dastur tugadi.")
        break
    else:
        print("Noto‘g‘ri tanlov!")
