class Board():
    def __init__(self,size):
        """
        Creates a size by size TicTacToe board
        """
        self.size = size
        self.matrix = [[" "] * self.size for i in range(self.size)]
        self.prev = ""
        #print(self.matrix)

    def __str__(self):
        s = self.size
        line = ""
        image = ""
        spaces = "-"*(4*s-1) + "\n"
        for x in range (s):
            for y in range (s):
                if y<s-1:
                    line = " " + self.matrix[x][y] + " " + "|"
                else:
                    line = " " + self.matrix[x][y] + " " + "\n"
                image += line
            if x < s-1:
                image += spaces
        return image


    def play(self, token, coord):
        """
            token takes in "x" or "o"
            coord takes in a coordinate for the matrix with row,column as a tuple
        """
        #check that an x or an o has been passed
        if token != "x" and token != "o":
            print("Please enter x or o for the token!")
        elif (self.prev != token) & (self.matrix[coord[0]][coord[1]] == " "):
            self.matrix[coord[0]][coord[1]] = token
            self.prev = token
        else: print("warning, can't play same token twice in a row or play where there's already a token")
        return self

    def winner(self):
        s = self.size
        #check rows for winner
        for x in range(s):
            count = 0
            for y in range(s-1):
                if(self.matrix[x][y] == self.matrix[x][y+1]):
                    count += 1
            if (count==(s-1)) & (self.matrix[x][y] != " "):
                return "The winner is " + str(self.matrix[x][y]) + " !"
        #check columns for winner
        for x in range(s):
            count = 0
            for y in range(s-1):
                if(self.matrix[y][x] == self.matrix[y-1][x]):
                    count += 1
            if (count==(s-1)) & (self.matrix[y][x] != " "):
                return "The winner is " + str(self.matrix[y][x]) + " !"
        #check left to right diagonal
        bool = True
        for x in range(s-1):
            if(self.matrix[x][x] != self.matrix[x+1][x+1]):
                bool = False
        if bool == True:
            return "The winner is " + str(self.matrix[0][0]) + " !"

        #check right to left diagonal
        bool = True
        minor = []
        for x in range(s-1):
            minor.append(self.matrix[x][s-x-1])
        for x in range(s-2):
            if minor[x] != minor[x+1]:
                bool = False
        if bool == True:
            return "The winner is " + str(self.matrix[0][s-1]) + " !"

        return None
