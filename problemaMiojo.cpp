#include "problemaMiojo.h"

#include <limits.h>

void troca(int* a, int* b){
	int c = *a;
	*a = *b;
	*b = c;
}

int problemaMiojoPrivate(int tempoMiojo, int amp1, int amp2, int amp1Original, int amp2Original){
	if(amp1 == amp2){
		return 0;
	}

	if(amp1 > INT_MAX || amp2 > INT_MAX){
		return 0;
	}

	int maiorTempo = 0;

	if(amp1 > amp2){
		troca(&amp1, &amp2);
		troca(&amp1Original, &amp2Original);
	}

	int diferenca = amp2 - amp1;
	maiorTempo = amp2;

	if(diferenca == tempoMiojo){
		return maiorTempo;
	} else {
		return problemaMiojoPrivate(tempoMiojo,
									amp1 + amp1Original,
									amp2,
									amp1Original,
									amp2Original);
	}
}

int problemaMiojo(int tempoMiojo, int amp1, int amp2){
	if(
		amp1 < tempoMiojo ||
		amp2 < tempoMiojo ||
		amp1 == amp2
	  ) {
		return -1;
	}

	return problemaMiojoPrivate(tempoMiojo, amp1, amp2, amp1, amp2);
}
