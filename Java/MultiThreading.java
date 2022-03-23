//import java.io.IOError;
import java.io.IOException;

/**
 * MultiThreading
 */
public class MultiThreading  extends Thread {
    
    public static void main(String[] args) throws IOException {
        MultiThreading t1 = new MultiThreading();
        MultiThreading t2 = new MultiThreading();
        System.out.println(t1.getId()+" "+t2.getId());
        t1.start();
        t2.start();
        

    }
    public synchronized void run(){  
        for(int i=1;i<10;i++){  
          try{
      Thread.sleep(500);
      }catch(InterruptedException e){System.out.println(e);}  
          if(Thread.currentThread().getName().equals("Thread-1"))
            System.out.println("Three: "+ 3*i);
          else{
              System.out.println("Five "+ 5*i);
          }
        }  
       }  
      
}