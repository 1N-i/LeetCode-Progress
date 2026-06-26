var isPalindrome = function(s) {
    const textFixed = s.replace(/[^a-zA-Z0-9]/g, "")
    const textReversed = textFixed.split("").reverse().join("")

    return textFixed.toLowerCase() === textReversed.toLowerCase()
};