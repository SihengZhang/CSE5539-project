.PHONY: all clean pdf watch copy-figures

MAIN = main
LATEX = pdflatex
BIBTEX = bibtex

all: pdf

pdf: $(MAIN).tex
	$(LATEX) $(MAIN)
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.synctex.gz *.fdb_latexmk *.fls

watch:
	latexmk -pdf -pvc $(MAIN)

# Copy figures from data analysis
copy-figures:
	cp ../data/critical_points_analysis/*.png figures/analysis/
	@echo "Copied analysis figures to figures/analysis/"

# Quick compile (no bibliography)
quick:
	$(LATEX) $(MAIN)
