# The Click python package is required to use this app: $ pip install click

# Full Click documentation: https://click.palletsprojects.com/en/8.0.x/
# Google Books API documentation: https://developers.google.com/books/docs/v1/getting_started

# To launch this app: $ python3 books.py

import click
import requests
import csv
from csv import DictWriter

@click.group()
# The message that displays when you Enter "python3 books.py"
def main():
    """
    Welcome! \U0001F4DA This simple CLI app for querying Google Books was build by Brady Gerber with the Click python package. To use this app, in your terminal, type out "python3 books.py" and one of the below commands (EX: "python3 books.py view" or "python3 books.py search harry-potter 10").\n
    To search for a book, type in what you wish to find (replace spaces with dashes) and the number of books you want to return (up to 40 books per search).
    To exit: "ctrl + c."\n
    Happy reading!\n
    -B
    """
    pass

# The "view" command.
# ICEBOX: update this so I may view reading_list.py, instead of reading_list above.
@main.command()
def view():
    """👀 View your reading list"""
    click.echo('_____________')
    click.echo(('Reading List:').upper())
    # Connect reading_list.txt to books.py via csv ...
    with open('reading_list.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                click.echo(f'\t {line_count}. "{row[0]}" by {row[1]}, published by {row[2]}')
                line_count += 1
        click.echo('')
        click.echo(f'Counted {line_count-1} book(s).')
    click.echo('')
    click.echo('To add to your list, Enter "Python3 books.py search {book-title} {# of books to return, up to 40 per search}"')
    click.echo('_____________')
    click.echo('')

# The "search" command.
@main.command()
@click.argument('user_search')
@click.argument('max_results')
def search(user_search, max_results):
    """🔎 Search for books (replace spaces with dashes, return up to 40 books per search)"""
    # Make the Google Books API request after the user types in their "user_search" and "max_results"
    api = "https://www.googleapis.com/books/v1/volumes?"
    query = {'q': {user_search}, 'maxResults': {max_results}}

    # printing off our query
    click.echo('********************************')
    click.echo(f'Your top {max_results} results for "{user_search}" ...')
    click.echo('')
    response = requests.get(api, params=query)
    json_response = response.json()
    json_response_books = json_response["items"]
    
    # Start a search with no books in it that we'll populate soon.
    combine_dict = []
    
    # For each book called by the API (json_response_books), reformat to only return the title, author(s), and publisher, and return default data if any information is missing ("~XXX not available~") ...
    for item in json_response_books:
        n = 0
        try:
            title = item["volumeInfo"]['title']
        except KeyError:
            title = '~Title not available]~'
        try:
            author = " & ".join(item["volumeInfo"]['authors'])
        except KeyError:
            author = '~Author not available~'
        try:
            publisher = item["volumeInfo"]['publisher']
        except KeyError:
            publisher = '~Publisher not available~'
        API_reading_list = {"TITLE" : title, "AUTHOR": author, "PUBLISHER": publisher}
        
        # ... And then add these new books to our empty combine_dict.
        combine_dict.append(API_reading_list)
    
    # And then actually print off our reading list in a more readable way.
    for item in combine_dict:
        n += 1
        click.echo(f'{n}: "{item["TITLE"]}" by {item["AUTHOR"]}, published by {item["PUBLISHER"]}')
        click.echo('')
    click.echo('********************************')
    click.echo('')

    # The user selects a book from the books returned above ...
    user_pick = (int(input("Excellent! Which book would you like to add? (Please Enter a number): ")))
    click.echo('')

    # ... We confirm the book that user selects.
    user_selection = combine_dict[user_pick-1]
    click.echo(f'Great! You picked No. {user_pick}: "{user_selection["TITLE"]}"')
    click.echo('')

    # If we find duplicates in your choice, exit out of script ...
    def check_duplicates(file_name):
        with open(file_name, 'r') as f:
            for row in f:
                if user_selection['TITLE'] in row:
                    click.echo('But hey now, this book is already in your list. Please search for another title.')
                    click.echo('')
                    exit()
    check_duplicates('reading_list.txt')

    # ... Otherwise, create our field_names to help with our following append function ...
    field_names = ['TITLE', 'AUTHOR', 'PUBLISHER']
    
    # ... And then we append that selection to our reading list
    def append_dict_as_row(file_name, dict_of_elem, field_names):
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            dict_writer = DictWriter(write_obj, fieldnames=field_names)
            # Add dictionary as row in the csv
            dict_writer.writerow(dict_of_elem)
    append_dict_as_row('reading_list.txt', user_selection, field_names)

    # ... And then confirm that the add was successful ...
    click.echo('We\'ve added it to your list.')
    click.echo('')
    click.echo('To view your updated list, please Enter "python3 books.py view".')
    click.echo('_____________')
    click.echo(' ')
            
if __name__ == "__main__":
    main()