function solution(s) {
    var answer = '';
    const numArr = s.split(" ").map(Number);
    answer += (Math.min(...numArr) + " " + Math.max(...numArr));
    return answer;
}