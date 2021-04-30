"""
start
open file 'Final.txt'
count number of grades in the file
find the average by adding up all the grades and dividing them by the total number of grades
find the percentage of grades that are above the average grade
output the results
end
"""

"""
infile = open file 'Final.txt' in read mode
grades = lines in infile
close file 'Final.txt'
count number of grades
average = sum of grades / number of grades
sum % of grades > than average
print results
"""

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade > average:
        num +=1
print("Number of grades: ", len(grades))
print("Average grade: ", average)
print("Percentage of grades above average: {0:.2f}%".format(100 * num / len(grades)))
