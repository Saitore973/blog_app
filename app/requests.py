
import urllib.request,json
from .models import Quote



base_url = 'http://quotes.stormconsultancy.co.uk/random.json'
def get_random_quote():
    url = base_url
    response = urllib.request.urlopen(url)
    data= json.loads(response.read())
    quote_details=[]
    author = data.get('author')
    quote = data.get('quote')
    popular_quotes= Quote(author, quote)
    quote_details.append(popular_quotes)
    return quote_details