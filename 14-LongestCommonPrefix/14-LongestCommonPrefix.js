// Last updated: 24/11/2025, 17:27:27
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    let prefix = "";
    for (let i = 0; i < strs[0].length; i++) {
        if(strs.every(str => str[i] === strs[0][i])){ 
            prefix += strs[0][i];
        }else {
            break;
        }
    }
    return prefix;
};