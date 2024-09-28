class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        compare = []
        count = 0
        idx = 0

        while idx < len(haystack):
            
            if (haystack[idx] == needle[count]):
                compare.append(haystack[idx])
                count += 1
            else:
                if count > 0:
                    idx = idx - count
                count = 0
                compare = []


            if (len(compare) == len(needle)):
                return idx + 1 - len(needle)
        
            idx += 1

        return -1
        