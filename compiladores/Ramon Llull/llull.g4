grammar llull;

root : bloc EOF;

bloc : instru* ;

instru : expr
  |assigancio
  |lectura
  |escriptura
  ;

expr : '(' expr ')'
  |<assoc=right> expr '^' expr
  |expr ('*'|'/') expr
  |expr ('+'|'-') expr
  |(NUM|ID)
  ;

lectura : 'read' '(' ID ')' ;

escriptura: 'write' '(' blocStrings ')' ;

assigancio : ID '=' expr ;

blocStrings : (expr|STRING) (',' (expr|STRING))* ;

ID : [a-zA-Z]+ ;

STRING : '"' ~["]* '"' ;

NUM : [0-9]+ ;

WS : [ \n]+ -> skip ;
