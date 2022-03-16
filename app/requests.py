from app import app
import urllib.request,json
from .models import quote

Quote=quote.Quote

# Getting the movie base url
base_url = app.config["QUOTES_API_BASE_URL"]

def get_quotes(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(category)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_results = None

        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']
            quote_results = process_results(quote_results_list)


    return quote_results