# В масиві, який складається із n чисел, обчислити: Кількість елементів масиву, менших С (С – задається користувачем);
# # use comprehension

lis = [1, 2, 67, -3, 6, 0.25, -3.89, 4.52, -12, -7]
nums = float(input('Set a digit: '))

amount = [num for num in lis if num < nums]

print(len(amount))



