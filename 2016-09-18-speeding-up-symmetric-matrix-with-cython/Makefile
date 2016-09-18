.PHONY: tests benchmark pep8 clean

symmetric_matrix.so: symmetric_matrix.pyx
	@python3 setup.py build_ext -if
	@mv symmetric_matrix.*.so symmetric_matrix.so

tests: symmetric_matrix.so
	@nosetests symmetric_matrix_tests.py

benchmark: symmetric_matrix.so
	@python3 benchmark.py

pep8:
	@pep8 *.py symmetric_matrix.pyx

clean:
	rm -rf *.so build/ __pycache__/ *.html *.c
