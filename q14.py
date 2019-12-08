peso = float(input("Informe o peso dos peixes pescados: "))
multaPorQuilo = 4.0
pesoMaximo = 50.0

if (peso > pesoMaximo):
    excesso = peso - pesoMaximo
    print("Excesso de peso(%.2f). você foi multado em: %.2f"%(excesso, excesso*multaPorQuilo))
else:
    print("Não houve excesso de peso")
