class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        istringstream ss(s);
        string word;
        unordered_map<char, string> patternMap;
        int i = 0;
        while (ss >> word) {
            words.push_back(word);
        }
        if (pattern.size() != words.size()) return false;
        for (char c : pattern) {
            if (patternMap.count(c)) {
                if (patternMap[c] != words[i]) return false;
            } else {
                bool valueUsed = false;
                for (const auto& p : patternMap) {
                    if (p.second == words[i]) {
                        valueUsed = true;
                        break;
                    }
                }
                if (valueUsed) return false;
            }
            patternMap[c] = words[i];
            i++;
        }
        return true;
    }
};