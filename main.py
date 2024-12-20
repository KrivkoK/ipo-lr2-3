import math

def calculate_radius(v):
    # Вычисляем радиус по формуле
    radius = ((3 * v) / (4 * math.pi)) ** (1/3)
    return radius

# Ввод объема шара
X = float(input("Введите объем шара (в кубических единицах): "))

# Вычисление радиуса
radius = calculate_radius(X)

# Вывод результата
print(f"Радиус шара: {radius:.6f}")
