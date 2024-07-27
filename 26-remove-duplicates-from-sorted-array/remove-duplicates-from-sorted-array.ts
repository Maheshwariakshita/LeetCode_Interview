function removeDuplicates(nums: number[]): number {
    let j=0
    for (let i=0; i<nums.length-1;i++){
        if(nums[i]!==nums[i+1]){
            nums[j++]=nums[i]
            
        }
    }
    nums[j++]=nums[nums.length-1]
    return j

};