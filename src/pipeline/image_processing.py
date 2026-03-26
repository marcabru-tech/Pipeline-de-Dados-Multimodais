"""Processamento de imagem: estatísticas básicas com Pillow e NumPy."""

from __future__ import annotations

from typing import Dict, Union

import numpy as np
from PIL import Image


def basic_image_stats(img: Image.Image) -> Dict[str, Union[int, float]]:
    """Retorna largura, altura e média RGB da imagem.

    Args:
        img: Objeto ``PIL.Image.Image`` já aberto.

    Returns:
        Dicionário com chaves ``largura``, ``altura`` e ``media_rgb``.
    """
    arr = np.array(img.convert("RGB"), dtype=np.float32)
    return {
        "largura": img.width,
        "altura": img.height,
        "media_rgb": float(arr.mean()),
    }
