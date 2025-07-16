class Solution:
    def sortSentence(self, s: str) -> str:
       arr = s.split()
       sentence = []

       for i in range(1,len(arr)+1):
            for word in arr:
                if i == int(word[-1]):
                    sentence.append(word[:-1])

       return (" ".join(sentence))
        