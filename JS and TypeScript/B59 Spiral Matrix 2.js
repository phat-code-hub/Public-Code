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