function solution(n)
{
    var ans = 0;
    ans = n.toString(2).match(/1/g).length;

    return ans;
}