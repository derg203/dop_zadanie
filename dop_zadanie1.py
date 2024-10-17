grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 5, 2], [4, 4, 3], [5, 5, 5, 5, 4, 5]]
students = {'Джонни', 'Бильбо', 'Стив', 'Хендрик', 'Аарон'}
students=sorted(students)
book= {}
g=0
for s in students:
 book.update({s:sum(grades[g])/len(grades[g])})
 g=g+1
print(book)