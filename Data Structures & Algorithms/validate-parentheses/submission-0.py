class Solution:
    def isValid(self, s: str) -> bool:
        str_stack = []
        par = {')': '(', ']': '[', '}': '{'}

        for i in s:
            # If it's a closing bracket
            if i in par:
                # Stack must not be empty, and top must match
                if not str_stack or str_stack[-1] != par[i]:
                    return False
                str_stack.pop()

            # If it's an opening bracket
            else:
                str_stack.append(i)

        # Valid only if nothing is left in the stack
        return not str_stack


s = Solution()
print(s.isValid('()[]{}'))