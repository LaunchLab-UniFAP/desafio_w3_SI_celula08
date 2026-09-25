import unittest

from src.auditoria_git import gerar_relatorio


class TestAuditoriaGit(unittest.TestCase):
    def test_relatorio_lista_hashes_e_aprova_divisao_isonomica_de_dupla(self):
        commits = [
            {
                "hash": "a" * 40,
                "autor": "Ana",
                "data": "2026-09-24",
                "mensagem": "feat: adiciona auditoria",
            },
            {
                "hash": "b" * 40,
                "autor": "Bruno",
                "data": "2026-09-25",
                "mensagem": "test: valida relatorio",
            },
        ]

        relatorio = gerar_relatorio(commits)

        self.assertIn(f"Commit: {'a' * 40} | Ana | 2026-09-24", relatorio)
        self.assertIn("Ana: 1 commit(s)", relatorio)
        self.assertIn("Bruno: 1 commit(s)", relatorio)
        self.assertIn("Resultado: ISONOMIA CONFIRMADA", relatorio)

    def test_relatorio_sinaliza_evidencia_insuficiente_com_um_unico_autor(self):
        commits = [
            {
                "hash": "c" * 40,
                "autor": "Carla",
                "data": "2026-09-25",
                "mensagem": "docs: adiciona politica",
            }
        ]

        relatorio = gerar_relatorio(commits)

        self.assertIn("Resultado: EVIDENCIA INSUFICIENTE", relatorio)


if __name__ == "__main__":
    unittest.main()
