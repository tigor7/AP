int: n;
array[1..n] of int: value;

array[1..n] of var 0..1: taken;

constraint forall (i in 1..n-1)(taken[i] + taken[i+1] < 2);

var int: total_value = sum (i in 1..n where taken[i] = 1) (value[i]);

solve maximize total_value;

output ["taken = ["] ++ ["\(taken[i])" ++ if i != n then ", " else "" endif | i in 1..n] ++ ["]\nTotal Value = \(total_value)"];
