def fasl_aniqla(oy):
    oy = oy.lower()

    if oy in ["mart", "aprel", "may"]:
        return "Bahor"
    elif oy in ["iyun", "iyul", "avgust"]:
        return "Yoz"
    elif oy in ["sentabr", "oktabr", "noyabr"]:
        return "Kuz"
    elif oy in ["dekabr", "yanvar", "fevral"]:
        return "Qish"
    else:
        return "Xato: noto‘g‘ri oy!"
