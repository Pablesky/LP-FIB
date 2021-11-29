grammar Expr;
root : expr EOF ;
expr : '(' expr ')'
    | <assoc=right> expr '^' expr
    | expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | NUM
    ;
NUM : [0-9]+ ;
WS : [ \n]+ -> skip ;
