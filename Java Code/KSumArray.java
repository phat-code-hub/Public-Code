import java.util.*;
public class KSumArray {
    public static void main(String[] args) {
        int[] nums = {7,4,3,9,1,8,5,2,6}; 
        int k = 3;
        int n= nums.length; 
        int limit= 2*k+1;
        int[] res =new int[nums.length];
        Arrays.fill(res,-1);
        // if (limit>k) return res;
        int sums =0;
        for (int i=0;i<limit;i++){
            sums += nums[i];
        }
        res[k] =(int) Math.floor(sums/limit);
        for (int i=k+1;i< n-k;i++){
            sums -= nums[i-k-1];
            sums += nums[i+k];
            res[i] =(int) Math.floor( sums/limit);
        }
        for (int m:res) {
            System.out.print(m+",");
        }
    }
}
