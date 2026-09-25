import json
from pathlib import Path
import unittest


MANIFESTO = Path(__file__).resolve().parents[1] / "docs" / "governanca_dados.json"


class TestGovernancaDados(unittest.TestCase):
    def test_manifesto_define_licenca_privacidade_retencao_e_auditoria(self):
        with MANIFESTO.open(encoding="utf-8") as arquivo:
            manifesto = json.load(arquivo)

        self.assertEqual(manifesto["licenca_distribuicao"]["tipo"], "MIT")
        self.assertTrue(manifesto["compliance_lgpd"]["anonimizacao_obrigatoria"])
        self.assertTrue(manifesto["compliance_lgpd"]["restricoes_anonimizacao"])
        self.assertEqual(
            manifesto["compliance_lgpd"]["politica_retencao_historico"]["prazo_anos"],
            5,
        )
        self.assertTrue(manifesto["regras_git"]["auditoria_commits_obrigatoria"])


if __name__ == "__main__":
    unittest.main()
