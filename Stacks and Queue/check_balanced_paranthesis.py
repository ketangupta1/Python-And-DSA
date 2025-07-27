class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            else:
                if not st:
                    return False
                else:
                    b_ch = st.pop()
                    if ((ch == ')' and b_ch == '(') or
                            (ch == '}' and b_ch == '{') or
                            (ch == ']' and b_ch == '[')):
                        continue
                    else:
                        return False
        if st:
            return False
        return True

