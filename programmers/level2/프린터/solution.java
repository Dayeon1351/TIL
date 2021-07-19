import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        
        Queue<Integer> list = new LinkedList<>();
        
        for(int n : priorities){
            list.add(n);
        }
        
        while(!list.isEmpty()){
            if(list.peek()<Collections.max(list)){
                location = location==0 ? list.size()-1 : location-1;
                list.add(list.poll());
            }else{
                if(location==0){
                    answer++;
                    break;
                }else{
                    list.poll();
                    location--;
                    answer++;
                }
                
            }
        }
        
        return answer;
    }
}
