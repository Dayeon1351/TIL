class Solution {
    public int solution(int n) {
        int answer = 0;
        int f0 = 0;
        int f1 = 1;
        for(int i = 0;i<n-1;i++){
            answer = (f0+f1)%1234567;
            f0 = f1%1234567;
            f1 = answer%1234567;
        }
        return answer;
    }
}
