"""Funções de preparação do dataset de vendas de jogos de PS4."""

from __future__ import annotations

import pandas as pd

REGION_COLUMNS = ["North America", "Europe", "Japan", "Rest of World"]


def prepare_games_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cria variáveis auxiliares sem imputar ano ou publisher ausentes."""
    data = df.copy()
    data["Year"] = pd.to_numeric(data["Year"], errors="coerce").astype("Int64")
    data["Publisher"] = data["Publisher"].fillna("Unknown")
    data["Sales Recorded"] = data["Global"] > 0
    data["Regional Sum"] = data[REGION_COLUMNS].sum(axis=1).round(2)
    data["Global Difference"] = (data["Global"] - data["Regional Sum"]).round(2)
    return data


def temporal_analysis_sample(df: pd.DataFrame) -> pd.DataFrame:
    """Seleciona 2013–2018 para a análise temporal principal."""
    data = prepare_games_data(df)
    return data[data["Year"].between(2013, 2018)].copy()