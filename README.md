Neste vídeo, você aprenderá como criar um código eficiente para raspar dados de odds do site Bwin.com em tempo real, 
permitindo que você se envolva na emocionante estratégia de arbitragem de apostas. 
Com o código Python fornecido e explicado passo a passo, 
você poderá coletar informações cruciais de odds a cada 0.6 segundos, 
tornando-se extremamente ágil na tomada de decisões de apostas.

Nosso "código de base" que usamos em todos os vídeos
```python
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
```

## Pacotes para instalar: pip install selenium seleniumbase PrettyColorPrinter a-selenium2df bs4 lxml

