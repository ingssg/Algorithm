function solution(s) {
    let ans = 0;
    const test = Array.from(s);
    for(let i = 0; i < s.length; i++) {
        const stk = [];
        let rst = true;
        for(let a of test) {
            if(stk.length == 0) {
                if(a === ']' || a === '}' || a === ')')
                    {
                        rst = false;
                        break;    
                    }
            }
            if(a === ']' && stk[stk.length-1] === '[' || a === '}' && stk[stk.length-1] === '{' || a === ')' && stk[stk.length-1] === '(') {
                stk.pop();
                continue;
            }
            stk.push(a);                
        }
        if(stk.length != 0) {
            rst = false;
        }
        if(rst) ans += 1;
        test.push(test.shift());
    }
    return ans;
}