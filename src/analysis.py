"""Executa a análise descritiva do dataset de vendas de jogos de PS4."""

from pathlib import Path
import pandas as pd
from src.data_cleaning import REGION_COLUMNS, prepare_games_data, temporal_analysis_sample

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "ps4_games_sales.csv"


def main() -> None:
    raw = pd.read_csv(DATA_PATH)
    df = prepare_games_data(raw)

    print("=== VISÃO GERAL ===")
    print(f"Registros: {len(df)}")
    print(f"Jogos únicos: {df['Game'].nunique()}")
    print(f"Gêneros: {df['Genre'].nunique()}")
    print(f"Publishers identificados: {raw['Publisher'].nunique()}")
    print(f"Vendas globais somadas: {df['Global'].sum():.2f}")

    print("\n=== QUALIDADE DOS DADOS ===")
    print(f"Ano ausente: {raw['Year'].isna().sum()}")
    print(f"Publisher ausente: {raw['Publisher'].isna().sum()}")
    print(f"Vendas globais iguais a zero: {(raw['Global'] == 0).sum()}")
    print(f"Duplicatas completas: {raw.duplicated().sum()}")

    print("\n=== TOP 10 JOGOS ===")
    print(df.nlargest(10, "Global")[["Game", "Year", "Genre", "Publisher", "Global"]].to_string(index=False))

    print("\n=== VENDAS POR REGIÃO ===")
    print(df[REGION_COLUMNS].sum().sort_values(ascending=False).round(2))

    print("\n=== TOP GÊNEROS ===")
    print(df.groupby("Genre")["Global"].agg(["count", "sum", "mean"]).sort_values("sum", ascending=False).head(10).round(2))

    print("\n=== TOP PUBLISHERS ===")
    print(df[df["Publisher"] != "Unknown"].groupby("Publisher")["Global"].agg(["count", "sum", "mean"]).sort_values("sum", ascending=False).head(10).round(2))

    print("\n=== JANELA TEMPORAL 2013–2018 ===")
    temporal = temporal_analysis_sample(raw)
    print(temporal.groupby("Year")["Global"].agg(["count", "sum", "mean"]).round(2))


if __name__ == "__main__":
    main()