% minizinc stable_matchings_women.mzn -D "Women = {Maria, Ana, Lucia}; Men = {Carlos, Marco, Juan}; wrank=[|1, 2, 3|3, 2, 1|2, 3, 1|]; mrank=[|2, 1, 3|1, 2,3 |1, 3, 2|]"


include "globals.mzn";

enum Women;
enum Men;

array[Women, Men] of int: wrank;
array[Men, Women] of int: mrank;

array[Men] of var Women: wife;
array[Women] of var Men: husband;



constraint inverse(wife, husband);
constraint forall(m in Men, w in Women)(wrank[w,m] < wrank[w, husband[w]] -> mrank[m, wife[m]] < mrank[m, w]);
constraint forall(m in Men, w in Women)(mrank[m,w] < mrank[m, wife[m]] -> wrank[w, husband[w]] < wrank[w, m]);

var int: obj_men = sum(m in Men)(mrank[m, wife[m]] = 1);
var int: obj_women = sum(w in Women)(wrank[w, husband[w]] = 1);

solve minimize abs(obj_men - obj_women);

output ["wife: \(wife)\nhusband: \(husband)\nobj_men:\(obj_men)\nobj_women:\(obj_women)"];