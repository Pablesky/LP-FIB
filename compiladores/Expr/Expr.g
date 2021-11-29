grammar Expr;
root : value EOF ;

value : conditional
    |assignation
    |ifcondition
    |expr;

expr :
    |'(' expr ')'
    | <assoc=right> expr '^' expr
    | expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | 'write' expr
    | VAR
    | NUM
    ;

assignation: VAR ':=' expr [expr]*;
ifcondition: 'if' conditional 'then' (expr)+ 'end';
conditional : expr ('='|'<'|'>'|'<='|'>=') expr;
NUM : [0-9]+ ;
VAR : [a-zA-Z]+;
WS : [ \n]+ -> skip ;
