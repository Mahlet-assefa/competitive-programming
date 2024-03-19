class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        my_set=set()
        
        def backexist(i, j, w):
            if w == len(word):
                return True
            
            if 0 > i or i >= len(board):
                return False
            if 0 > j or j >= len(board[0]):
                return False
            if board[i][j] != word[w] or (i,j) in my_set:
                return False
            my_set.add((i,j))
            
            up = backexist(i - 1, j, w + 1)
            down = backexist(i + 1, j, w + 1)
            left = backexist(i, j - 1, w + 1)
            right = backexist(i, j + 1, w + 1)
            
            my_set.remove((i,j))
            
            return up or down or left or right
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backexist(i, j, 0):
                    return True
        
        return False























        # up=True
        # down=True
        # row=True
        # col=True
        # letter=[]
        # my_set=set()
        # path=[]
        # for i in range(len(word)):
        #     letter.append(word[i])
       
        # def backexist(i,j):
        #     #base case
        #     if path not in my_set:

        #     if path[-1]==letter[i]:
        #         return 

        #     if i<len(board) and j<len(board) and board[i][j] not in my_set:
        #         path.append(board[i][j])
        #         backexist(i,j+1)
        #     if i<len(board) and j<len(board) and board[i][j] not in my_set:
        #         path.append(board[i][j])
        #         backexist(i+1,j)
        #     if 
            
            
            
                        

                    

         

                    
    





        # up=True
        # down=True
        # row=True
        # col=True
        # letter=[]
        # my_set=set()
        # path=[]
        # for i in range(len(word)):
        #     letter.append(word[i])
       
        # def backexist(i,j):
        #     #base case
        #     if path not in my_set:

        #     if path[-1]==letter[i]:
        #         return 

        #     if i<len(board) and j<len(board) and board[i][j] not in my_set:
        #         path.append(board[i][j])
        #         backexist(i,j+1)
        #     if i<len(board) and j<len(board) and board[i][j] not in my_set:
        #         path.append(board[i][j])
        #         backexist(i+1,j)
        #     if 
            
            
            
                        

                    

         

                    
    