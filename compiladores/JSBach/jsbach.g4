grammar jsbach;

root : bloc EOF;

bloc : instru*;

instru : escriure
    | expr
    | lectura
    | bucleWhile
    | assigancio
    | crearFuncio
    | executarFuncio
    | condicioIf
    | afegirFinalLLista
    | retallarLlista
    | notas
    | crearLlista
    ;

expr : '(' expr ')'
  |<assoc=right> expr '^' expr
  |expr ('*'|'/'|'%') expr
  |expr ('+'|'-') expr
  |longitudLlista
  |agafarValorLLista
  |(NUM|VARIABLE|NOTA)
  ;

condicio : expr ('='|'/='|'<'|'>'|'<='|'>=') expr ;

lectura : '<?>' VARIABLE;

escriure : '<!>' blocStrings;

blocStrings : (expr|STRING) (expr|STRING)*;

bucleWhile : 'while'  condicio  '|:' bloc ':|';

assigancio : (VARIABLE ('[' expr ']')?) '<-' expr;

crearFuncio : FUNCIO crearParametres '|:' bloc ':|';

executarFuncio : FUNCIO executarParametres;

executarParametres : expr*;

crearParametres : (VARIABLE)*;

condicioIf : 'if' condicio '|:'  bloc ':|' (condicioElse)?;

condicioElse : 'else' '|:' bloc ':|';

agafarValorLLista : VARIABLE '[' expr ']';

afegirFinalLLista : VARIABLE '<<' expr;

retallarLlista : '8<' VARIABLE '[' expr ']';

longitudLlista : '#' VARIABLE;

crearLlista : VARIABLE '<-' '{' expr* '}';

notas : '<:>' (VARIABLE|'{' NOTA* '}');

NUM : [0-9]+;
VARIABLE : [a-z][A-Za-z]*;
FUNCIO : [A-Z][a-zA-Z]+;
STRING: '"' ~["]* '"';

NOTA: [A-G][0-8]?;

WS : [ \n]+ -> skip;
COMMENT : '~~~' .*? '~~~' -> skip;