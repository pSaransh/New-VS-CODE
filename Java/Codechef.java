import java.util.*;
/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		String s1 = "ab.dr.h.yhi.i.e";
		String[] res = s1.split("\\.");
		System.out.println("Hii");
		System.out.println(res.length);
		for (int i = 0; i < res.length; i++) {
			System.out.println(res[i]);
		}
		sc.close();
	}
}