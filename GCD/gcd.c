#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b);

int main(int argc, char* argv[])
{
	if (argc != 3) return EXIT_FAILURE;
	
	int n, m;

	m = atoi(argv[1]);
	n = atoi(argv[2]);

	printf("The GCD(%d, %d) = %d", m, n, gcd(m,n));
}

int gcd(int n, int m)
{
	if (n % m == 0)
		return (n < m) ? n : m;
	else return gcd(m, n%m);
}
