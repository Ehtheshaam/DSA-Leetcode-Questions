class Solution:

    def wordBreak(self, s, wordDict):

        dict_set = set(wordDict)
        memo = {}

        return self.backtrack(s, 0, dict_set, memo)

    def backtrack(self, s, start, dict_set, memo):

        # Reached the end
        if start == len(s):
            return [""]

        # Already calculated
        if start in memo:
            return memo[start]

        result = []

        # Try every possible word
        for end in range(start + 1, len(s) + 1):

            word = s[start:end]

            # If word exists in dictionary
            if word in dict_set:

                remaining = self.backtrack(
                    s, end, dict_set, memo
                )

                # Add word to every possible sentence
                for sentence in remaining:

                    if sentence == "":
                        result.append(word)
                    else:
                        result.append(word + " " + sentence)

        # Store result
        memo[start] = result

        return result
        