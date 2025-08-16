class Employee:
    def __init__(self,name,id,age,salary):
        print("Constructor called.")
        self.name = name
        self.id= id
        self.age = age
        self.salary = salary

    def __del__(self):
        print("Destructor called.")

    def credit(self):
        print(f"{self.salary} credited for {self.name}.")


employee= Employee('Akshita',82401,19,70000000)
employee.credit()

#to manually call a destructor we use " del employee"


