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
- - -
* Set  
  + 데이터의 중복을 인정하지 않는다.
    - HashSet
    ```JAVA
        HashSet<Integer> hs = new HashSet<>();
        hs.add();
    ```  
  + Iterator
    ```JAVA
      HashSet<Integer> hs = new HashSet<>();
      Iterator it = hs.iterator();
        
        while(it.hasNext()){
            answer[index++] = (int)it.next();
        }
    ```
