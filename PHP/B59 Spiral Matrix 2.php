<!-- ans = [[0] * n for _ in range(n)]
cnt = 1
for loop in range((n + 1) // 2):
    # direction 1 - traverse from left to right
    for i in range(loop, n - loop):
        ans[loop][i] = cnt
        cnt += 1
    # direction 2 - traverse from top to bottom
    for i in range(loop + 1, n - loop):
        ans[i][n - loop - 1] = cnt
        cnt += 1
    # # direction 3 - traverse from right to left
    for i in range(n - loop - 2, loop - 1, -1):
        ans[n - loop - 1][i] = cnt
        cnt += 1
    # # direction 4 - traverse from bottom to top
    for i in range(n - loop - 2, loop, -1):
        ans[i][loop] = cnt
        cnt += 1 -->

<?php
    $n =6;
    $arr = array_fill(0,$n,array_fill(0,$n,0));
    $nn = floor(($n+1)/2);
    $cnt=1;
    // echo ('$nn la :'.$nn."<br>");
    for  ($loop =0;$loop <$nn;$loop++) {
        //  direction 1 - traverse from left to right
        for ($i=$loop;$i<($n-$loop);$i++){
            $arr[$loop][$i] = $cnt++;
        };
        // # direction 2 - traverse from top to bottom
        for ($i=$loop+1;$i<($n-$loop);$i++){
            $arr[$i][$n-$loop-1] = $cnt++;
        };
        // direction 3 - traverse from right to left
        for ($i=$n-$loop-2;$i>($loop-1);$i--){
            $arr[$n-$loop-1][$i] = $cnt++;
        };
        // direction 4 - traverse from bottom to top
        for ($i=$n-$loop-2;$i>($loop);$i--){
            $arr[$i][$loop]= $cnt++;
        };
    }
//  in ra 
    foreach ($arr as $a) {
        foreach ( $a as $b) {
            print $b." ";
        }
        echo "<br>";
    }