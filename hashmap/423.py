class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        hm = {}
        hm['0'] = count['z']
        hm['2'] = count['w']
        hm['4'] = count['u']
        hm['6'] = count['x']
        hm['8'] = count['g']
        hm['3'] = count['h'] - hm['8']
        hm['5'] = count['f'] - hm['4']
        hm['7'] = count['s'] - hm['6']
        hm['9'] = count['i'] - hm['5'] - hm['6'] - hm['8']
        hm['1'] = count['o'] - hm['0'] - hm['2'] - hm['4']
        result = [key * hm[key] for key in sorted(hm.keys())]
        return "".join(result)