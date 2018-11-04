# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

outer_range = range(2, 100)
inner_range = range(2, 10)
result = {}

for i in outer_range:
    for j in inner_range:
        if i % j == 0:
            if j in result:
                result[j] += 1
            else:
                result[j] = 1

# выводим рез-ты
# задачу можно было бы решить не используя словари, а только списки, но со словарем получается нагляднее
for key, value in result.items():
    print(f'Кол-во чисел из диапазона от 2 до 99 кратных {key}: {value}')