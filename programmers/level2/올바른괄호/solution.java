import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        for(int i =0;i<s.length();i++){
            char c = s.charAt(i);
            if(c==')'){
                if(stack.empty()){
                    answer = false;
                    break;
                }
                stack.pop();
            }else{
                stack.push(c);
            }
        }
        if(!stack.empty()){
            answer = false;
        }        
        return answer;
    }
}
