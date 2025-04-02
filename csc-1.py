import math 

x = float(input("Ingresa el valor para calcular la cosecante"))

if abs(x) < 1:
    print("Cosecante a la -1 solo está definida para |x| ≥ 1 te veo como mal")
else:
    angulo = math.asin(1 / x)
    print(f"csc⁻¹({x}) = {angulo} en radianes")
    
