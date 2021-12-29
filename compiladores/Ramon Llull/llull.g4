grammar llull;

root : bloc EOF;

bloc : instru* ;

instru : arrayCrear
  |ejecutarFuncion
  |arrayGet
  |arraySet
  |expr
  |ifCondicion
  |condicion
  |assigancio
  |lectura
  |escriptura
  |bucleWhile
  |bucleFor
  |asignacionFuncion
  |expr
  ;

expr : arrayGet
  |'(' expr ')'
  |<assoc=right> expr '^' expr
  |expr ('*'|'/'|'%') expr
  |expr ('+'|'-') expr
  |(NUM|ID)
  ;

condicion : expr ('=='|'<>'|'<'|'>'|'<='|'>=') expr ;

lectura : 'read' '(' ID ')' ;

bucleWhile : 'while' '(' condicion ')' '{' bloc '}';

bucleFor : 'for' '(' assigancio ';' condicion ';' assigancio ')' '{' bloc '}' ;

escriptura: 'write' '(' blocStrings ')' ;

assigancio : ID '=' (expr|condicion) ;

blocStrings : (expr|STRING) (',' (expr|STRING))* ;

asignacionFuncion : 'void' ID '(' asigParametros ')' '{' bloc '}' ;

ejecutarFuncion: ID '(' ejecParametros ')' ;

asigParametros : (ID (',' ID)* )? ;

ejecParametros : (expr (',' expr)* )? ;

ifCondicion : 'if' '(' condicion ')' '{' bloc '}' (elseCondicion)?;

elseCondicion: 'else' '{' bloc '}';

arrayCrear : 'array' '(' ID ',' expr ')' ;

arrayGet : 'get' '(' ID ',' expr ')' ;

arraySet : 'set' '(' ID ',' expr ',' expr ')' ;

ID : [a-zA-Z]+ ;

STRING : '"' ~["]* '"' ;

NUM : [0-9]+ ;

WS : [ \n#] -> skip ;

COMMENT : '#' ~[\r\n]* -> skip ;
