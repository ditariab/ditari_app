from email import header
import time
import requests
import configparser

class Polygon_api():
    is_initiated = False
    __host = None
    __key = None
    __content_type = "application/json"

    @staticmethod
    def initiate_api(cred: configparser.ConfigParser) -> None:
        if Polygon_api.is_initiated:
            Polygon_api.is_initiated = True
            Polygon_api.__host = cred["host"]
            Polygon_api.__key = cred["key"]
    
    @staticmethod
    def initiate_api_parameters(host: str, key: str) -> None:
        cred = configparser.ConfigParser()
        cred.add_section("API Polygon")
        cred.set("API Polygon", "host", host)
        cred.set("API Polygon", "key", key)
        Polygon_api.initiate_api(cred["API Polygon"])

    @staticmethod
    def get_ticker(limit = 10):
        try_count = 0
        while try_count <= 5:
            try:
                http_ = f"{Polygon_api.__host}/v3/reference/tickers?limit={limit}"

                headers_ = {
                    "Accept": Polygon_api.__content_type,
                    "Authorization": f"Bearer {Polygon_api.__key}"
                }

                request_ = requests.get(url = http_, headers = headers_)

                request_.raise_for_status()
            except Exception as e:
                if try_count < 5:
                    try_count += 1
                    t = try_count*2
                    print(f"Failed, retry in {str(t)} seconds")
                    time.sleep(t)
            else:
                return request_.json()
