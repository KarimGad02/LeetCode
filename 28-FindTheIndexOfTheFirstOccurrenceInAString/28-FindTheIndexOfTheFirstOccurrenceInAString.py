# Last updated: 24/11/2025, 17:27:21
class Solution:
    def strStr(self, haystack, needle):
        haystack=[char for char in haystack]
        needle=[char for char in needle]
        l=0
        r=1
        i=0
        j=1
        if len(haystack)==0:
            return -1
        elif len(haystack)==1 and len(needle)==1:
            if haystack[0]==needle[0]:
                return 0
            else:
                return -1
        elif len(needle)==1:
            for i in range(len(haystack)):
                if haystack[i]==needle[0]:
                    return i
            return -1
        elif len(needle)>len(haystack):
            return -1
        else:
            while j<len(needle):
                if l==len(haystack) or r>=len(haystack):
                    return -1
                elif haystack[l]==needle[i] and haystack[r]==needle[j]:
                    r+=1
                    j+=1
                else:
                    l+=1
                    r=l+1
                    i=0
                    j=1
            return l