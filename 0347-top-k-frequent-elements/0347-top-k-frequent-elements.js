var topKFrequent = function(nums, k) {
    const frequencyMap = {};
    for (const num of nums) {
        frequencyMap[num] = (frequencyMap[num] || 0) + 1;
    }
    
    const frequencyArray = Object.entries(frequencyMap);
    frequencyArray.sort((a, b) => b[1] - a[1]);
    return frequencyArray.map(entry => Number(entry[0])).slice(0, k);
};