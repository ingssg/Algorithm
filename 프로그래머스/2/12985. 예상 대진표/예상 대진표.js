function solution(n,a,b)
{
    let ans = 1;
    if(a > b) {
        [a, b] = [b, a];
    }
    while(b-a != 1 || b % 2 == 1) {
        ans += 1;
        a = Math.ceil(a/2);
        b = Math.ceil(b/2);
    }
    return ans;
}