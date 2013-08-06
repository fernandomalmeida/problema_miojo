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

    maiortempo = 0
    if amp_1 < amp_2:
    	diferenca = amp_2 - amp_1
    	maiortempo = amp_2
    else:
    	return problema_miojo(tempo_miojo,amp_2,amp_1)

    if diferenca == tempo_miojo:
    	return maiortempo
    else:
    	return problema_miojo(tempo_miojo, amp_1*2, amp_2)

    return 0
 # 0 - nao e possivel
 # -1 - erro
 # > 0 possivel

class ProblemaMiojoTest(unittest.TestCase):
    def test_argumentos_1(self):
        self.assertEqual(-1, problema_miojo(5, 3, 2))
    def test_argumentos_2(self):
    	self.assertEqual(-1, problema_miojo(5, 10, 10))
    def test_diferenca_simples(self):
    	self.assertEqual(7, problema_miojo(2, 5, 7))
    def test_diferenca_trocada(self):
    	self.assertEqual(7, problema_miojo(2, 7, 5))
    def test_do_site(self):
    	self.assertEqual(10, problema_miojo(3, 5, 7))
    def test_do_site_trocada(self):
    	self.assertEqual(10, problema_miojo(3, 7, 5))
    #def teste_sem_solucao(self):
    #	self.assertEqual(0, problema_miojo(2, 4, 8))

if __name__ == '__main__':
    unittest.main()
