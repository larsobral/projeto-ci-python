import unittest
from main import obter_definicao


class TestDicionarioTecnologia(unittest.TestCase):

    def test_obter_definicao_existente(self):
        definicao = obter_definicao("API")
        self.assertEqual(definicao, "Interface de Programação de Aplicativos")

    def test_obter_definicao_inexistente(self):
        definicao = obter_definicao("XYZ")
        self.assertEqual(definicao, "Termo não encontrado no dicionário.")


if __name__ == '__main__':
    unittest.main()
