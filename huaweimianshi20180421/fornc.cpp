#include<iostream>  
using namespace std;  
  
int Sum1s(int n)  
{  
    int count = 0; //记录1的个数  
    int factor = 1; //标记，逐位计算1的个数  
  
    int LowerNum = 0;  
    int CurrNum = 0;  
    int HigherNum = 0;  
  
    while ( n/factor != 0)        //每次计算LowerNum CurrNum HigherNum的值  
    {   cout <<'k';
        LowerNum = n - (n/factor) * factor;  
        CurrNum = (n/factor) % 10;  
        HigherNum = n / (factor*10);  
  
        switch (CurrNum)  
        {  
        case 0:  
            count += HigherNum * factor;  
            break;  
        case 1:  
            count += HigherNum * factor + LowerNum +1;  
            break;  
        default:  
            count += (HigherNum +1)*factor;  
            break;  
        }  
        factor *= 10;  
    }  
    
    return count;  
}  
  
int  main()  
{  
    cout<<Sum1s(1000)<<endl;  
} 