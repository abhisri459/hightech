%{

#include <stdio.h>

#include "y.tab.h"

extern yylval;

%}

%%

[ \t];

[+|-|*|/|=|<|>] {printf("%s is an Operator.\n",yytext);return OP;}

[0-9]+ {yylval = atoi(yytext); printf("%d is a Number.\n",yylval); return DIGIT;} 

int|char|bool|float|void|for|do|while|if|else|return|void {printf("%s is a Keyword.\n",yytext);return KEY;}

[a-zA-Z0-9]+ {printf("%s is an Identifier.\n",yytext);return ID;}

. ;

%%
