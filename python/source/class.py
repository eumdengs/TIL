class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def info():
        print("학번: {0} 이름: {1}".format(self.id, self.name))

    class Student(Person):
        def __init__(self, id, name, major):
            super().__init__(id,name)
            self.major = major

        def student_info():
            super.info()
            print("전공: {0}".format(self.major))