from data_extraction import get_fear_greed_index, get_sp500_data, get_inflation_data
from data_cleaning import clean_fear_greed_data, clean_sp500_data, clean_inflation_data, merge_all_data
from database import save_market_sentiment_data, get_recent_data

def run_complete_pipleline():
    #STEP 1: EXTRACT DATA FROM APIs:
    print("Step 1: Extracting data from APIs:")
    raw_fgi = get_fear_greed_index()
    raw_sp500 = get_sp500_data(days=30)
    raw_inflation = get_inflation_data()

    #STEP 2: CLEAN DATA:
    print("Step 2: clea data")
    clean_fgi = clean_fear_greed_data(raw_fgi)
    clean_sp500 = clean_sp500_data(raw_sp500)
    clean_inflation = clean_inflation_data(raw_inflation)

    final_data = merge_all_data(clean_fgi, clean_sp500, clean_inflation)

    if final_data is None or final_data.empty:
        print("Pipeline failed. No data to process.")
        return False

    #STEP 3: LOAD DATA to PostgreSQL
    print("Step 3: Loading data to PostgreSQL")
    save_success = save_market_sentiment_data(final_data)

    if save_success:
        print("Pipeline completed successfully!")
        get_recent_data(days=3)
        return True
    else:
        print("Pipeline failed at database save step.")
        return False
    
def main():
    try:
        success = run_complete_pipleline()
        if success:
            print("Pipeline executed successfully!")
        else:
            print("Pipeline failed!")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__=="__main__":
    main()