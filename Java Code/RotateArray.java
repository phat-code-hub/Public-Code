import java.util.Arrays;

public class RotateArray {
    public static void main(String[] args) {
        int[] nums ={1,2,3,4,5,6,7};
        int k=3;
        int[] arr1 = Arrays.copyOfRange(nums, (nums.length-k), nums.length);
        // for(var n:arr1) System.out.println(n);
        int[] arr2 = Arrays.copyOf(nums, (nums.length-k));
        for(var n:arr2) System.out.println(n);
        int j=0;
        // int lim = nums.length-k;
        for (int i=0;i<nums.length;i++){

            // if (i<(nums.length-k)){
            if (i<k){
                nums[i] = arr1[j++];
            } else { 
                // System.out.println(j);
                // nums[i] = arr2[(nums.length-k)-(j--)];
            }
        }
        for (j=0;j<k;j++) System.out.println(nums[j]);
        // for (var n:nums) System.out.println(n);
    }
}
