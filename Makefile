PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

# assumes github pages has been added as a submodule to the repo
PAGES_SUBMODULE=$(CURDIR)/mattpitkin.github.io
PAGES_DIR=$(PAGES_SUBMODULE)/samplers-demo

GITHUB_PAGES_REMOTE=https://github.com/mattpitkin/mattpitkin.github.io.git
GITHUB_PAGES_BRANCH=master

GIT_COMMIT_HASH = $(shell git rev-parse HEAD)

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make pages-submodule                add to gh-pages submodule          '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

serve-global:
ifdef SERVER
	cd $(OUTPUTBUILDDIR) && $(PY) -m pelican.server 80 $(SERVER)
else
	cd $(OUTPUTBUILDDIR) && $(PY) -m pelican.server 80 0.0.0.0
endif


devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	$(BASEDIR)/develop_server.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

pages-submodule: publish
	# make sure gh-pages submoduls is up-to-date
	cd $(PAGES_SUBMODULE) && git pull --rebase && cd $(CURDIR)
	# rsync only samplers-demo changes (deleting any removed files)
	rsync -av --delete $(OUTPUTDIR)/ $(PAGES_DIR)/
	cd $(PAGES_DIR) && git add * && git commit -a -m "Update samplers-demo"

publish-to-github: pages-submodule
	cd $(PAGES_SUBMODULE) && git pull --rebase && git push origin $(GITHUB_PAGES_BRANCH)
	# clean out any generated pages
	cd $(BASEDIR) && git clean -dxf

# remove the use of ghp-import by having gh-pages repo as a submodule
#publish-to-github: publish
#	ghp-import -n -m "publish-to-github from $(GIT_COMMIT_HASH)" -b blog-build $(OUTPUTDIR)
#	git push $(GITHUB_PAGES_REMOTE) blog-build:$(GITHUB_PAGES_BRANCH)

#publish-to-github-force: publish
#	ghp-import -n -m "publish-to-github-force from $(GIT_COMMIT_HASH)" -b blog-build $(OUTPUTDIR)
#	git push -f $(GITHUB_PAGES_REMOTE) blog-build:$(GITHUB_PAGES_BRANCH)

.PHONY: html help clean regenerate serve serve-global devserver stopserver publish github pages-submodule publish-to-github
