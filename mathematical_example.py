import math
a = float(input("Print a:"))
b = float(input("Print b:"))
c = float(input("Print c:"))
d = float(input("Print d:"))

print("e^a|b/c-d*5|log2 d = ")
# Вычислите e^a 
exp_a = math.exp(a)

# Вычислите b / c
div_bc = b / c

# Вычислите d ∙ 5
mul_d5 = d * 5

# Вычислите log_2⁡d
log2_d = math.log2(d)

# Вычислите b / c - d * 5
result1 = div_bc - mul_d5

# Вычислите e ^ a or b / c - d * 5
result2 = int(exp_a) | int(result1)

#e^a|b/c-d*5|log2 d
result3 = result2 | int(log2_d)

# Выведите результат
print(result3/1000) 