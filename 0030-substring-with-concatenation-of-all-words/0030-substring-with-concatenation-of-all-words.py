class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        w = len(words[0])
        m = len(words)
        n = len(s)

        need = {}
        for word in words:
            need[word] = need.get(word, 0) + 1

        res = []
        for offset in range(w):
            left = offset
            count = 0
            window = {}

            for right in range(offset, n - w + 1, w):
                word = s[right:right + w]

                if word in need:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    # too many of this word: shrink from the left
                    while window[word] > need[word]:
                        left_word = s[left:left + w]
                        window[left_word] -= 1
                        count -= 1
                        left += w

                    if count == m:
                        res.append(left)
                        # slide forward by one word to look for the next match
                        left_word = s[left:left + w]
                        window[left_word] -= 1
                        count -= 1
                        left += w
                else:
                    window = {}
                    count = 0
                    left = right + w

        return res