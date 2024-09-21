class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail()
    def generateEmail(self):
        return f'{self.name}@company.com'
    def __str__(self):
        return (f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, '
                f'Gender: {self.gender}, Email: {self.email}')  
    def showInfo(self):
        print(self.name, self.age, self.salary, self.gender, self.email) 
        obj = Employee('John', '39', '$20,000', 'M')
        print(obj)
      