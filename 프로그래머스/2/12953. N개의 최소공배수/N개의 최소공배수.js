const gcd = (a, b) => {
    while(b != 0) {
        let temp = b;
        b = a%b;
        a = temp;
    }
    return a;
}

const lcm = (a, b) => {
    return (a*b) / gcd(a, b);
}

function solution(arr) {
    if(arr.length === 1) return arr[0];
    return arr.reduce((rst, cur) => lcm(rst, cur));
}
