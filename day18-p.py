n = int(input('Enter the number of student:'))
for i in range(n):
    name = input('Enter the name of the student:  ')
    phy = int('Enter marks in physics:  ')
    che = int('Enter marks in chemistry:  ')
    maths = int('Enter marks in maths:  ')
    eng = int('Enter marks in english:  ')
    nep = int('Enter marks in nepali:  ')
    soc = int('Enter marks in social:  ')
    total = phy + che + maths + eng + nep + soc
    per = (phy + che + maths + eng + nep + soc)/6
    if per < 50:
        grade = 'E'
    elif per <=50 & per < 60:
        grade = 'D'
    elif per <=60 & per < 70:
        grade = 'c'
    elif per <=70 & per < 80:
        grade = 'B'
    elif per <=80 & per < 90:
        grade = 'A'
    else:
        grade = 'A+'
    data = f'{name},{phy},{che},{maths},{eng},{nep},{soc},{total},{per},{grade}'
    result = result + data
    
try:
    file = open('ledger.csv','x')
except:
    print('File already exists')

file = open('ledger.csv','w')
file.write('                          XYZ School')
file.write('                       Tinkune,Kathmandu')
file.write('                First Terminal Examination Report')
file.write('                                             ')
file.write('                                             ')
file.write('                                             ')
file.write('Name,Physics,Chemistry,Maths,English,Nepali,Social')
file.write(result)






