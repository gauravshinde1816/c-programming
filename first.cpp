 
#include <bits/stdc++.h> 
using namespace std;   
int main() 
{ 
	int n;
    int sum=0;

    cin>>n;

	// input here 
 int A[n][n];
 int C[n][n];
 cout<<"enter the sample matrix"<<endl;
 for(int i=0;i<n;i++){
     for(int j=0;j<n;j++){
         cin>>A[i][j];
     }
 }


    //square matrix logic here..

    int magicSquare[n][n]; 

	
	memset(magicSquare, 0, sizeof(magicSquare)); 

 
	int i = n/2; 
	int j = n-1; 

	
	for (int num = 1; num <= n*n; ) 
	{ 
		if (i == -1 && j == n) 
		{ 
			j = n-2; 
			i = 0; 
		} 
		else
		{ 
			
			if (j == n) 
				j = 0; 

			
			if (i < 0) 
				i = n - 1; 
		} 
		if (magicSquare[i][j]) 
		{ 
			j -= 2; 
			i++; 
			continue; 
		} 
		else
			magicSquare[i][j] = num++; 

		j++; i--; 
	} 




    //end of sqaure matrix
    
    //cost logic
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
       C[i][j]=abs(A[i][j]-magicSquare[i][j]);
    }
}
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        sum=sum+C[i][j];
    }
}


    //print answer
    cout<<"minimal cost"<<sum;

	return 0; 
} 


