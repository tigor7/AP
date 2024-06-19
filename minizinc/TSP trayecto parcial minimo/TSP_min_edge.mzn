%TSP trayecto parcial mínimo

include "globals.mzn";
int: numCities;          % número de ciudades
set of int: City = 1..numCities; 
int: maxAllowedEdge;     % máxima distancia permitida de un trayecto del recorrido

% distancia entre ciudades 
% -1 significa que no hay conexión directa
array[City,City] of int: distance; 

array[City] of var int: succ;

constraint circuit (succ);
constraint forall(i in City) (distance[i, succ[i]] != -1);

var 0..maxAllowedEdge: maxEdge = max(i in City) (distance[i, succ[i]]);

solve minimize maxEdge;

output ["succ = array1d(1..\(numCities), \(succ);\nmaxEdge = \(maxEdge)"];