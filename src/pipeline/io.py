"""Funções de I/O: leitura de textos/imagens e escrita de parquet."""

from __future__ import annotations

from pathlib import Path
from typing import List

import pandas as pd
from PIL import Image

from pipeline.config import PROCESSED_DIR, SAMPLE_IMAGE, SAMPLE_TEXTS


def load_texts() -> List[str]:
    """Lê sample_texts.txt e retorna lista de linhas não-vazias."""
    with SAMPLE_TEXTS.open(encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip()]


def load_image() -> Image.Image:
    """Abre sample_image.jpg com Pillow e retorna o objeto Image."""
    return Image.open(SAMPLE_IMAGE)


def save_parquet(df: pd.DataFrame, name: str) -> Path:
    """Salva *df* em data/processed/<name>.parquet e retorna o caminho."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PROCESSED_DIR / f"{name}.parquet"
    df.to_parquet(out_path, index=False)
    return out_path
