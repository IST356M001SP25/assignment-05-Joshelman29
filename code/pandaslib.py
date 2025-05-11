from datetime import datetime

def clean_currency(number: str) -> float:
    '''
    remove anything from the number that prevents it from being converted to a float
    '''    
    currency = float(str(number).replace(',', '').replace('$', ''))
    return currency

def extract_year_mdy(tstamp: str) -> int:
    '''
    use the datetime.strptime to parse the date and then extract the year
    Expected format: MM/DD/YYYY HH:MM:SS (e.g., "05/15/2023 14:30:00")
    Returns the year as an integer
    
    '''
    year = datetime.strptime(tstamp, '%m/%d/%Y %H:%M:%S').year
    return year

def clean_country_usa(item: str) ->str:
    '''
    This function should replace any combination of 'United States of America', USA' etc.
    with 'United States'
    '''
    possibilities = [
        'united states of america', 'usa', 'us', 'united states', 'u.s.'
    ]
    lower_item = item.lower().strip()
    
    # Check against all possible variations
    for variant in possibilities:
        if lower_item == variant:
            return "United States"
    
    # Return original if no match found
    return item


if __name__=='__main__':
    print("""
        Add code here if you need to test your functions
        comment out the code below this like before sumbitting
        to improve your code similarity score.""")

