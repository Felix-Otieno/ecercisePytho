#Are data types that allow you to store key value pairs and they are mutable

employee = {
    "Name": "Maurice Kabarage",
    "Age": 39,
    "Salary": "$10,000",
    "Designation": "Manager"
}
print(employee["Name"], employee["Age"])

for i in employee:
    print(i)

for i in employee.keys():
     print(i)

for i in employee.values():
          print(i)
for key in employee:
      print(key + ":"+ str(employee[key]))