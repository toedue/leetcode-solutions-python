class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for j in range (4):

            if mat == target:
                return True

            left, right = 0, len(mat)-1

            while (left < right):
                for i in range (right - left):
                    top, bottom = left , right
                    # first store thr top left to a temp variable
                    topleft = mat [top][left+i]

                    mat[top][left+i] = mat[bottom-i][left]

                    mat[bottom-i][left] = mat[bottom][right-i]

                    mat[bottom][right-i] = mat[top+i][right]

                    mat[top+i][right]= topleft

                left+=1
                right-=1

        return (mat == target)


