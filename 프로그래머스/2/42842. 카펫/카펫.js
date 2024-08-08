function solution(brown, yellow) {
    var answer = [];
    const sum = brown + yellow;
    for(let c = sum - 1; c > 0; c--) {
        let r = sum / c;
        if(!Number.isInteger(r)) continue;
        if((c-2) * (r-2) == yellow) {
            answer.push(c, r);
            break;
        }
    }
    return answer;
}