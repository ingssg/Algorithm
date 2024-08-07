const func = (str) => {
  let newS = "";
  let numS = Number(str);
  while(numS > 0) {
      newS += numS%2;
      numS = Math.floor(numS/2);
  }
  return newS;
}


function solution(s) {
  var answer = [];
  let zeroC = 0;
  let cnt = 0;
  
  while(s.length != 1) {
      s = s.split("").filter(e => {
          if(e == 0) {
              zeroC += 1;
              return false;
          }
          return true;
      }).join("");
      s = func(s.length.toString());
      cnt += 1;
  }
  answer.push(cnt);
  answer.push(zeroC)
  return answer;
}
