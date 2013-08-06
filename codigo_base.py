# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def problema_miojo(tempo_miojo, amp_1, amp_2):
    return True

class ProblemaMiojoTest(unittest.TestCase):
    def test_simples(self):
        self.assertEqual(True, problema_para_resolver())

if __name__ == '__main__':
    unittest.main()
