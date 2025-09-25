# src/pipeline.py

import pandas as pd
import numpy as np
from typing import Dict, List, Optional

class DemographicsPipeline:
    """
    Encapsulates the data processing pipeline for county demographics data.
    Each method represents an atomic step in the process.
    """
    def __init__(self, state_map: Dict[str, str]):
        self.state_map = state_map
        self.df: Optional[pd.DataFrame] = None
        self.aggregated_df: Optional[pd.DataFrame] = None

    def _load_data(self, filepath: str) -> None:
        """(Atomic) Loads data from a given filepath."""
        print(f"STEP 1: Loading dataset from '{filepath}'...")
        self.df = pd.read_csv(filepath)
        print("Original Shape:", self.df.shape)

    def _clean_column_names(self) -> None:
        """(Atomic) Cleans the DataFrame's column names."""
        print("\nSTEP 2: Cleaning column names...")
        self.df.columns = (
            self.df.columns.str.strip()
                         .str.replace(" ", "_", regex=False)
                         .str.replace("[^0-9a-zA-Z_]", "", regex=True)
        )

    def _handle_noisy_values(self) -> None:
        """(Atomic) Replaces placeholders with NaN and converts types."""
        print("\nSTEP 3: Handling noisy values...")
        self.df.replace([-1, " "], np.nan, inplace=True)
        for col in self.df.columns:
            self.df[col] = pd.to_numeric(self.df[col], errors="ignore")

    def _impute_missing_values(self) -> None:
        """(Atomic) Imputes missing values for numeric and categorical columns."""
        print("\nSTEP 4: Detecting and imputing NaN values...")
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        
        categorical_cols = self.df.select_dtypes(include="object").columns
        for col in categorical_cols:
            self.df[col].fillna(self.df[col].mode()[0], inplace=True)
        
    def _aggregate_by_state(self, agg_cols: List[str]) -> None:
        """(Atomic) Aggregates population data by state."""
        print(f"\nSTEP 5: Aggregating by 'State'...")
        self.aggregated_df = self.df.groupby("State")[agg_cols].sum().reset_index()

    def _map_state_names(self) -> None:
        """(Atomic) Converts state abbreviations to full names."""
        print("\nSTEP 6: Converting State abbreviations to full names...")
        self.aggregated_df["State"] = self.aggregated_df["State"].map(self.state_map)
        
    def _add_national_total(self, agg_cols: List[str]) -> None:
        """(Atomic) Appends a national total row to the aggregated data."""
        print("\nSTEP 7: Adding national total row...")
        total_row = pd.DataFrame({
            "State": ["United States"],
            agg_cols[0]: [self.aggregated_df[agg_cols[0]].sum()],
            agg_cols[1]: [self.aggregated_df[agg_cols[1]].sum()]
        })
        self.aggregated_df = pd.concat([self.aggregated_df, total_row], ignore_index=True)

    def _save_data(self, filepath: str) -> None:
        """(Atomic) Saves the final aggregated DataFrame to a CSV."""
        self.aggregated_df.to_csv(filepath, index=False)
        print(f"\n:white_check_mark: Aggregated dataset saved as '{filepath}'")

    def run(self, input_path: str, output_path: str, agg_cols: List[str]) -> pd.DataFrame:
        """
        Executes the full data processing pipeline in sequence.
        
        Args:
            input_path (str): The path to the source data file.
            output_path (str): The path to save the processed file.
            agg_cols (List[str]): A list of columns to aggregate.
            
        Returns:
            pd.DataFrame: The final, aggregated DataFrame.
        """
        self._load_data(input_path)
        self._clean_column_names()
        self._handle_noisy_values()
        self._impute_missing_values()
        self._aggregate_by_state(agg_cols=agg_cols)
        self._map_state_names()
        self._add_national_total(agg_cols=agg_cols)
        self._save_data(output_path)
        
        return self.aggregated_df









