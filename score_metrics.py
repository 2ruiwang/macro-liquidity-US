def score_walcl(value):
    if value > 8.5:
        return 3, "Fed balance sheet expanding – QE mode."
    elif value > 7.5:
        return 2, "Fed balance sheet stable or slowly declining."
    elif value > 7.0:
        return 1, "QT in progress, liquidity cautiously declining."
    else:
        return 0, "QT accelerating – liquidity contraction risk."

def score_tga(value):
    if value < 300:
        return 3, "Treasury injecting liquidity via spending."
    elif value <= 500:
        return 2, "TGA at normal range."
    elif value <= 700:
        return 1, "TGA buildup draining liquidity."
    else:
        return 0, "TGA at high levels – strong liquidity drain."

def score_wresbal(value):
    if value > 3.0:
        return 3, "Ample bank reserves."
    elif value > 2.5:
        return 2, "Neutral reserve levels."
    elif value > 1.4:
        return 1, "Watch for stress – reserve cushion thinning."
    else:
        return 0, "Below critical – funding stress likely."

def score_rrp(value):
    if value > 1000:
        return 3, "MMFs holding excess liquidity."
    elif value > 300:
        return 2, "Moderate MMF cash parked."
    elif value > 100:
        return 1, "Liquidity being deployed."
    else:
        return 0, "MMF liquidity exhausted – market exposed."

def score_sofr(value):
    if value < 5.0:
        return 3, "Overnight funding costs low – easy conditions."
    elif value <= 5.2:
        return 2, "Funding costs stable."
    elif value <= 5.5:
        return 1, "Funding tight – watch repo stress."
    else:
        return 0, "Repo rates spiking – system pressure rising."

def score_hyg_trend(change_5d):
    if change_5d > 1.0:
        return 3, "High-yield rally – credit risk low."
    elif change_5d > -1.0:
        return 2, "Credit conditions neutral."
    elif change_5d > -2.0:
        return 1, "Credit stress building."
    else:
        return 0, "Credit markets stressed – HYG breakdown."
