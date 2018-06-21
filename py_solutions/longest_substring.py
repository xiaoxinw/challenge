# coding: utf-8

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from collections import OrderedDict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        max_norepeate  = 1
        left = 0
        current_len = 0
        container = {}
        for i in range(0, len(s)):
            if (s[i] not in container) or (container[s[i]] < left):
                container[s[i]] = i
                current_len += 1
            else:
                current_len = i - left
                left = container[s[i]] + 1
                container[s[i]] = i
                max_norepeate = current_len if current_len > max_norepeate else max_norepeate

                current_len = i - left + 1
        
        return current_len if current_len > max_norepeate else max_norepeate
    

if __name__ == "__main__":
    s = Solution()
    # test_str = 'aabcabcbbbcabc'
    test_str = 'pwwkew'
    print(test_str)
    ans = s.lengthOfLongestSubstring(test_str)
    print(ans)