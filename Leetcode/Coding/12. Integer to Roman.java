class Solution {
     //Returns 1 based roman. The pos tells which position digit Roman we need.
    private String getOneRoman(int pos){
        switch(pos){
            case 1: return "I";
            case 2: return "X";
            case 3: return "C";
            case 4: return "M";
        }
        return "";
    }
    //Returns 5 based roman. The pos tells which position digit Roman we need
    private String getFiveRoman(int pos){
        switch(pos){
            case 1: return "V";
            case 2: return "L";
            case 3: return "D";
        }
        return "";//nothing 

    }
    //Get the roman based on the val and position.
    private String getRoman(int val,int pos){
        String roman = "";
        if(val <= 5){
            if(val == 4) roman += getOneRoman(pos) + getFiveRoman(pos);
            if(val < 4) roman += getOneRoman(pos).repeat(val);
            if(val == 5) roman += getFiveRoman(pos);
        }else{ //val > 5  && <= 9
            if(val > 5 && val < 9){
            roman += getFiveRoman(pos) + getRoman(val-5,pos); //Do recursion to get the value
            }else{
                roman += getOneRoman(pos) + getOneRoman(pos+1);
            }
        }
        return roman;
    }

    public String intToRoman(int num) {
        int val = num;
        int position = 1;
        StringBuilder roman = new StringBuilder("");
        while(val!=0){
            int last_digit = val%10;
            roman.append(","+getRoman(last_digit,position ));
            val = val/10;
            position+=1;
        }        
        String[] arr = roman.toString().split(",");
        String result = "";
        for(int i = arr.length-1;i>=0;i--){
            result+=arr[i];
        }
        System.out.println(result);
        
        return result;
        
    }
}