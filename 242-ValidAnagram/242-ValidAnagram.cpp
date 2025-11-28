// Last updated: 28/11/2025, 13:48:02
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        if(s == t){
            return true;
        }
        return false;
    }
};