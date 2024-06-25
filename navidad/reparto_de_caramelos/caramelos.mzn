int: n;
array[1..n] of int: nota;        % Puntuación de cada niño; el indice del array
                                 % indica la posición donde está sentado.

int: max_caramelos = 100000;
array[1..n] of var 1..max_caramelos: x; % Número de caramelos dados a cada niño
var int: total_caramelos = sum(i in 1..n) (x[i]); % Número de caramelos totales repartidos por Rosa

var int: max_caramelos_x = max(i in 1..n) (x[i]);


output [ show(total_caramelos) ];


constraint forall(i in 1..n-1) (nota[i] = nota[i+1] -> x[i] = x[i+1]);
constraint forall(i in 1..n-1) (nota[i] < nota[i+1] -> x[i] < x[i+1]);
constraint forall(i in 1..n-1) (nota[i] > nota[i+1] -> x[i] > x[i+1]);
constraint forall(i in 1..n) (x[i] * 2 > max_caramelos_x);

solve minimize total_caramelos;