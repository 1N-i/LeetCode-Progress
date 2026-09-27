var isPalindrome = function(s) {
    let textFixed = s.replace(/[^a-zA-Z0-9]/g, "")
    textFixed = textFixed.toLowerCase()
    const textReversed = textFixed.split("").reverse().join("")

    return textFixed === textReversed
};