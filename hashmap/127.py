class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        all_combo_dict = collections.defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                inter_word = word[:i] + '*' + word[i+1:]
                all_combo_dict[inter_word].append(word)
        level = 1
        queue = collections.deque([(beginWord, level)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(L):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                # all_combo_dict[intermediate_word] = []
        return 0