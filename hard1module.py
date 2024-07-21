grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

gpa1=sum(grades[0])/len(grades[0])
gpa2=sum(grades[1])/len(grades[1])
gpa3=sum(grades[2])/len(grades[2])
gpa4=sum(grades[3])/len(grades[3])
gpa5=sum(grades[4])/len(grades[4])

names=list(students)
names.sort()
n1=names[0]
n2=names[1]
n3=names[2]
n4=names[3]
n5=names[4]
print(dict([[n1,gpa1],[n2,gpa2],[n3,gpa3],[n4,gpa4],[n5,gpa5]]))

