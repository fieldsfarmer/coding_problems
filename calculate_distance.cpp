// Given a vector T of length N. T[i] denotes that i is connected to the neighbor T[i]. If i == T[i], it's the capital.
// The N nodes 0, ..., N-1 form a tree (i.e. all of them are connected and there is no loop).
// Return a vector S of length N-1. S[i] is the number of nodes that have distance of i+1 from the capital.
// For example, T[0]=9, T[1]=1, T[2]=4, T[3]=9, T[4]=0, T[5]=4, T[6]=8, T[8]=0, T[9]=1
// Then it will return [1,3,2,3,0,0,0,0,0] because 1 is the captial. 9 is distance 1 from it. [0,3,7] is distance 2 from it. [4,8] is distance 3 from it. [2,5,6] is distance 4 from it.
// The worst time complexity is required to be O(N). The worst space is also the same.

