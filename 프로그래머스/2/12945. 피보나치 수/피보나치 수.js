function solution(n) {
    var answer = 0;
    const dp = new Array(n+1).fill(0);
    dp[1] = 1;
    dp[2] = 1;
    for(let i = 3; i < n+1; i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
    }
    answer = dp[n];
    return answer;
}