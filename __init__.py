import json
from api_handlers.polygon_api import Polygon_api
from macro import Macro_analysis
import configparser

def main():
    #config = read_config()
    #Polygon_api.initiate_api(config["API_Polygon"])
    
    #------------------------------
    #Macro data
    Two_Prev_GDP = 2094 #GDP 2 quarters ago
    Prev_GDP = 2100 #GDP 1 quarter ago
    This_GDP = 2143 #GDP this quarter
    Two_Prev_CPI = 0.5 #CPI 2 quarters ago
    Prev_CPI = 1 #CPI 1 quarter ago
    This_CPI = 2 #CPI this quarter

    macro_analysis_ = Macro_analysis(Two_Prev_GDP, Prev_GDP, This_GDP, Two_Prev_CPI, Prev_CPI, This_CPI)
    stage = macro_analysis_.get_market_stage()
    for sector_ in stage:
        codes = stage[sector_]
        print(f"{sector_}: {codes}")


def update_ticker_data():
    dict_ = {}
    for tickers in Polygon_api.get_all_tickers():
        for ticker in tickers["results"]:
            tag = ticker["ticker"]
            dict_[tag] = ticker
    
    file_ = f"data_storage\\all_tickers.json"
    with open(file_, "w") as file:
        json.dump(dict_, file, indent=4)

def read_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config

if __name__ == "__main__":
    main()