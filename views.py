from flask import Blueprint,render_template
import scraper


bynogame = scraper.bynogame()
oyunfor = scraper.oyunfor()
oyuneks = scraper.oyuneks()
kopazar = scraper.kopazar()


views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html",bynogame=bynogame,oyunfor=oyunfor,oyuneks=oyuneks,kopazar=kopazar)