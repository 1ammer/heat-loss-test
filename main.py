# src/main.py

from source.config import INPUT_FILEPATH, OUTPUT_FILEPATH, POPULATION_COLS, STATE_MAP
from source.pipeline import DemographicsPipeline

def main():
    """
    Main function to orchestrate the data processing pipeline.
    """
    print("--- Starting Demographics Data Pipeline ---")

    # 1. Initialize the pipeline with the state mapping configuration.
    pipeline = DemographicsPipeline(state_map=STATE_MAP)
    
    # 2. Run the pipeline with the remaining configurations.
    final_data = pipeline.run(
        input_path=INPUT_FILEPATH,
        output_path=OUTPUT_FILEPATH,
        agg_cols=POPULATION_COLS
    )
    
    print("\n--- Pipeline execution complete. ---")
    print("Final data tail:\n", final_data.tail())

if __name__ == "__main__":
    main()









