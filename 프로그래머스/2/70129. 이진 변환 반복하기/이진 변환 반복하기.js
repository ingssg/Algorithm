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
      s = s.length.toString(2);
      cnt += 1;
  }
  answer.push(cnt);
  answer.push(zeroC)
  return answer;
}
