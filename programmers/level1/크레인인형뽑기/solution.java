import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0;i < moves.length;i++){
            for(int j = 0;j < board.length;j++){
                int num = board[j][moves[i]-1];
                if(num != 0){
                    if(!stack.empty()&&num==stack.peek()){
                        stack.pop();
                        answer++;
                        board[j][moves[i]-1] = 0;
                        break;
                    }else{
                        stack.push(num);
                        board[j][moves[i]-1] = 0;
                        break;
                    }
                    
                }
            }
        }
        
        answer*=2;
        return answer;
    }
}
