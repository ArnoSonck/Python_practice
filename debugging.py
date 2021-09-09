def divisors(num):
    divisors = [i for i in range(1,num+1) if num % i == 0]
    return divisors

# usando excepciones
# def run():
#     try:
#         num = int(input("ingresa un número: "))
#         if num <= 0:
#             raise ValueError
#         print(divisors(num))
#         print("Termino mi programa")
#     except ValueError:
#         print("Debes ingresar un número entero positivo")

# usando assert statements
def run():
    num = input("ingresa un número: ")
    assert num.isnumeric(),"Debe ingresar un número positivo"  
    print(divisors(int(num)))
    print("Termino mi programa")

if __name__=='__main__':
    run()