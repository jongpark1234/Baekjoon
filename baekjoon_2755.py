from sys import stdin
credit_dict = {'A+' : 4.3, 'A0' : 4.0, 'A-' : 3.7, 'B+' : 3.3, 'B0' : 3.0, 'B-' : 2.7,
'C+' : 2.3, 'C0' : 2.0, 'C-' : 1.7, 'D+' : 1.3, 'D0' : 1.0, 'D-' : 0.7, 'F' : 0.0
}
totalcredit = 0; temp = 0
for _ in range(int(stdin.readline())):
    name, credit, grade = input().split(); credit = int(credit)
    totalcredit += credit
    temp += credit * credit_dict[grade]
print('{:.2f}'.format(round(temp / totalcredit + 1e-10, 2)))
