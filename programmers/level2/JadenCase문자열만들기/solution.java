class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.split("",-1);
        
        for(String ss : str){
            if(answer.length()==0||answer.charAt(answer.length()-1)==' '){
                answer+=ss.toUpperCase();
            }else{
                answer+=ss.toLowerCase();
            }
        }
        
        return answer;
    }
}
