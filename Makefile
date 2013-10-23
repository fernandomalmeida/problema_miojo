test: compile
	./test/test --log_level=test_suite

compile:
	g++ -o test/test -lboost_unit_test_framework test/test.cpp problemaMiojo.cpp
