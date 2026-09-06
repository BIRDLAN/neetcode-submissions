# Time: O(n), space: O(n), n = length of s 
class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        for c in s:
            if c in ["(", "{", "["]:
                q.append(c)
                continue
            if not q:
                return False
            pop_element = q.pop()
            if c == ")":
                if pop_element != '(':
                    return False
            elif c == "}":
                if pop_element != '{':
                    return False
            else:
                if pop_element != '[':
                    return False
        
        return len(q) == 0

                
                
