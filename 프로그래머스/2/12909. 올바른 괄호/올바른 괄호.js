function solution(s){
    var answer = true;
    const stk = [];
    for (i = 0; i < s.length; i++) {
        if(s[i] == ")") {
            if(stk.length === 0) return false;
            stk.shift();
            continue;
        }
        stk.push(s[i]);        
    }
    if(stk.length > 0) answer = false;
    return answer;
}