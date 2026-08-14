class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need_count={}
        for char in t:
            need_count[char]=need_count.get(char,0)+1
        count={}
        left=0
        have=0
        need=len(need_count)
        answer=""
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            if s[right] in need_count:
                if count[s[right]]==need_count[s[right]]:
                    have+=1
            while have==need:
                if answer=="" or right - left+1<len(answer):
                    answer=s[left:right+1]
                count[s[left]]-=1
                if s[left] in need_count:
                    if count[s[left]]<need_count[s[left]]:
                        have-=1
                left+=1
        return answer
        