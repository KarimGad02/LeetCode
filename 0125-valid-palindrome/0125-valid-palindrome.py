class Solution:
    def isPalindrome(self, s):
        alnum = ''.join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(alnum)-1
        while l < r:
            if alnum[l] != alnum[r]:
                return False
            l += 1
            r -= 1
        return True