int: n = 5;

array[1..n] of var 0..9: my_array;

constraint sum(my_array) = product(my_array);

constraint forall(i in 1..n - 1) (my_array[i] <= my_array[i+1]);

solve maximize product(my_array);

output ["x = array1d(1..\(n), ["];

output ["\(my_array[i]), " | i in 1..n-1];
output ["\(my_array[n])]);"];
                                              