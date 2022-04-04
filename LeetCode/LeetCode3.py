class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = [i for i in s]
        l = list(set(l))
        l.sort()
        return len(l)

s = Solution()
s.lengthOfLongestSubstring("abcabcbb")