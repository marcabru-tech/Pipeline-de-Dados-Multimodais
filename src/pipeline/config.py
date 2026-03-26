"""Configurações e constantes de paths do pipeline."""

from pathlib import Path

# Raiz do repositório (dois níveis acima deste arquivo: src/pipeline/config.py)
ROOT_DIR: Path = Path(__file__).resolve().parents[2]

DATA_DIR: Path = ROOT_DIR / "data"
RAW_DIR: Path = DATA_DIR / "raw"
PROCESSED_DIR: Path = DATA_DIR / "processed"

SAMPLE_TEXTS: Path = RAW_DIR / "sample_texts.txt"
SAMPLE_IMAGE: Path = RAW_DIR / "sample_image.jpg"
