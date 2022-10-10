#------------------------------
#GICS sectors:
#GICS_10_Utilities: 5510
stages_ = {
    "recovery": {
        "GICS_3_Industrials": ["2010", "2020", "2030"],
        "GICS_8_Information_Technology": ["4510", "4520", "4530"],
        "GICS_9_Communication_Services": ["5010", "5020"],
        "GICS_7_Financials": ["4010", "4020", "4030"],
        "GICS_11_Real_Estate": ["6010"]
    },
    "expansion": {
        "GICS_1_Energy": ["1010"],
        "GICS_3_Industrials": ["2010", "2020", "2030"],
        "GICS_4_Consumer_Discretionary": ["2510", "2520", "2530," "2550"],
        "Paper_And_Forest_Products": ["151050"]
    },
    "slowdown": {
        "GICS_2_Materials": ["1510"],
        "GICS_6_Health_Care": ["3510", "3520"],
        "GICS_8_Information_Technology": ["4510", "4520", "4530"],
        "GICS_9_Communication_Services": ["5010", "5020"],
        "GICS_11_Real_Estate": ["6010"],
        "Aerospace_And_Defense": ["201010"]
    },
    "contraction": {
        "GICS_4_Consumer_Discretionary": ["2510", "2520", "2530," "2550"],
        "GICS_5_Consumer_Staples": ["3010", "3020", "3030"],
        "GICS_6_Health_Care": ["3510", "3520"],
        "Aerospace_And_Defense": ["201010"]
    }
}

class Macro_analysis():
    def __init__(self, Two_Prev_GDP, Prev_GDP, This_GDP, Two_Prev_CPI, Prev_CPI, This_CPI) -> None:
        GDP_Change = This_GDP-Prev_GDP #change of GDP
        self.GDP_Change_Rate = (GDP_Change/Prev_GDP)/((Prev_GDP-Two_Prev_GDP)/Two_Prev_GDP) #Rate of change of GDP

        CPI_Change = This_CPI-Prev_CPI #change of CPI
        self.CPI_Change_Rate = (CPI_Change/Prev_CPI)/((Prev_CPI-Two_Prev_CPI)/Two_Prev_CPI) #Rate of change of CPI

    def get_market_stage(self):
        if (self.GDP_Change_Rate>0 and self.CPI_Change_Rate<0): #1 - Recovery
            print("Focus on European, high yield, growing stocks")
            return stages_["recovery"]
            
        if (self.GDP_Change_Rate>0 and self.CPI_Change_Rate>0): #2 - Expansion
            print("Focus on European, high yield stocks")
            return stages_["expansion"]

        if (self.GDP_Change_Rate<0 and self.CPI_Change_Rate>0): #3 - Slowdown
            print("Focus on American, low volatility stocks")
            return stages_["slowdown"]
            
        if (self.GDP_Change_Rate<0 and self.CPI_Change_Rate<0): #4 - Contraction
            print("Focus on American, low volatility stocks")
            return stages_["contraction"]