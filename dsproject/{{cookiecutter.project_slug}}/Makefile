## install     : Install project package locally and install pre-commit.
.PHONY : install
install :
	python -m pip install pip-tools
	pip-compile requirements.in
	python -m pip install -r requirements.txt
	flit install --pth-file
	pre-commit install

## help        : Documentation for make targets.
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
