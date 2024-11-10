const n=6;
const arr= Array.from(Array(n), _ => Array(n).fill(0));
var i=0;
var cnt = 1;
const LIM =Math.floor((n+1)/2);
for (let loop = 0; loop<LIM;loop++){
    // iterate from left to right
    for(i =loop;i<n-loop;i++) arr[loop][i] = cnt++;
    // iterate from top to bottom 
    for(i =loop+1;i<n-loop;i++) arr[i][n - loop - 1] = cnt++;
    // iterate from right to left
    for(i =n-loop-2;i>loop-1;i--) arr[n - loop - 1][i] = cnt++;
    // iterate from bottom to top
    for(i =n-loop-2;i>loop;i--) arr[i][loop] = cnt++;
};
for (let j=0;j<n;j++){
    console.log(arr[j]);
}



// cnt = 1 # index from 1 to n
// for loop in range((n + 1) // 2):
//     # Top loop from Left to Right
//     for i in range(loop, n - loop):
//         arr[loop][i] = cnt
//         cnt += 1
//     # Right loop from top to bottom
//     for i in range(loop + 1, n - loop):
//         arr[i][n - loop - 1] = cnt
//         cnt += 1
//     # Bottom loop from right to left
//     for i in range(n - loop - 2, loop - 1, -1):
//         arr[n - loop - 1][i] = cnt
//         cnt += 1
//     # Left loop from bottom to top
//     for i in range(n - loop - 2, loop, -1):
//         arr[i][loop] = cnt
//         cnt += 1