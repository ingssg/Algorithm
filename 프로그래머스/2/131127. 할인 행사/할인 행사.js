function solution(want, number, discount) {
    const dict = {};
    const predict = {};
    let ans = 0;
    for (let i = 0; i < want.length; i ++) {
        predict[want[i]] = number[i];
    }
    let start = 0; end = start + 9;
    for(let i = start; i <= end; i++) {
        dict[discount[i]] ? dict[discount[i]] += 1 : dict[discount[i]] = 1;
    }
    while(true) {
        if(isOk(dict, predict)) {
            ans += 1;
        }
        dict[discount[start]] -= 1;
        start += 1;
        end += 1;
        if(end == discount.length) break;
        dict[discount[end]] ? dict[discount[end]] += 1 : dict[discount[end]] = 1;
    }
    return ans;
}
    
const isOk = (dict, predict) => {
    for(let [key, value] of Object.entries(predict)) {
        if(!dict[key] || dict[key] < value) return false;
    }
    return true;
}