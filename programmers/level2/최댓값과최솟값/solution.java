import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.split(" ");
        
        int[] nums = Arrays.stream(str).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(nums);
        
        answer = nums[0] + " " + nums[nums.length-1];   
        
        return answer;
    }
}
