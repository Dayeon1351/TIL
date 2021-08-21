import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        HashMap<Integer,Integer> hm = new HashMap<>();
        hm.put(0,0);
      
        for(Integer i : stages){
            hm.put(i,hm.getOrDefault(i,0)+1);
        }
        
        int num = stages.length;
        HashMap<Integer,Double> result = new HashMap<>();
      
        for(int i =0;i<N;i++){
            num-=hm.getOrDefault(i,0);
            result.put(i+1,(double)hm.getOrDefault(i+1,0)/num);
            if(Double.isNaN(result.get(i+1))){
                result.put(i+1,0.0);
            }
        }
         
        
        List<Integer> keySetList = new ArrayList<>(result.keySet());
        Collections.sort(keySetList,(o1,o2)->(result.get(o2).compareTo(result.get(o1))));
        
        int index = 0;
        for(Integer key : keySetList){
            answer[index++]= key;
        }
        
        
        return answer;
    }
}
