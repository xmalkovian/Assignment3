TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
Script = Assignment1copy.py
a1img1 = 1 1 1 1 0 0.01 100 1 1
a1img2 = 1 1 1 1 20 0.01 100 1 2
a1img3 = 1 1 1 1 20 0.01 100 0 3

all:	Assignment1.pdf

view:
	open Assignment1.pdf

clean:
	rm -f Assignment1.pdf a1img1.png a1img2.png a1img3.png

%.png: $(Script)
	python $^ $($*)

Assignment1.pdf: a1img1.png a1img2.png a1img3.png
	$(TEX) Assignment1.tex
