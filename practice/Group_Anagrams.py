"Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]"


from collections import defaultdict

def groupAnagrams(strs):
    mp = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        mp[key].append(word)

    return list(mp.values())
