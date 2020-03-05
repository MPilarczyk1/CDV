#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<sys/types.h>
#include<unistd.h>
#include<string.h>

int main(int argc, char* argv[])
{
	
	char buf1[]="abcdefghij";
	char buf2[]="ABCDEFGHIJ";
	
	int fd;
	if((fd = open ("file.nohole", O_CREAT | O_WRONLY | O_TRUNC, 0664))==-1)
	{
		fprintf(stderr,"Couldn't create file\n");
		return 1;
	}
	
	if(write(fd,buf1,10) != 10)
	{
		fprintf(stderr,"Error\n");
		return 2;
	}
	if(write(fd,buf2,10)!=10)
		{
			
			fprintf(stderr,"Error\n");
			return 3;
		}
		
		close(fd);
		
		return 0;
}