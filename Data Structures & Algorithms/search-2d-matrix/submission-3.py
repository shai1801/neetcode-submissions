class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top,bot=0,rows-1

        
        while top<=bot:
            midRow=top+((bot-top)//2)
            if target>matrix[midRow][-1]:
                top=midRow+1
            elif target<matrix[midRow][0]:
                bot=midRow-1
            else:
                break
        
        if not (top<=bot):
            return False

        row = (top+(bot-top)//2)
        l,r=0,cols-1
        while l<=r:
            midCol=l+((r-l)//2)
            if target>matrix[row][midCol]:
                l=midCol+1
            elif target<matrix[row][midCol]:
                r=midCol-1
            else:
                return True
        return False

       
            