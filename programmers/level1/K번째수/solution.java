import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        
        for(int i = 0;i<answer.length;i++){
            int[] temp = Arrays.copyOfRange(array,commands[i][0]-1,commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
             
        }
        
//         for(int i =0; i<answer.length;i++){
//             start = commands[i][0];
//             end = commands[i][1];
//             size = end - start + 1;
//             temp = new int[size];
            
//             if(size == 1){
//                 answer[i] = array[start-1];
//             }else{
                
//             int k =0;
//             for(int j = start-1;j<end;j++){
//                 temp[k] = array[j];
//                 k++;
//             }
//             Arrays.sort(temp);
//             answer[i]=temp[commands[i][2]-1];
//             }
            
//         }
        
        return answer;
    }
}
