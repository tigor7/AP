int: num_nodes;                          % número de nodos del grafo
int: num_edges;                          % número de aristas del grafo

1..num_nodes:source;                     % nodo fuente
1..num_nodes:sink;                       % nodo sumidero

array[1..num_edges, 1..2] of int: edges; % aristas del grafo (origen->destino)
array[1..num_edges] of int: capacity;    % capacidad de cada arista

var int: max_flow = exit[source];        % variable de decision para el valor
                                         % del flujo máximo
array[1..num_edges] of var int: flow;    % variable de decisión para el flujo
                                         % final de cada arista

constraint forall(i in 1..num_edges) ( flow[i] >= 0 /\flow[i] <= capacity[i]);

array[1..num_nodes] of var int: enter;
array[1..num_nodes] of var int: exit;

constraint forall(i in 1..num_nodes) (enter[i] = sum(j in 1..num_edges where edges[j, 2] = i) (flow[j]));
constraint forall(i in 1..num_nodes) (exit[i] = sum(j in 1..num_edges where edges[j, 1] = i) (flow[j]));

constraint forall(i in 1..num_nodes where i != source /\ i != sink) (enter[i] = exit[i]);

solve maximize max_flow;

output
[ 
  "max flow =" ++ show(max_flow)
];