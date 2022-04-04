class Solution {
    public int removeElement(int[] nums, int val) {
        int v=0,i=0;
        for(i = 0; i < nums.length; i++){
            if(nums[i]!=val){
                nums[v] = nums[i];
                v+=1;
            }
        }
        return v;
    }
}
