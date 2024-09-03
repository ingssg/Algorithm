function solution(k, tangerine) {
    const tMap = new Map();
    tangerine.forEach((e) => {
        if(tMap.has(e)) {
            tMap.set(e, tMap.get(e) + 1);
            return;
        }
        tMap.set(e, 1);
    })
    const tArr = Array.from(tMap).sort((a, b) => b[1] - a[1]);
    let i = 0;
    while(k > 0) {
        k -= tArr[i][1]
        i += 1;
    }
    return i;
}