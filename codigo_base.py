# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def problema_miojo(tempo_miojo, amp_1, amp_2):
    if amp_1 < tempo_miojo or amp_2 < tempo_miojo or amp_1 == amp_2:
    	return -1



    return 0
 # 0 - nao e possivel
 # -1 - erro
 # > 0 possivel

class ProblemaMiojoTest(unittest.TestCase):
    def test_argumentos_1(self):
        self.assertEqual(-1, problema_miojo(5, 3, 2))
    def test_argumentos_2(self):
    	self.assertEqual(-1, problema_miojo(5, 10, 10))
    #def test_derradeiro(self)
    #	self.assertEqual(-1, problema_miojo(5, 10, 10))

if __name__ == '__main__':
    unittest.main()
