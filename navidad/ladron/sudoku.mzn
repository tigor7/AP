int: n;
int: x;
array[1..n] of int: value;

array[1..n] of var 0..1: taken;

var int: total_value = sum(i in 1..n) (taken[i] * value[i]);

constraint forall(i in 1..n-1) (taken[i] + taken[i + 1] < 2);

constraint sum(i in 1..n) (taken[i]) <= x;

solve maximize total_value;

output ["taken = \(taken)\ntotal_value = \(total_value)"];