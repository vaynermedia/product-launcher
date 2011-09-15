M4   := $(shell which m4)
DEPS := ../m4/base.m4

ifeq ($(shell test -f overrides.m4 || echo n),n)
    .PHONY: overrides.m4
else
    DEPS += overrides.m4
endif

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  all          to make settings.py, JavaScript, and CSS"
	@echo "  settings.py  to make settings.py (Django's configuration file)"
	@echo "  migrations   to make South migration files"
	@echo "  clean        to make clean that which is dirty"
	@echo "  tests        to make a unit test run"

all: settings.py js css

settings.py: $(DEPS) settings.py.m4
	m4 $^ > $@

clean:
	rm -f settings.py && find . -name \*.pyc -print -delete
	rm -rf ./reports/

migrations:
	./manage.py schemamigration rocket --auto && echo "Migration files added." || echo "No changes."
	git add ./apps/rocket/migrations

tests:
	./manage.py test rocket
