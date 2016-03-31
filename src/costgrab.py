import productsites

class Product:
    def guessSite(link):

        return ""

    def getPrice(link, site=""):
        if not site:
            site = guessSite(link)
        if (site == "cdw"):
            return productsites.CDW.get(link)
        elif  (site == "newegg"):
            return productsites.Newegg.get(link)
        elif (site == "pcon"):
            return productsites.PCON.get(link)
        elif (site == "pcm"):
            return productsites.PCM.get(link)
        elif (site == "insight"):
            return productsites.Insight.get(link)
        elif (site == "prov"):
            return productsites.Prov.get(link)
        elif (site == "zones"):
            return productsites.Zones.get(link)
        else:
            return ""
