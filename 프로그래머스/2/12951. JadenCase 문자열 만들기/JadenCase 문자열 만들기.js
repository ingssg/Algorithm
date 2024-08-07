function solution(s) {
    var answer = '';
    answer = s.split(" ").map(e => e.charAt(0).toUpperCase() + e.slice(1).toLowerCase()).join(" ");
    return answer;
}