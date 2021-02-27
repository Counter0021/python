# Сортировка с lambda по последним буквам
a = ["apple", "banana", "orange", "soup", "tomato", "potato"]
print(a)
a.sort(key=lambda i: i[-1])
print(a)
# 1 вариант без lambda
a.sort(key=len)
print(a)
# 2 вариант с lambda
a.sort(key=lambda i: len(i))
print(a)