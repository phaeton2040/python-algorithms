# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. Например,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

# где в этой задаче использовать hash или sha1 ?
def count_substr(string):
    string = str.lower(string)
    max_substr_length = len(string) - 1
    # Единственное в этой задаче, что связано с хэшированием.
    substr_set = set([])

    for i in range(len(string)):
        for j in range(len(string)):
            s = string[j:max_substr_length + j]
            if len(s) == max_substr_length:
                substr_set.add(s)
                # В чате один студент описывал свое решение, где он
                # берет хэш от подстроки и помещает ее во множество.
                # Есть ли в этом смысл? без хэширования будет то же самое и даже быстрее
                # substr_set.add(hash(s))
        max_substr_length -= 1
        if max_substr_length == 0:
            break
    return len(substr_set)

print(count_substr('co co cocokookrttr do od doo'))
print(count_substr('papa'))
print(count_substr('mama'))
