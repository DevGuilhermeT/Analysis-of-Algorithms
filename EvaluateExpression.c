#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct what{
    char cont;
    struct what* prox;
} celula;

void empilhar(celula** cabeca, char y){
    celula *nova;
    nova = malloc(sizeof(celula));
    nova->cont = y;
    nova->prox = *cabeca;
    *cabeca = nova;
}

char desempilha(celula** cabeca){
    celula *p;
    p = *cabeca;
    char x; 
    x = p->cont;
    *cabeca = p->prox;
    free(p);
    return x;
}

bool corres(char c1, char c2){
	if (c1 == '(' && c2 == ')')
		return true;
	else if (c1 == '[' && c2 == ']')
		return true;
	else
		return false;
}

bool q3(char express[]){
	int i = 0;
    celula* p1 = NULL;
	while (express[i]){
		if (express[i] == '(' || express[i] == '[')
			empilhar(&p1, express[i]);
		if (express[i] == ')' || express[i] == ']') {
			if (p1 == NULL){
				return false;
            }else if (corres(desempilha(&p1), express[i]) == false)
				return false;
		}i++;
	}if (p1 == NULL){
		return true;
    }else{
		return false;
    }
}

int main(){
	char express[100] = "(00())";
	if (q3(express))
		printf("True\n");
	else
		printf("False\n");
	return 0;
}