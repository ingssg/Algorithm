function solution(s)
{
    var answer = 0;
    const stk = [];
    stk.push(s[0]);
    console.log(stk)
    for(let i = 1; i < s.length; i++) {
        if(stk[stk.length-1] == s[i]) {
            stk.pop();
            continue;
        }
        stk.push(s[i]);
    }
    if(stk.length == 0) answer = 1;

    return answer;
}