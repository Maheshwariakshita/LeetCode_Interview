class Solution {
    public double findMaxAverage(int[] nums, int k) {
        if( nums.length==0 || nums==null){
            return 0;
        }
        if (nums.length<k){
            return 0;
        }
        int maxi_s=0;
        int n=nums.length;
        for (int i=0; i<k;i++){
            maxi_s+=nums[i];
        }
        int curr_s=maxi_s;
        for(int j=k; j<n;j++){
            curr_s+=nums[j]-nums[j-k];
            maxi_s=Math.max(maxi_s,curr_s);
        }
        return maxi_s/(double)k;
    }
}