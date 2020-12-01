INPUT_FILES = $(shell find test_formats -type f)

.PHONY: generate python_generator_dependecies $(INPUT_FILES)

generate: python_generator_dependecies $(INPUT_FILES)

python_generator_dependecies:
	@echo "Installing dependencies..."
	@python3 -m pip install numpy tqdm
	@rm -r -f in
	@mkdir in

$(INPUT_FILES):
	@echo "\n==============="
	@python3 generator.py quiet < $@
	@echo "===============\n"
