class Solution(object):
    def isValid(self, s):
        map = {"}":"{","]":"[",")":"("}
        stack = []

        if len(s)%2 != 0 :
            return False

        for i in s:
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            
            else :
                stack.append(i)

        if stack :
            return False

        return True
                    
sol = Solution()
value = "(({[]})[])"

print(sol.isValid(value))