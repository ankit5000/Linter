sumto(0,0).

sumto(N,S) :- N > 0, N1 is N - 1, sumto(N1,S1), S is S1 + N.

/*

Now sumto(10,S) will give 0 + 1 + 2 + ..... + 10 = 55.

*/

sumsquares(0,0).

sumsquares(N,S) :- N > 0, N1 is N - 1, sumsquares(N1,S1), S is S1 + (N*N).

/*

Now sumsquares(5,S) will give 0^2 + 1^2 + ... + 5^2 = 55.

*/