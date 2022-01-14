#include<stdio.h>
#include<math.h>
int main(){
	int n;
	printf("Enter the integer you have in mind: ");
	scanf("%d",&n);
	int nC = ceil(n/2);
	for(int i=0; i<n;i++)
	{
		for(int j=0; j<2*n-1; j++)
		{
			print(nC+" ");
		}
	}
	return 0;
}

