function solution(n, words) {
    const set = new Set();
    let round = 1;
    let last = words[0][words[0].length-1];
    set.add(words[0])
    for(let i = 1; i < words.length; i++) {
        if(i % n == 0) round += 1;
        let setCnt = set.size;
        set.add(words[i]);
        if(last != words[i][0] || setCnt == set.size) {
            return [(i+1)%n > 0 ? (i+1)%n : n, round];
        }
        last = words[i][words[i].length-1];
    }
    return [0, 0];
}