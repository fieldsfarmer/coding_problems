class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        res = []
        two_sets = [set(), set()]
        cur, pre = 0,1
        wordlist.add(endWord)
        two_sets[pre].add(beginWord)
        path_dict = collections.defaultdict(list)
        l = len(beginWord)
        while True:
            for w in two_sets[pre]:
                wordlist.remove(w)
            for w in two_sets[pre]:
                for i in range(l):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        new_w = w[:i]+j+w[i+1:]
                        if new_w in wordlist:
                            two_sets[cur].add(new_w)
                            path_dict[new_w].append(w)
                        if new_w == endWord:
                            break
            pre, cur = cur, pre
            two_sets[cur].clear()
            if len(two_sets[pre])==0: return res
            if endWord in two_sets[pre]: break
        self.build(res, path_dict, endWord, [])
        return res
        
    def build(self, res, path_dict, endWord, t):
        if len(path_dict[endWord])==0:
            t.append(endWord)
            u = list(t)
            u.reverse()
            res.append(u)
            t.pop()
            return
        t.append(endWord)
        for w in path_dict[endWord]:
            self.build(res,path_dict, w, t)
        t.pop()
        
        
        
def main():
    s = Solution()
    print s.findLadders('a', 'c', set(["a","b","c"]))
        