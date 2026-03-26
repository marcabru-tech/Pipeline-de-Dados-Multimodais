#!/usr/bin/env bash
# smoke_demo.sh – executa demo_flow e verifica que os parquets de saída existem.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROCESSED_DIR="${REPO_ROOT}/data/processed"

# Garante que o pacote seja encontrado mesmo sem pip install -e .
export PYTHONPATH="${REPO_ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"

echo "==> Executando demo_flow..."
python3 -c "from pipeline.flow import demo_flow; demo_flow()"

echo "==> Verificando arquivos parquet..."

for file in text_entities.parquet image_stats.parquet; do
    path="${PROCESSED_DIR}/${file}"
    if [ -f "${path}" ]; then
        echo "    OK: ${file}"
    else
        echo "    ERRO: ${file} não encontrado em ${PROCESSED_DIR}"
        exit 1
    fi
done

echo "==> Smoke test concluído com sucesso."
