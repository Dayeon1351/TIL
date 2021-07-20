import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        int num = 0;
        LinkedList<Integer> que = new LinkedList<>();
        LinkedList<Integer> spd = new LinkedList<>();
        
        for(Integer n : progresses){
            que.add(n);
        }
        for(Integer n : speeds){
            spd.add(n);
        }
        
        while(!que.isEmpty()){
            for(int i = 0;i<que.size();i++){
                que.set(i,que.get(i)+spd.get(i));
            }
            while(!que.isEmpty()&&que.peek()>=100){
                    que.poll();
                    spd.poll();
                    num++;
            }
            if(num!=0){
                spd.add(num);
            }
            num = 0;        
        }
        answer = new int[spd.size()];
        int idx = 0;
        for(Integer n : spd){
            answer[idx++]=n;
        }
        
        return answer;
    }
}
