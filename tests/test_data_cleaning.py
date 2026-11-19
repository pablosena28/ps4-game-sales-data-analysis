import pandas as pd

from src.data_cleaning import prepare_games_data, temporal_analysis_sample


def test_prepare_games_data_preserves_missing_year_and_flags_sales():
    sample = pd.DataFrame({
        "Game": ["A", "B"],
        "Year": [2017, None],
        "Genre": ["Action", "Sports"],
        "Publisher": ["Studio", None],
        "North America": [1.0, 0.0],
        "Europe": [2.0, 0.0],
        "Japan": [0.1, 0.0],
        "Rest of World": [0.5, 0.0],
        "Global": [3.6, 0.0],
    })
    result = prepare_games_data(sample)
    assert result.loc[0, "Sales Recorded"]
    assert not result.loc[1, "Sales Recorded"]
    assert result.loc[1, "Publisher"] == "Unknown"
    assert pd.isna(result.loc[1, "Year"])


def test_temporal_analysis_sample_excludes_2019_2020():
    sample = pd.DataFrame({
        "Game": ["A", "B", "C"],
        "Year": [2018, 2019, 2020],
        "Genre": ["Action"] * 3,
        "Publisher": ["Studio"] * 3,
        "North America": [1.0, 0.0, 0.0],
        "Europe": [1.0, 0.0, 0.0],
        "Japan": [0.0, 0.0, 0.0],
        "Rest of World": [0.0, 0.0, 0.0],
        "Global": [2.0, 0.0, 0.0],
    })
    result = temporal_analysis_sample(sample)
    assert result["Year"].tolist() == [2018]