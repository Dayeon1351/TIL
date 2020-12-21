<img src = "https://t1.daumcdn.net/cfile/tistory/175466144CC11C2755" width = "50%"></img>

* Map  
  + key와 value
    - HashTable  
     > 동기화가 보장된다.
    - HashMap 
    > 동기화가 보장되지 않는다.  
    > data의 순서 없다.  
    > null key, null value 허용한다.  
    > value의 중복은 허용하나 key의 중복은 허용하지 않는다.
    ```JAVA
      HashMap<String,Integer> hm = new HashMap<>();
      hm.put(key,value);
      hm.get(key);
      hm.remove(key);       
      hm.clear();           // public void clear();
      hm.isEmpty();         // public boolean isEmpty();
    ```  
    ---  
    
    > 중복된 숫자의 개수 세기
    ```Java
     HashMap<Integer,Integer> hm = new HashMap<>();
        for(Integer i : stages){
            hm.put(i,hm.getOrDefault(i,0)+1);
        }
     ``` 
     ---
   + 정렬  
      - 오름차순  
      ```Java
      HashMap<Integer,Double> result = new HashMap<>();
      List<Integer> keySetList = new ArrayList<>(result.keySet());
      Collections.sort(keySetList,(o1,o2)->(result.get(o1).compareTo(result.get(o2))));
      ```
      - 내림차순
      ```Java
      HashMap<Integer,Double> result = new HashMap<>();
      List<Integer> keySetList = new ArrayList<>(result.keySet());
      Collections.sort(keySetList,(o1,o2)->(result.get(o2).compareTo(result.get(o1))));
      ```
- - -
* Set  
  + 데이터의 중복을 인정하지 않는다. 자동 제거해준다.
    - HashSet  
    > 값들을 자동정렬 해주지 않는다.
    ```JAVA
        HashSet<Integer> hs = new HashSet<>();
        hs.add();
    ```  
    - TreeSet  
    > 이진탐색 트리구조  
    > <값이 추가되는 과정>  
    > <img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FSXQBD%2FbtqEtE5Opsm%2FTyuNWSDe5kDxDoueaNQjsK%2Fimg.png" width = "50%"></img>  
    > 값들을 자동정렬 해준다.  
    
  + Iterator
    ```JAVA
      HashSet<Integer> hs = new HashSet<>();
      Iterator it = hs.iterator();
        
        while(it.hasNext()){
            answer[index++] = (int)it.next();
        }
    ```
