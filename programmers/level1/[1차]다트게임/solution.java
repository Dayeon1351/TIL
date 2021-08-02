class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        
        String[] str = dartResult.split("");
        int[] result = new int[3];
        
        int num = 0;
        int idx = 0;
        
        for(int i =0;i<str.length;i++){
            switch(str[i]){
                case "S":
                    num = (int)Math.pow(num,1);
                    result[idx++] = num;
                    break;
                case "D":
                    num = (int)Math.pow(num,2);
                    result[idx++] = num;
                    break;
                case "T":
                    num = (int)Math.pow(num,3);
                    result[idx++] = num;
                    break;
                case "#":
                    result[idx-1]*=-1;
                    break;
                case "*":
                    result[idx-1]*=2;
                    if(idx-2>=0){
                        result[idx-2]*=2;
                    }
                    break;
                default:
                    if(i!=0&&str[i].equals("0")&&str[i-1].equals("1")){
                        num = 10;
                    }else{
                        num = Integer.parseInt(str[i]);    
                    }    
                    break;
            }
        }
        
        for(int n : result){
            answer+=n;
        }
        
        return answer;
    }
}
