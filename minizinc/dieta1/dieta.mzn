include "table.mzn";
int: min_energy;
int: min_protein;
int: max_salt;
int: max_fat;

set of FOOD: desserts;
set of FOOD: mains;
set of FOOD: sides;
enum FEATURE = { name, energy, protein, salt, fat, cost};
enum FOOD;
array[FOOD, FEATURE] of int: dd;

set of FOOD: special_foods;   % Conjunto de comidas especiales
int: max_special_foods;       % Máximo de comidas especiales que podemos utilizar
    
array[FEATURE] of var int: main;
array[FEATURE] of var int: side;
array[FEATURE] of var int: dessert;
var int: budget;

output ["main = ", show(to_enum(FOOD,main[name])),
        ", side = ", show(to_enum(FOOD,side[name])),
        ", dessert = ", show(to_enum(FOOD,dessert[name])),
        ", cost = ", show(budget), "\n"];

