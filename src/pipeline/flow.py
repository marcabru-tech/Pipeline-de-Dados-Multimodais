"""Flow Prefect principal do Pipeline de Dados Multimodais."""

from __future__ import annotations

import pandas as pd
from prefect import flow, task
from prefect.deployments import Deployment
from prefect.client.schemas.schedules import CronSchedule
from rich.console import Console
from rich.table import Table

from pipeline.image_processing import basic_image_stats
from pipeline.io import load_image, load_texts, save_parquet
from pipeline.text_processing import extract_entities

console = Console()


@task(name="carregar-dados")
def task_load_data():
    """Carrega textos e imagem dos arquivos de entrada."""
    texts = load_texts()
    img = load_image()
    return texts, img


@task(name="processar-textos")
def task_process_texts(texts):
    """Extrai entidades básicas dos textos."""
    return extract_entities(texts)


@task(name="processar-imagem")
def task_process_image(img):
    """Calcula estatísticas básicas da imagem."""
    return basic_image_stats(img)


@task(name="salvar-resultados")
def task_save_results(df_texts: pd.DataFrame, img_stats: dict):
    """Persiste DataFrames de texto e imagem em parquet."""
    path_texts = save_parquet(df_texts, "text_entities")
    df_img = pd.DataFrame([img_stats])
    path_img = save_parquet(df_img, "image_stats")
    return path_texts, path_img


@task(name="imprimir-resumo")
def task_print_summary(df_texts: pd.DataFrame, img_stats: dict):
    """Imprime resumo formatado com Rich."""
    console.rule("[bold blue]Pipeline de Dados Multimodais[/bold blue]")

    # Tabela de textos
    tbl = Table(title="Entidades de Texto", show_lines=True)
    tbl.add_column("Frase", style="cyan", no_wrap=False)
    tbl.add_column("Nº Palavras", justify="right", style="green")
    for _, row in df_texts.iterrows():
        tbl.add_row(row["frase"], str(row["num_palavras"]))
    console.print(tbl)

    # Estatísticas de imagem
    console.print(
        f"[bold]Imagem:[/bold] {img_stats['largura']}x{img_stats['altura']} px  |  "
        f"Média RGB: [yellow]{img_stats['media_rgb']:.2f}[/yellow]"
    )
    console.rule()


@flow(name="demo-flow", description="Flow de demonstração multimodal.")
def demo_flow():
    """Executa o pipeline completo: carga → processamento → persistência → resumo."""
    texts, img = task_load_data()
    df_texts = task_process_texts(texts)
    img_stats = task_process_image(img)
    task_save_results(df_texts, img_stats)
    task_print_summary(df_texts, img_stats)


def deploy():
    """Registra um Deployment local do demo_flow (sem Docker)."""
    deployment = Deployment.build_from_flow(
        flow=demo_flow,
        name="demo-flow-local",
        work_queue_name="default",
        schedule=CronSchedule(cron="0 6 * * *", timezone="America/Sao_Paulo"),
    )
    deployment.apply()
    console.print("[green]Deployment 'demo-flow-local' registrado com sucesso![/green]")


if __name__ == "__main__":
    demo_flow()
