class Solution {
    public int findMaxConsecutiveOnes(int[] arr) {
        int maxi_c=0;
        int curr_c=0;
        for (int i=0;i<arr.length;i++){
            if (arr[i]==1){
                curr_c+=1;
            }
            else{
                curr_c=0;
            }
            maxi_c=Math.max(curr_c,maxi_c);
        }
        return maxi_c;











        // if (arr==null || arr.length==0){
        //     return 0;
        // }
        // int maxi=0;
        // int curr_c=0;
        // int n=arr.length;
        // for (int i=0; i<n;i++){
        //     if (arr[i]==1){
        //         curr_c+=1;
        //     }
        //     else {
        //         curr_c=0;
        //     }
        //     maxi=Math.max(maxi, curr_c);

        // }
        // return maxi;
    }
}