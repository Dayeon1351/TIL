class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int num = 1;
              
        while(!s.equals("1")){
            int len = s.length();
            s = s.replace("0","");
            
            answer[0] = num++;
            answer[1] += len-s.length();
            
            s = Integer.toBinaryString(s.length());
        }
        return answer;
    }
}
