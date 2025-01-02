#include <stdio.h>
#include <stdlib.h>

void display(int*, int,int);
void input(int*, int,int);
void new_screen();

int add_scalar(int*, int,int, int);
int multiply_scalar(int*, int,int, int);
int multiply(int*,int*, int,int, int,int);
int add(int*,int*, int,int);
int inverse(int*, int,int);
int transpose(int*, int,int);
int determinant( int*, int,int);

int *matrix_1=NULL, *matrix_2=NULL, *matrix_3=NULL, m1,m2,m3, n1,n2,n3, choice, num;

void main(){
system("clear");
start:
printf("\nenter the dimentions of matrix(MxN): ");
if (scanf("%dx%d",&m1,&n1) != 2){
	printf("\n\n---invalid input---");
	new_screen();
	goto start;
}
else if((matrix_1 = (int*)malloc(sizeof(int)*m1*n1)) == NULL){
	printf("\ncan not allocate memory, please clear some RAM and try again");
	new_screen();
	goto start;
}
input(matrix_1,m1,n1);

do{
new_screen();
printf("\n---------------------------------------------------");
printf("\noperand matrix:");
display(matrix_1,m1,n1);

printf("\n\nWhat do you wish to do...");
printf("\n1. Multiply by scalar number");
printf("\n2. Add a scalar number");
printf("\n3. Multiply by a matrix");
printf("\n4. Add a matrix");
printf("\n5. Transpose matrix");
printf("\n6. Find determinant");
printf("\n7. Adjoint matrix")
printf("\n8. Inverse matrix");
printf("\n9. Enter new matrix");
printf("\n0. Exit");

printf("\n\nenter choice: ");
scanf("%d",&choice);

switch(choice){

case (1):
	printf("\nenter the number: ");
	scanf("%d",&num);
	if (multiply_scalar(matrix_1,m1,n1,num)==1){
		printf("\nmemory could not be allocated, please free some ram and try again");
		continue;
		}
	break;
case (2):
	printf("\nenter the number: ");
	scanf("%d",&num);
	if (add_scalar(matrix_1,m1,n1,num)==1){
		printf("\nmemory could not be allocated, please free some ram and try again");
		continue;
		}
	break;
case (3):
	printf("\nenter the dimentions of matrix(MxN): ");
        if (scanf("%dx%d",&m2,&n2) != 2){
                printf("\n---invalid input---");
                continue;
        }
        else if (n1!=m2){
                printf("\nthe dimentions of operand matrices are inconsistent, please try again");
                continue;
        }
        else if((matrix_2 = (int*)malloc(sizeof(int)*m2*n2)) == NULL){
                        printf("\ncan not allocate memory, please clear some RAM and try again");
                continue;
        }
        input(matrix_2,m2,n2);

	if (multiply(matrix_1,matrix_2,m1,m2,n1,n2)==1){
		printf("\ncan not allocate memory, please clear some RAM and try again");
		continue;
	}
	free(matrix_2);
	break;
case (4):
	printf("\nenter the dimentions of matrix(MxN): ");
	if (scanf("%dx%d",&m2,&n2) != 2){
		printf("\n---invalid input---");
		continue;
	}
	else if (m1!=m2 || n1!=n2){
		printf("\nthe dimentions of operand matrices are inconsistent, please try again");
		continue;
	}
	else if((matrix_2 = (int*)malloc(sizeof(int)*m2*n2)) == NULL){
		printf("\ncan not allocate memory, please clear some RAM and try again");
		continue;
	}
	input(matrix_2,m2,n2);

	if (add(matrix_1,matrix_2,m1,n1) == 1){
		printf("\nmemory could not be alocated, please clear some RAM and try again");
		continue;
	}
	free(matrix_2);
	break;
case (5):
	if (transpose(matrix_1,m1,n1)==1){
		printf("\nmemory could not be allocated, please free some RAM and try again");
		continue;
	}
	break;
case (6):
	break;
case (7):
	break;
case (8):
	printf("\nenter the dimentions of matrix(MxN): ");
	if (scanf("%dx%d",&m3,&n3) != 2){
                printf("\n---invalid input---");
                continue;
        }
        else if((matrix_3 = (int*)malloc(sizeof(int)*m3*n3)) == NULL){
                        printf("\ncan not allocate memory, please clear some RAM and try again");
                continue;
        }
        input(matrix_3,m3,n3);
	break;
case (0):
	free(matrix_1);
	printf("\n\n---you have exited the program---");
	printf("\n***************************************************\n");
	exit(0);
default:
	printf("\n\n---invalid choice---");
}

free(matrix_1);
matrix_1=matrix_3;
matrix_3=NULL;
m1=m3; n1=n3;
}while(choice);
}



void input(int* matrix, int m, int n){
//inputs integers to matrix as elements
for (int i=0;i<m;i++){
	printf("enter the elements of row %d: ",i+1);
	for (int j=0;j<n;j++)
		scanf("%d",(matrix + n*i + j));
}}




void display(int *matrix, int m,int n){
//displays the matrix on screen
for (int i=0;i<m;i++){
	printf("\n[\t");
	for (int j=0;j<n;j++)
		printf("%d\t",*(matrix + i*n +j));
	printf("]");
}}




void new_screen(){
printf("\nenter anything to go back");
scanf(" %c");
system("clear");
}




int multiply_scalar(int *matrix_1, int m1, int n1, int num){
//multiplies every element in matrix_1 by a given integer and puts the result in matrix_3
m3=m1;
n3=n1;
if ((matrix_3 = (int*)calloc(sizeof(int),m1*n1))==NULL)
	return 1;
for (int x=m1*n1; x--;)
	*(matrix_3+x) = *(matrix_1+x) * num;
return 0;
}




int add_scalar(int *matrix_1, int m1, int n1, int num){
//adds every element in matrix_1 by the given number and puts the result in matrix_3
m3=m1;
n3=n1;
if ((matrix_3 = (int*)calloc(sizeof(int),m1*n1))==NULL)
	return 1;
for (int x=m1*n1; x--;)
	*(matrix_3+x) = *(matrix_1+x) + num;
return 0;
}




int multiply(int *matrix_1, int *matrix_2, int m1,int m2, int n1, int n2){
//multiplies matrix_1 and matrix_2 puts the results in matrix_3
m3=m1;
n3=n2;
if ((matrix_3=(int*)calloc(sizeof(int), m3*n3))==NULL)
	return 1;
for (int i=0, x=m3*n3;i<x;i++)
        for (int j=0;j<n1;j++)
	        *(matrix_3+i) += *(matrix_1 + (i/n3)*n1 + j) * (*(matrix_2 + (i%n3) + (j*n3)));
return 0;
}




int add(int *matrix_1, int *matrix_2, int m, int n){
//adds matrix_1 and matrix_2 then puts the reslt in matrix_3
m3=m1;
n3=n1;
if ((matrix_3=(int *)calloc(sizeof(int),m*n))==NULL)
	return 1;
for (int x=m*n;x--;)
	*(matrix_3+x) = *(matrix_1+x) + *(matrix_2+x);
return 0;
}




int transpose(int *matrix_1,int m, int n){
//transposes the matrix and stores the result in matrix_3
m3=n1;
n3=m1;
if ((matrix_3=(int*)calloc(sizeof(int),m3*n3))==NULL)
	return 1;
for (int x=m3*n3;x--;)
	*(matrix_3+x)=*(matrix_1 + (x%n3)*m3 + x/n3);
return 0;
}
