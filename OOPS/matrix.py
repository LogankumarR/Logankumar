class matrix():
    def __init__(self,row,col):
        self.row = m1
        self.col = l1
        self.matrix = []

    def buildmatrix(self):
        for col_idx in range(0,self.col):
            temp_row = []
            for row_idx in range (0,self.row):
                 ele = eval(input("enter a number in matrix col_num:" + str(col_idx)+ "row:"+str(row_idx))
                 temp_row.append(temp_row)
             self.matrix.append(temp_row)
    def prin(self):
             print(self.matrix)
def main():
    m1 = matrix(2,2)
    m1.buildmatrix()
    m1.prin()
main()