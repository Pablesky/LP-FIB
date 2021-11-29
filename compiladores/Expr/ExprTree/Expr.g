grammar Expr;
root : expr EOF ;
expr : VAR ':=' expr [expr]?
    |'(' expr ')'
    | <assoc=right> expr '^' expr
    | expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | 'write' expr
    | VAR
    | NUM
    ;
NUM : [0-9]+ ;
VAR : [a-zA-Z]+;
WS : [ \n]+ -> skip ;
