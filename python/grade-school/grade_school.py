class School:
    def __init__(self):
        self.student_list = []
        self.featured_grades = []

    def add_student(self, name, grade):
        new_student = (name, grade)
        self.student_list.append(new_student)
        if not grade in self.featured_grades:
            self.featured_grades.append(grade)        
        self.student_list.sort(key=self.roster_sort)
        self.featured_grades.sort()
        return self
        

    def roster(self):
        all_students = []

        for i in range(0, len(self.featured_grades)):
            all_students += self.grade(self.featured_grades[i])
        return all_students

    def grade(self, grade_number):
        grade_roster = filter(self.filter_search(grade_number), self.student_list)

        return list(map(lambda each: each[0], grade_roster))
    
    def filter_search(self, grade):
        def callback(student):
            return student[1] == grade
        return callback

    def roster_sort(self, tup):
        return tup[0]