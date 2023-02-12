def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Seleziona l'operazione che vuoi eseguire:")
print("1. Addizione")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")

scelta = int(input("Inserisci il numero dell'operazione che vuoi eseguire (1/2/3/4): "))

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

if scelta == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif scelta == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif scelta == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif scelta == 4:
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Input non valido. Riprova.")

input("Premi INVIO per uscire")