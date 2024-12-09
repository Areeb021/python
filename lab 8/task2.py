class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)

    def average_marks(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        return 0

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average Marks: {self.average_marks()}")

student1 = Student("John", 20)
student1.add_marks([65, 90, 78])
student1.display_info()
