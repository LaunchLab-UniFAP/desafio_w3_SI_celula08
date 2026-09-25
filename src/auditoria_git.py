"""Audita os commits dos ultimos sete dias da celula."""

from collections import Counter
import subprocess


SEPARADOR = "\x1f"


def obter_commits():
    formato = "%H%x1f%an%x1f%ad%x1f%s"
    resultado = subprocess.run(
        [
            "git",
            "log",
            "--since=7 days ago",
            f"--format={formato}",
            "--date=short",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    commits = []
    for linha in resultado.stdout.splitlines():
        hash_commit, autor, data, mensagem = linha.split(SEPARADOR, maxsplit=3)
        commits.append(
            {
                "hash": hash_commit,
                "autor": autor,
                "data": data,
                "mensagem": mensagem,
            }
        )
    return commits


def gerar_relatorio(commits):
    linhas = ["RELATORIO SEMANAL DE COMMITS", ""]

    for commit in commits:
        linhas.append(
            f"Commit: {commit['hash']} | {commit['autor']} | {commit['data']} | "
            f"{commit['mensagem']}"
        )
    if not commits:
        linhas.append("Nenhum commit encontrado nos ultimos 7 dias.")

    autores = Counter(commit["autor"] for commit in commits)
    linhas.extend(["", "COMMITS POR PESSOA"])
    for autor, quantidade in autores.items():
        linhas.append(f"{autor}: {quantidade} commit(s)")

    if len(autores) < 2:
        resultado = "EVIDENCIA INSUFICIENTE"
    elif max(autores.values()) - min(autores.values()) <= 1:
        resultado = "ISONOMIA CONFIRMADA"
    else:
        resultado = "DIVISAO DE TAREFAS DEVE SER REVISTA"

    linhas.append(f"\nResultado: {resultado}")
    return "\n".join(linhas)


def main():
    print(gerar_relatorio(obter_commits()))


if __name__ == "__main__":
    main()
