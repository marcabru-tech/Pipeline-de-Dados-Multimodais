"""Processamento de texto: extração de entidades básicas."""

from __future__ import annotations

from typing import List

import pandas as pd


def extract_entities(texts: List[str]) -> pd.DataFrame:
    """Retorna DataFrame com cada frase e sua contagem de palavras.

    Args:
        texts: Lista de strings a processar.

    Returns:
        DataFrame com colunas ``frase`` e ``num_palavras``.
    """
    records = [
        {"frase": text, "num_palavras": len(text.split())}
        for text in texts
    ]
    return pd.DataFrame(records)
