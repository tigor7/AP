int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

array[ITEMS] of var 0..1: taken;

constraint sum(i in ITEMS) (taken[i] * weight[i]) <= capacity;

var int: total_value = sum(i in ITEMS) (taken[i] * value[i]);

solve maximize total_value;

output ["taken = \(taken)\nTotal Value = \(total_value)"];