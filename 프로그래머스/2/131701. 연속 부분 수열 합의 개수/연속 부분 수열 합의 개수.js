function solution(elements) {
    const set = new Set();
    elements.forEach((e) => set.add(e));
    for(let i = 1; i < elements.length; i++) {
        let start = 0, end = start + i;
        const first = start;
        let sum = 0;
        for(let j = start; j <= end; j++) {
            sum += elements[j];
        }
        set.add(sum);
        while(true) {
            sum -= elements[start%elements.length];
            start += 1;
            end += 1;
            if(start%elements.length == first) break;
            sum += elements[end%elements.length];
            set.add(sum);
        }   
    }
    return set.size;
}