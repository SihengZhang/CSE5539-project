# Makefile for LaTeX project proposal

# Main documents
MAIN = project_proposal
SIMPLE = project_proposal_simple

# LaTeX compiler
LATEX = pdflatex

# BibTeX compiler
BIBTEX = bibtex

.PHONY: all clean view simple help

# Default target - compile both versions
all: $(MAIN).pdf $(SIMPLE).pdf

# Compile the full proposal
$(MAIN).pdf: $(MAIN).tex
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex

# Compile the simple 2-page version
$(SIMPLE).pdf: $(SIMPLE).tex
	$(LATEX) $(SIMPLE).tex
	$(LATEX) $(SIMPLE).tex

# Just compile the simple version
simple: $(SIMPLE).pdf

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg

# Clean everything including PDFs
cleanall: clean
	rm -f $(MAIN).pdf $(SIMPLE).pdf

# View the full PDF (macOS)
view: $(MAIN).pdf
	open $(MAIN).pdf

# View the simple PDF (macOS)
view-simple: $(SIMPLE).pdf
	open $(SIMPLE).pdf

# Help message
help:
	@echo "Available targets:"
	@echo "  make              - Compile both proposal PDFs"
	@echo "  make simple       - Compile only the 2-page simple version"
	@echo "  make clean        - Remove auxiliary files"
	@echo "  make cleanall     - Remove all generated files including PDFs"
	@echo "  make view         - Open the full proposal PDF (macOS)"
	@echo "  make view-simple  - Open the simple 2-page PDF (macOS)"
	@echo "  make help         - Show this help message"
