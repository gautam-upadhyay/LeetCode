class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        a = ""

        for i in s:
            if i.isalnum():
                # a.append(i.lower()) 
                a += i.lower()
        return a == a[::-1]