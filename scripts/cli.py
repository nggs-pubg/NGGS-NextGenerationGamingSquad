"""CLI oficial da NGGS para automações do site."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from scripts.generators import create_weapon_page, update_calculator_page
from scripts.utils.math import DEFAULT_PUBG_YAW

app = typer.Typer(help="Ferramentas NGGS para geração de conteúdo e cálculos.")

gen_app = typer.Typer(help="Geradores de conteúdo estático.")
calc_app = typer.Typer(help="Calculadoras e utilitários de performance.")

app.add_typer(gen_app, name="gen")
app.add_typer(calc_app, name="calc")


@gen_app.command("weapon")
def generate_weapon(
    nome: Annotated[str, typer.Option("--nome", prompt=True, help="Nome da arma.")],
    tipo: Annotated[
        str,
        typer.Option(
            "--tipo",
            prompt=True,
            help="Tipo da arma (AR, DMR, SMG...).",
        ),
    ],
    saida: Annotated[
        Path,
        typer.Option(
            Path("docs/pubg/armas"),
            "--saida",
            help="Diretório de saída para o arquivo gerado.",
        ),
    ] = Path("docs/pubg/armas"),
    funcao: Annotated[str | None, typer.Option(help="Função da arma na composição.")] = None,
    cano: Annotated[str | None, typer.Option(help="Anexo de cano preferido.")] = None,
    empunhadura: Annotated[str | None, typer.Option(help="Empunhadura recomendada.")] = None,
    municao: Annotated[str | None, typer.Option(help="Tipo de munição.")] = None,
    otica: Annotated[str | None, typer.Option(help="Ótica recomendada.")] = None,
) -> None:
    """Gerar arquivo Markdown de arma baseado no template oficial."""
    try:
        destino = create_weapon_page(
            nome=nome,
            tipo=tipo,
            saida=saida,
            funcao=funcao,
            cano=cano,
            empunhadura=empunhadura,
            municao=municao,
            otica=otica,
        )
        typer.echo(f"✅ Arquivo gerado em: {destino}")
    except Exception as exc:  # pragma: no cover - mensagens de CLI
        typer.secho(f"Erro ao gerar arma: {exc}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from exc


@calc_app.command("edpi")
def calculate_edpi(
    dpi: Annotated[float, typer.Option("--dpi", prompt=True, help="DPI do mouse.")],
    sens: Annotated[float, typer.Option("--sens", prompt=True, help="Sensibilidade no jogo.")],
    saida: Annotated[
        Path,
        typer.Option("--saida", help="Arquivo Markdown a ser atualizado."),
    ] = Path("docs/mouse/calculadora.md"),
    yaw: Annotated[
        float,
        typer.Option(
            "--yaw",
            help="Yaw do jogo (padrão PUBG: 0.0025).",
            show_default=True,
        ),
    ] = DEFAULT_PUBG_YAW,
) -> None:
    """Atualizar calculadora de eDPI e distância de 360°."""
    try:
        destino = update_calculator_page(saida, dpi=dpi, sensitivity=sens, yaw=yaw)
        typer.echo(f"✅ Calculadora atualizada: {destino}")
    except Exception as exc:  # pragma: no cover - mensagens de CLI
        typer.secho(f"Erro ao atualizar calculadora: {exc}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from exc


@app.callback()
def main() -> None:
    """Ponto de entrada da CLI."""


if __name__ == "__main__":  # pragma: no cover
    app()
