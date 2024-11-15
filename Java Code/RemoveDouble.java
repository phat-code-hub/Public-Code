import java.util.*;

public class RemoveDouble {
    public static void main(String[] args) {
        int[] nums =  {0,0,1,1,1,2,2,3,3,4,5};
        // int[] nums =  {1,1,2};
        List<Integer> expectedNums =new ArrayList<>();
        for(var n:nums) {
            if(!expectedNums.contains(n))
                expectedNums.add(n);
        }
        // nums =expectedNums.stream().mapToInt(Integer::intValue).toArray();
        int i=0;
        for (var n:expectedNums) nums[i++] = n;
        for (i=0;i<expectedNums.size();i++) System.out.println(nums[i]);
    } 
}
