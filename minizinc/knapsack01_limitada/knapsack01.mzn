% minizinc knapsack01.mzn -D "n=3; capacity=10; value = [45, 48, 35]; weight = [5, 5, 3]; m = 1; limitation = {1, 2};";
int: n;                    % numero maximo de items
int: capacity;            % capacidad de la mochila

set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

set of ITEMS: limitation;
int: m;                    % Numero maximo de items a elegir dentro del 
                          % conjuto limitation
var set of ITEMS: taken;
var int: benefit = sum(i in taken) (value[i]); 

constraint sum(i in taken) (weight[i]) <= capacity;
% Como se saca el tamaño de un set ???
constraint sum(i in (taken intersect limitation)) (1) <= m;

solve maximize benefit;

output ["taken = \(taken)\n\(benefit)"];