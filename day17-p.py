# WAP for result management system

# result = ''
# n = int(input('Enter the number of student = '))
# for i in range(n):
#     name = input('Enter the student name = ')
#     eng = int(input('Enter marks in English = '))
#     nep = int(input('Enter marks in Nepali = '))
#     mth = int(input('Enter marks in Maths = '))
#     sc = int(input('Enter marks in Science = '))
#     soc = int(input('Enter marks in social = '))
#     per = (eng + nep + mth + sc + soc) / 5
#     data = f"{name},{eng},{nep},{sc},{soc}\n"
#     result = result + data
# print(result)

# csv = open('result.csv','w')
# csv.write("Name:,English:,Nepali:,Maths:,Science:,Social:\n")
# csv.write(result)
# csv.close()

# result = ""
# n = int(input('Enter the number of student = '))
# for i in range(n):
#     name = input('Enter the student name = ')
#     eng = int(input('Enter marks in English = '))
#     nep = int(input('Enter marks in Nepali = '))
#     mth = int(input('Enter marks in Maths = '))
#     sc = int(input('Enter marks in Science = '))
#     soc = int(input('Enter marks in social = '))
#     per = (eng + nep + mth + sc + soc) / 5
#     data = f"{name},{eng},{nep},{sc},{soc},{per}\n"
#     result = result + data
# print(result)

# file = open('result1.csv','w')
# file.write('Name of student,English,Nepali,Maths,Science,Social\n')
# file.write(result)
# file.close()

# import pandas as pd
# a = pd.read_csv('result1.csv')
# print(a)