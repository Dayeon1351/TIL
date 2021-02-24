* 스택  
> LIFO
```Java
Stack<Integer> stack = new Stack<>();
stack.push(1);   
stack.add(1);
stack.pop();      // 가장 맨 위의 값 제거
stack.peek();     // 가장 맨 위의 값 반환
stack.empty();    // 스택이 비어있으면 true 비어있지 않으면 false 반환  
stack.indexOf(1)  // 특정 값의 인덱스 반환
stack.contains(1) // 특정 값이 스택에 있는지 확인
stack.set(인덱스, 값) // 스택 특정 인덱스의 값 변경

```
