// import java.util.*;
// public class TicTacToe{
//     public static void main(String[] args) {
//         System.out.println("Welcome to the game");
//         boolean res= false,flag = true;
//         Scanner sc = new Scanner(System.in);
//         int[] crossPos = new int[9];
//         int[] zeroPos = new int[9];
//         int i=0,j=0;
//         //String n = new String();
//         System.out.println("Enter -1 to exit");
//         while(true){
//             if(flag){
//                 System.out.println("Enter the position of X between 1-9.");
//                 int crossSinglePos = sc.nextInt();
//                 if(crossSinglePos==-1) break;
//                 if(new TicTacToe().checkReservedPosition(crossSinglePos, crossPos, zeroPos)){
//                     System.out.println("No Cheating. X Lost.");
//                     break;
//                 }
//                 crossPos[i] = crossSinglePos;
//                 res = new TicTacToe().checkForWin(crossPos);
//                 if(res){
//                     System.out.println("X wins");
//                     break;
//                 }
//                 i+=1;
//                 flag = false;
//             }
//             else{
//                 System.out.println("Enter the position of O between 1-9.");
//                 int zeroSinglePos = sc.nextInt();
//                 if(zeroSinglePos==-1) break;
//                 if(new TicTacToe().checkReservedPosition(zeroSinglePos, crossPos, zeroPos)){
//                     System.out.println("No Cheating. O Lost.");
//                     break;
//                 }
//                 zeroPos[j] = zeroSinglePos;
//                 res = new TicTacToe().checkForWin(zeroPos);
//                 if(res){
//                     System.out.println("O wins");
//                     break;
//                 }
//                 j+=1;
//                 flag = true;
//             }
//         }
//         sc.close();
//     }
//     public boolean checkReservedPosition(int num,int[] arr1, int[] arr2){
//         for (int i = 0; i < arr1.length; i++) {
//             if(num==arr1[i]) return true;
//             if(num==arr2[i]) return true;
//         }
//         return false;
//     }
//     public boolean checkForWin(int[] arr){
//         for(int i = 0; arr[i] != 0;){
//             if(arr[i]==1 && arr[i+1]==2 && arr[i+2]==3) return true;
//             if(arr[i]==4 && arr[i+1]==5 && arr[i+2]==6) return true;
//             if(arr[i]==7 && arr[i+1]==8 && arr[i+2]==9) return true;
//             if(arr[i]==9 && arr[i+1]==6 && arr[i+2]==3) return true;
//             if(arr[i]==5 && arr[i+1]==2 && arr[i+2]==8) return true;
//             if(arr[i]==1 && arr[i+1]==4 && arr[i+2]==7) return true;
//             if(arr[i]==1 && arr[i+1]==5 && arr[i+2]==9) return true;
//             if(arr[i]==7 && arr[i+1]==5 && arr[i+2]==3) return true;
//             i+=1;

//         }
//         return false;
//     }
// }


/**
 * TicTacToe
 */
@FunctionalInterface
interface A{
    void print();
}
public class TicTacToe {
    public static void main(String[] args) {
        A obj = () -> System.out.println("Hello");
        obj.print();
    }
}