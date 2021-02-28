- Queue 
> 인덱스 사용 불가능
```Java
Queue<Integer> que = new Queue<>();
Queue<Integer> que = new LinkedList<>();
PriorityQueue<Integer> que = new PriorityQueue<>();   // 값을 자동정렬해준다. 
que.add(1);
que.offer(1);
que.indexOf(1);             //해당값의 인덱스가 없을 때 -1 반환
que.contains(1);            //해당값을 포함하고 있으면 true 아니면 false 반환
```
- LinkedList
> 인덱스 사용 가능
```Java
LinkedList<Integer> list = new LinkedList<>();
list.add(1);
list.get(0);    // 인덱스 0의 값 반환 -> 1출력 
list.set(0,3);  // 인덱스 0의 값을 3으로 변경
```
