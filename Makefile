

app/static/less/custom/%.less: app/static/css/custom/%.css
	./node_modules/less/bin/lessc $< > $@

all: app/static/less/custom/style.less
