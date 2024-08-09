function solution(people, limit) {
    var answer = 0;
    people.sort((a, b) => a - b);
    let [start, end] = [0, people.length-1];
    while(start < end) {
        if(people[start] + people[end] <= limit) {
            start += 1;
        }
        answer += 1;
        end -= 1;
    }
    if(start == end) answer += 1;
    return answer;
}