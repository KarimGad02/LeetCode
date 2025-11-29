var isValid = function (s) {
    const closingBrackets = {
        "(": ")",
        "{": "}",
        "[": "]",
    };

    const openingBrackets = [];

    for (const bracket of s) {
        if (bracket in closingBrackets) {
            openingBrackets.push(bracket);
        }
        else if (closingBrackets[openingBrackets.pop()] !== bracket) {
            return false;
        }
    }
    return openingBrackets.length === 0;
};