# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def problema_miojo_private(tempo_miojo, amp_1, amp_2, amp_1_original, amp_2_original):
	if amp_1 == amp_2:
		return 0
	maiortempo = 0
	if amp_1 < amp_2:
		diferenca = amp_2 - amp_1
		maiortempo = amp_2
	else:
		return problema_miojo_private(tempo_miojo,amp_2,amp_1, amp_2_original, \
			amp_1_original)

	if diferenca == tempo_miojo:
		return maiortempo
	else:
		return problema_miojo_private(tempo_miojo, amp_1 + amp_1_original, amp_2, \
			amp_1_original, amp_2_original)


def problema_miojo(tempo_miojo, amp_1, amp_2):
	if amp_1 < tempo_miojo or amp_2 < tempo_miojo or amp_1 == amp_2:
		return -1
	else:
		return problema_miojo_private(tempo_miojo, amp_1, amp_2, amp_1, amp_2)

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
	def test_5_6_7(self):
		self.assertEqual(12, problema_miojo(5,6,7))
    def teste_sem_solucao(self):
    	self.assertEqual(0, problema_miojo(2, 4, 8))
    def teste_derradeiro(self):
    	self.assertEqual(110, problema_miojo(10, 110, 20))
    def teste_2_200_199(self):
    	self.assertEqual(400, problema_miojo(2, 200, 199))
    def teste_0_0_0(self):
    	self.assertEqual(-1, problema_miojo(0, 0, 0))
    def teste_30_50_60(self):
    	self.assertEqual(150, problema_miojo(30, 50, 60))
    #def teste_2119_7963_22171(self):
    #	self.assertEqual(4037241, problema_miojo(2119, 7963, 22171))

if __name__ == '__main__':
    unittest.main()
