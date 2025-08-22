import math
import argparse
from datetime import datetime
from typing import List,Dict, Any

import httpx

class Config:
    def __init__(self, 
                 coins: List[str] = ["bitcoin","ethereum"] ,
                 fiat: str = 'inr',
                 lat: float = 28.6139,
                 lon: float =77.2090,
                 sys_intrval: float = 2.0,
                 crypto_interval: float = 20.0,
                 weather_interval: float = 600.0,
                 timeout: float = 10.0):
        
        self.coins = coins
        self.fiat = fiat.lower()
        self.lat = lat
        self.lon = lon
        self.sys_interval = sys_intrval
        self.crypto_interval = crypto_interval
        self.weather_interval = weather_interval
        self.timeout = timeout
        
        
    #---------------HELPER------------
    
def human_bytes(n: float |None) -> str:
        step =1024.0
        units = ["B","KB","MB","GB","TB"]
        i = 0
        
        while n >= step and i < len(units) - 1:
            n /= step
            i += 1
        return f"{n:.2f} {units[i]}"
    
    
def pct_str(v:float | None):
        if v is None or math.isnan(v):
            return "-"
        
        sign = "+" if v>= 0 else ""
        return f"{sign}{v: .2f}%"
    
    
def safe_get(d: Dict , *path , default = None):
        cur = d
        for p in path:
            if not isinstance(cur,dict) or p not in cur:
                return default
            
            cur = cur[p]
        
        return cur
        

class CryptoFetcher:
    URL = "https://api.coingecko.com/api/v3/simple/price"
    
    def  __init__(self,coins: List[str] , fiat: str , timeout: float  = 10.0):
            self.coins = coins
            self.fiat  = fiat
            self.timeout = timeout
    
    
    async def fetch(self) -> Dict[str,Any]:
        params = {
            'ids': ','.join(self.coins),
            'vs_currencies':self.fiat,
            "include_24hr_change": "true",
        }
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.get(self.URL , params=params)
            resp.raise_for_status()
            return resp.json()