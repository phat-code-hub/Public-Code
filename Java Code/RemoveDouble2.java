public class RemoveDouble2 {
    public static void main(String[] args) {
        int[] nums = {-3,-1,-1,0,1,1,1,2,2,3,4,4};
        nums =new int[]{1,1,2};
        int  index=0;
        for (int i=1;i<nums.length;i++){
            if (nums[i]  != nums[index]) {
                // System.out.print("index="+index+" la "+nums[index]+",");
                nums[++index] = nums[i];
                // System.out.print("index="+index+" la "+nums[index]+",");
            }
        }
        // System.out.println(index);
        for (int i=0;i<=index;i++){
            System.out.println(nums[i]);
        };
    }
}
