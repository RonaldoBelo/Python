peso = float(input("Digite seu peso: "))
op = input("(K)g ou (L)bs: ")
if op.upper() == "K":
    print(f"Peso em Libras: {peso*2.20462:.2f}")
elif op.upper() == "L":
    print(f"Peso em Kilos: {peso*0.453592:.2f}")
else:
    print("Opção inválida... Digite (K) para Kilos e (L) para Libras")