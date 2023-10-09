import re
import time
from time import sleep
import bs4
from seleniumbase import Driver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from PrettyColorPrinter import add_printer

add_printer(1)


def obter_dataframe(query="*"):
    df = pd.DataFrame()
    while df.empty:
        df = get_df(
            driver,
            By,
            WebDriverWait,
            expected_conditions,
            queryselector=query,
            with_methods=True,
        )
    return df


driver = Driver(uc=True)
sleep(5)
driver.get("https://sports.bwin.com/pt-br/sports/futebol-4/aposta/brasil-33/brasileir%C3%A3o-a-102838")
sleep(5)
resultados =[]
try:
    while True:
        try:
            df=obter_dataframe('ms-event')
            df= df.aa_innerHTML.apply(bs4.BeautifulSoup).apply(lambda soup: [x.text.strip() for x in soup.find_all('div', {'class': 'participant-wrapper'})]+ [float(g) if re.match(r'^\d+\.\d+$', (g:=x.text.strip())) else pd.NA for x in soup.find_all('div', {'class': 'option-value'})][:3]).apply(pd.Series).dropna().rename( columns={0: 'team1_nome', 1: 'team2_nome' , 2: 'team1', 3: 'empate', 4: 'team2'}).astype({'team1': 'Float64', 'empate': 'Float64', 'team2': 'Float64'})
            resultados.append(df.assign(timestamp=time.time()))
            #sleep(5)
        except Exception as e:
            print(e)
except KeyboardInterrupt:
    pass
