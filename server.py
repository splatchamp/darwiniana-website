from flask import Flask, render_template, url_for
from datetime import datetime
import requests
from quotes_info import QuotesInfo
from bs4 import BeautifulSoup
import random

app = Flask(__name__)
current_year = datetime.now().year

@app.route("/")
def home():
    #Using BeautifulSoup to scrape and edit darwin quotes from goodreads.com
    darwin_quotes_html = requests.get("https://www.goodreads.com/author/quotes/12793.Charles_Darwin").text
    soup = BeautifulSoup(darwin_quotes_html, 'html.parser')
    quotes = soup.find_all('div', {"class": "quoteText"})

    darwin_quotes = []
    for quote in quotes:
        quote = quote.text
        if len(quote) < 300:
            quote = quote.replace("―", "").replace("Charles Darwin,", "").replace("CHARLES DARWIN", "") \
                .replace("Charles Darwin", "").replace("The Autobiography of  1809–82", "") \
                .replace("The Descent of Man", "").replace("The Origin of Species", "").replace("The Life & Letters of", "") \
                .replace("The Correspondence of  Volume 9: 1861", "").replace("Voyage of the Beagle", "") \
                .replace("Notebooks", "").replace("The Expression of the Emotions in Man and Animals", "").strip()
            darwin_quotes.append(quote)
    darwin_quote = random.choice(darwin_quotes)

    #Using npoint.io json bin to access quotes for carousel
    quotes_json = requests.get("https://api.npoint.io/53dbb4f12d637faf333c").json()
    singer_quote_info = QuotesInfo(quotes_json[0]["name"], quotes_json[0]["quote"])
    trivers_quote_info = QuotesInfo(quotes_json[1]["name"], quotes_json[1]["quote"])
    pinker_quote_info = QuotesInfo(quotes_json[2]["name"], quotes_json[2]["quote"])

    return render_template("index.html", current_year=current_year, darwin_quote=darwin_quote,
                           singer_quote_info=singer_quote_info, trivers_quote_info=trivers_quote_info,
                           pinker_quote_info=pinker_quote_info)

@app.route("/natural-selection")
def natural_selection():
    return render_template("natural_selection.html", current_year=current_year)

@app.route("/evolutionary-mountain")
def evolutionary_mountain():
    return render_template("evolutionary_mountain.html", current_year=current_year)

@app.route("/animal-sentience")
def animal_sentience():
    return render_template("animal_sentience.html", current_year=current_year)

@app.route("/evolutionary-dentistry")
def evolutionary_dentistry():
    return render_template("evolutionary_dentistry.html", current_year=current_year)

@app.route("/a-cosmic-morality")
def a_cosmic_morality():
    return render_template("a_cosmic_morality.html", current_year=current_year)

@app.route("/the-religious-sense")
def the_religious_sense():
    return render_template("the_religious_sense.html", current_year=current_year)

@app.route("/attributions")
def attributions():
    return render_template("attributions.html", current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)