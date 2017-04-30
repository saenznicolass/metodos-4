REsultados_hw4.pdf: Resultados_hw4.tex
Resultados_hw4.tex: .txt
	python Plots_Temperatura.py
.txt: a.out
	./a.out
a.out: DifusionTemperatura.c
	cc DifusionTemperatura.c -lm