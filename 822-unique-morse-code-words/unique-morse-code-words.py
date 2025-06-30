class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
        "..-","...-",".--","-..-","-.--","--.."]

        
        unique_transformation = []


        for word in words:
            morse_word= ""
            for char in word:
                morse_word += morse_code[ord(char)-97]
            if morse_word not in unique_transformation:
                unique_transformation.append(morse_word)
        return (len(unique_transformation))
            



        