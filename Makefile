####################################
# Makefile for compiling resources
####################################

# Define variables
dir_static = app/static
dir_css = $(dir_static)/css/custom
dir_less = $(dir_static)/less/custom
lessc = ./node_modules/less/bin/lessc

# Make rules
$(dir_css)/%.css: $(dir_less)/%.less
	$(lessc) $< > $@

# Set all target
all: $(dir_css)/styles.css
