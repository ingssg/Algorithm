const countOne = (num) => {
    let cnt = 0;
    Array.from(num.toString(2)).forEach((e) => {
        if(e == 1) cnt += 1;
    })
    return cnt;
}

function solution(n) {
    var answer = 0;
    let curNum = n+1;
    const countOneN = countOne(n);
    while(true) {
        if(countOne(curNum) == countOneN) {
            answer = curNum;
            break;
        }
        curNum += 1;
    }
    return answer;
}