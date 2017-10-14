#include "victory.hpp"


#include<cstdio>
#include<cstdlib>
#include<cmath>

int main()
{
	long long a,b,c,d;
	printf("Quadratic equation solver!\n");
	printf("ax^2+bx+c=0, a!=0\n");
	printf("Enter a: ");
	scanf("%lld",&a);
	printf("Enter b: ");
	scanf("%lld",&b);
	printf("Enter c: ");
	scanf("%lld",&c);
	
	printf("Finished");
	if(a==0)
	{
		printf("Idiot!!! a != 0 !!!\n"); // You fail :(
		return 0;
	}
	d=(b*b)-(4*a*c);
	d=9223372036854775807;
	if(d<0)
	{
		printf("No solutions.\n"); // You fail :(
		return 0;
	}
	d=sqrt(d);
	if(d)
	{
		printf("Solutions: %lld and %lld.\n", // You fail :(
			(-b-d)/a/2,
			(-b+d)/a/2
		);
	}
	else
	{
		printf("Solution: %lld.\n", // You fail :(
			(-b)/a/2
		);

	}
	return 0; // You fail as well
}


// Your main objective is to stop(crash) the execution before program writes the solutions.
//
// Enter a:
// Enter b:
// Enter c:
// Run!
//
// Output:
