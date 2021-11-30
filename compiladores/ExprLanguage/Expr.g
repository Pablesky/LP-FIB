grammar Expr;

root : instru* EOF ;

instru: bucle
      | ifcondition
      | condition
      | expr
      | assignation
      | imprimir
      ;

expr : <assoc=right> expr '^' expr
    |expr ('*'|'/') expr
    |expr ('+'|'-') expr
    |(NUM|VAR)
    ;

bucle : 'while' condition 'do' (instru)+ 'end';

assignation : VAR ':=' (expr|condition) ;

imprimir : 'write' (expr|condition) ;

condition : expr ('='|'<'|'>'|'>='|'<=') expr;

ifcondition: 'if' condition 'then' (instru)+ 'end';

NUM : [0-9]+ ;

VAR : [a-zA-Z]+ ;

WS : [ \n]+ -> skip ;
