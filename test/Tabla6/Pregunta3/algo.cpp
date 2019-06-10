#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int c;
    cin >> c;

    int *arr = new int[c];

    for(int i = 0; i <= c; i++){
        cin >> arr[i];
    }

    for(int j = c; j >= 1; j--){
        cout << arr[--n];
    }


    return 0;
}
