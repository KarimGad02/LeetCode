class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        const int rows=strs[0].size();
        int deletes=0;
        for(int j=0; j<rows; j++){
            for (int i=0; i<strs.size()-1; i++){
                if(strs[i][j]>strs[i+1][j]){
                    deletes++;
                    break;
                }
            }
        }
        return deletes;
    }
};