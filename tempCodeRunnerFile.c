#include <stdio.h>
#include <string.h>
int func(char a[])
{ puts(a);}
int main()
{
 char str[10];
 scanf("%s",str);   
func(&str[4]);
}
