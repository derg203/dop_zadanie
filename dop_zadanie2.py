grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 5, 2], [4, 4, 3], [5, 5, 5, 5, 4, 5]]
students = {'Джонни', 'Бильбо', 'Стив', 'Хендрик', 'Аарон'}
a=sorted(students)
book={}
book.update({a[0]:sum(grades[0])/len(grades[0])})
book.update({a[1]:sum(grades[1])/len(grades[1])})
book.update({a[2]:sum(grades[2])/len(grades[2])})
book.update({a[3]:sum(grades[3])/len(grades[3])})
book.update({a[4]:sum(grades[4])/len(grades[4])})
print(book)
