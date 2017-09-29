// Give an array A, [2,3,1], which denote the height of sequence of locations. You can only build house in either valley or hill.
// Suppose [p ... q] is the section of the array. A[p] == A[p+1] == ... == A[q].
// If A[p-1] < A[p] and A[q] > A[q+1], then the section is a hill.
// If A[p-1] > A[p] and A[q] < A[q+1], then the section is a valley.
// If p == 0 or q == A.size()-1, then the side which beyond the range of the array can be taken as either very high or very low.
// Find how may houses can you build.
// For example: [2,2,1], return 2; [-1,-1], return 1; [2,3,1,1] return 3;

int solution(vector<int> &A) {
    int len = A.size();
    if(len==0) return 0;
    int cnt = 0;
    int p = 0, q = 0;
    int lastHeight = -1000000001;
    while(q<len){
        if(q<len-1 && A[q+1] != A[q]){
            if(A[q+1] < A[q]){
                if (p == 0 || (p>0 && A[p-1] < A[p])){
                    cnt += 1;
                    lastHeight = A[q];
                }
                p = q+1;
                q = q+1;
            }
            else if(A[q+1] > A[q]){
                if(p == 0 || (p>0 && A[p-1] > A[p])){
                    cnt += 1;
                    lastHeight = A[q];
                }
                p = q+1;
                q = q+1;
            }
        }
        else {
            q += 1;
        }
    }
    if(lastHeight != A[len-1])
        cnt += 1;
    return cnt;
}
