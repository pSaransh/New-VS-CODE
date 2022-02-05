package Java;

/**
 * Solution
**/
class Solution{
    private String name;
    private int id;
    private String city;
    Solution(String city){
        this.city = city;
    }
    Solution(String name, int id){
        this.name = name;
        this.id = id;
    }
    public static void main(String[] args) {
        Solution e1 = new Solution("NYC");
        Solution e2 = new Solution("Victor Karel",2345);
        System.out.println(e1.name+" "+e1.city+" "+e1.id);
        System.out.println(e2.name+" "+e2.city+" "+e2.id);
    }
}