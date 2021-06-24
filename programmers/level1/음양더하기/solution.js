function solution(absolutes, signs) {
    var answer = 0;
    
  // 방법1
    absolutes.forEach((val,idx)=>answer+= signs[idx] ? val : -val);
    
  // 방법2
//     answer = absolutes.reduce((pre,val,idx)=>{
//       //console.log(pre,val,idx);
//       return pre + (signs[idx] ? val : -val);
//     },0);
    
    // answer = absolutes.reduce((pre,val,idx)=>pre + (signs[idx] ? val : -val),0);   // 함수의 body 부분이 1줄일 경우 {}을 생략 할 수 있다. 그리고 그 1줄은 암묵적인 반환값
    
  return answer;
}
