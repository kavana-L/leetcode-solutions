class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        count={}
        max_freq=0
        answer=0
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            max_freq=max(max_freq,count[s[i]])
            if i-left+1-max_freq>k:
                count[s[left]]-=1
                left+=1
            answer=max(answer,i-left+1)
        return answer
        