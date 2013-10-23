#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE ProblemaMiojo
#include <boost/test/unit_test.hpp>

#include "../problemaMiojo.h"

BOOST_AUTO_TEST_SUITE(ExemplosSimples)

BOOST_AUTO_TEST_CASE(checandoFalhasDeEntrada) {
	BOOST_CHECK_EQUAL(problemaMiojo(5, 3, 2), -1);
	BOOST_CHECK_EQUAL(problemaMiojo(5, 10, 10), -1);
	BOOST_CHECK_EQUAL(problemaMiojo(0, 0, 0), -1);
}

BOOST_AUTO_TEST_CASE(exemploDadoNoProblema){
	BOOST_CHECK_EQUAL(problemaMiojo(2, 5, 7), 7);
}

BOOST_AUTO_TEST_CASE(trocaDeParametrosDaFuncao){
	BOOST_CHECK_EQUAL(problemaMiojo(2, 7, 5), 7);
}

BOOST_AUTO_TEST_CASE(outrosExemplos){
	BOOST_CHECK_EQUAL(problemaMiojo(3, 5, 7), 10);
	BOOST_CHECK_EQUAL(problemaMiojo(3, 7, 5), 10);
	BOOST_CHECK_EQUAL(problemaMiojo(5,6,7), 12);
}

BOOST_AUTO_TEST_CASE(casoImpossivel){
	BOOST_CHECK_EQUAL(problemaMiojo(2, 4, 8), 0);
}

BOOST_AUTO_TEST_SUITE_END()

BOOST_AUTO_TEST_SUITE(ExemplosComplexos)

BOOST_AUTO_TEST_CASE(testesMaiores){
	BOOST_CHECK_EQUAL(problemaMiojo(10, 110, 20), 110);
	BOOST_CHECK_EQUAL(problemaMiojo(2, 200, 199), 400);
	BOOST_CHECK_EQUAL(problemaMiojo(30, 50, 60), 150);
}

BOOST_AUTO_TEST_CASE(testeDerradeiro){
	BOOST_CHECK_EQUAL(problemaMiojo(2119, 7963, 22171), 4037241);
}

BOOST_AUTO_TEST_SUITE_END()
