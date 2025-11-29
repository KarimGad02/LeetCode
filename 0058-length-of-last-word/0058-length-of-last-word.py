class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pointer = len(s)-1
        counter = 0
        pointer2 = 0
        if len(s) == 1:
            counter = 0 if s[pointer] == " " else 1
            return counter
        while pointer >= 0:
            if s[pointer] == " ":
                pointer-=1
            else:
                pointer-=1
                pointer2 = pointer
                counter+=1
                if s[pointer2] == " ":
                    return counter
        return counter