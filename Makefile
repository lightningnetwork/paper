# A very basic Makefile that can build a LaTeX file + bibliography.
# Use as you see fit.
SOURCE=paper

all: $(SOURCE).tex
	pdflatex $(SOURCE).tex < /dev/null > /dev/null
	bibtex $(SOURCE).aux < /dev/null > /dev/null
	pdflatex $(SOURCE).tex < /dev/null > /dev/null
	pdflatex $(SOURCE).tex < /dev/null > /dev/null

