'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv', 'r', newline = '')
reader = csv.reader(infile)

#create an empty dictionary
list1 = []
emp_dict = {}

#use a loop to iterate through the csv file

for row in reader:
     if row[3] == 'Marketing':
        list1.append(row[1])
        list1.append(row[2])
        list1.append(row[5])
        for emp in emp_list: 
            full_name = row[1] + row[2]
            emp_dict[full_name] = row[5]


for emp in emp_dict:
    employee = emp_dict[emp]
    int(employee) * 1.10


for row in reader:
    if row[3] == 'Marketing':
        print('Manager name: ', row[1], row[2], 'Salary: ', row[5])


print()
print('=========================================')
print()

for emp in emp_dict:
    emp_dict[emp] = round(float(emp_dict[emp]) * 1.10,2)
    for k,j in emp_dict.items():
        print('Manager Name: ', k, 'Salary: ', j )

infile.close()

          
        

        
    
