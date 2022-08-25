filename=interpreter.py

run: ${filename} scheme_methods.py parsing.py
	@python3 ${filename}

clean:
	@find . -name __pycache__ -type d  -exec rm -rf {} +
	@#rm *.swp
