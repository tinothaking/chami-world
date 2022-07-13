import get_link as gl
import pandas_scraping as ps
import radar_from_arrs as ra


def generate(playerName):
    url = gl.getFBRefLink(playerName)
    arrs = ps.player(url)
    ra.radar(arrs[0], arrs[1], arrs[2])
