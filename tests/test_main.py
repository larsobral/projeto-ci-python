import unittest
from main import obter_definicao, pesquisar_termo


class TestDicionarioTecnologia(unittest.TestCase):

    def test_obter_definicao_existente(self):
        definicao = obter_definicao("API")
        self.assertEqual(definicao, "Interface de Programação de Aplicativos")

    def test_obter_definicao_inexistente(self):
        definicao = obter_definicao("XYZ")
        self.assertEqual(definicao, "Termo não encontrado no dicionário.")

    def test_pesquisar_termo(self):
        resultados = pesquisar_termo("API")
        self.assertIn("API: Interface de Programação de Aplicativos", resultados)


if __name__ == '__main__':
    unittest.main()
