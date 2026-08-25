class Solution(object):
    def reverseWords(self, s):
        words=[]
        word=""
        for ch in s:
            if ch!=" ":
                word+=ch
            else:
                if word!="":
                    words.append(word)
                    word=""

        if word!="":
            words.append(word)

        words.reverse()

        return " ".join(words)  


        #  words= s.split()
        # words.reverse()
        # return " ".join(words)                  
        