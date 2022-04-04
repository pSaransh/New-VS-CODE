class LeetCode26{
    public static void main(String[] args) {
        int[] nums = {0,0,1,1,1,2,2,3,3,4};
        int s = new LeetCode26().removeDuplicates(nums);
        for (int i = 0; i < s; i++) {
            System.out.print(nums[i]+" ");
        }
    }
    public int removeDuplicates(int[] nums) {
        int j=1,i=0;
        for(i = 0; i < nums.length-1; i++){    
            if(nums[i]==nums[i+1]){
                nums[j++]=nums[i+1];
            }
        }
        return j;
    }
}