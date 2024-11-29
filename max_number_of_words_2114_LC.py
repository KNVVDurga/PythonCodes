"""2114. Maximum Number of Words Found in Sentences
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in a single sentence."""

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans=0
        l = len(sentences)
        for i in range(l):
            sum=1
            for j in sentences[i] :
                if (j == " "):
                    sum = sum+1
            ans = max(ans, sum)
        return ans    
