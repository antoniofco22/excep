def division(num):
    num1 = 1
    try:
        resultado = num1 / num
        print(resultado)
    except ZeroDivisionError:
        print("Não é possível fazer uma divisão por zero. Tente novamente.")
    except:
        print("Ocorreu um erro de tipo. Tente novamente.")
    print("Antonio")

division(0)
division('leia')