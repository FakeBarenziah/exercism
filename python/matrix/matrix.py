class Matrix:
    def __init__(self, matrix_string):
        self.rows = matrix_string.split("\n")

        for str in range(len(self.rows)):
            self.rows[str] = self.rows[str].split(" ")
            for i in range(len(self.rows[str])):
                self.rows[str][i] = int(self.rows[str][i])

        self.columns = []

        for each in range(len(self.rows[0])):
            self.columns.append([row[each] for row in self.rows])
            

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
