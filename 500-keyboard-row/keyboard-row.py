class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 =['q','w','e','r','t','y','u','i','o','p']
        row2 = ['a','s','d','f','g','h','j','k','l']
        row3 = ['z','x','c','v','b','n','m',]
        rows =[row1,row2,row3]
        output=[]


        for word in words:
            for row in rows:
                if word[0].lower() in row:
                    result_row = row
                    break
    

            in_row = True

            for char in word:
                if char.lower() not in result_row:
                    in_row = False
                    break

            if in_row:
                output.append(word)

        return output
        