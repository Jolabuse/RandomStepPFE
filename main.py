import random
import time

import matplotlib.pyplot as plt

#impact entre -10 et 10

class News:
  def __init__(self, startTick, impact):
    self.startTick = startTick
    self.impact = impact
    self.endTick = startTick + 840


# f(x) = x/((x-0.5)²+0.75) -> fonction d'évolution d'impact des news

def newsEvolution(x):
    x = x/102.5
    return x / ((x - 0.5) ** 2 + 0.75)


def newsImpact(active_news, currentTick):
    final_impact = 0
    for i in range(len(active_news)):
        if active_news[i].endTick > currentTick:
            x = currentTick - active_news[i].startTick
            if i < 3:
                if active_news[i].impact > 0:
                    final_impact += (newsEvolution(x) / 10) \
                                    * (1 + active_news[i].impact/10)*(1-i/3)
                else:
                    final_impact -= (newsEvolution(x) / 10) \
                                    * (1 + (-1*active_news[i].impact)/10)*(1-i/3)

        else:
            active_news.pop()
            return newsImpact(active_news,currentTick)
    return final_impact


"""
note company entre -5 et 5, moins d'impact que l'état du marché
"""


def getGrowthProbability(noteCompany, newsCompany):
    growthProbability = 0.5
    growthProbability += newsCompany
    # console.log("Note Company")
    growthProbability += noteCompany/50
    return growthProbability


def getRand():
    rand = random.randint(0, 100) / 100
    return rand



def randStep(precedentStockPrice, noteCompany, currentTick, active_news):
    stockPrice = precedentStockPrice
    impact = newsImpact(active_news, currentTick)
    growthProbability = getGrowthProbability(noteCompany, impact)
    variation = random.gauss(0.5, 0.15) * precedentStockPrice / 120
    if getRand() < growthProbability:
        stockPrice += variation
    else:
        stockPrice -= variation
    return stockPrice


stockPrice = 50
assetEvolution = []
active_news = []
for i in range(200):
    """if i % 100 == 0:
        active_news.append(News(i, random.randint(-10,10)))"""
    if i == 500:
        active_news.append(News(i, -10))
        active_news.append(News(i, -10))
        active_news.append(News(i, -10))
    if i < 2000:
        stockPrice = randStep(stockPrice, 5, i, active_news)
    else:
        stockPrice = randStep(stockPrice, 0, i, active_news)
    assetEvolution.append(stockPrice)

plt.plot(assetEvolution)
plt.show()


