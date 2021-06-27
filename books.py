# The Click python package is required to use this app: $ pip install click

# Full Click documentation: https://click.palletsprojects.com/en/8.0.x/
# Google Books API documentation: https://developers.google.com/books/docs/v1/getting_started

# To launch this app: $ python3 books.py

import click
import requests

# Start the reading list (populate it with one book to give the user a sense of the list and search format)
reading_list = [
    { "TITLE": "Eloquent JavaScript", "AUTHOR": "Marijn Haverbeke", "PUBLISHER" : "No Starch Press" },
]

@click.group()
# The message that displays on the Main page each time.
def main():
    """
    Welcome! \U0001F4DA This CLI app for querying Google Books was build by Brady Gerber using the Click python package. To use this app, in your terminal, type out "python3 books.py" and one of the below commands (EX: "python3 books.py view" or "python3 books.py search harry-potter 10").\n
    To search for a book, type in the book you want (replace spaces with dashes) and the number of books you want to return (up to 40 books per search).
    To exit: "ctrl + c."\n
    Happy reading!\n
    -B
    """
    pass

# The "view" command.
@main.command()
def view():
    """👀 View your reading list (we added one to start!)"""
    click.echo('_____________')
    click.echo(('Reading List').upper())
    # Reformat each book in our initial reading list for easier user viewing.
    for item in reading_list:
        click.echo(f'** "{item["TITLE"]}" by {item["AUTHOR"]}, published by {item["PUBLISHER"]}')
    click.echo('_____________')
    click.echo('')

# The "search" command.
@main.command()
@click.argument('user_search')
@click.argument('max_results')
def search(user_search, max_results):
    """🔎 Search for books (replace spaces with dashes, return up to 40 books per search)"""
    # Make the Google Books API request after the user types in their "user_search" (EX:"python3 books.py search harry-potter")
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
    
    # For each of the books called by the API, reformat them to only return the title, author(s), and publisher, and return default data if any information is missing ("~XXX not available~") ...
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
    
    # V2 UPDATE FOR LOOP TO RETURN EVERYTHING
    for item in combine_dict:
        n += 1
        click.echo(f'{n}: "{item["TITLE"]}" by {item["AUTHOR"]}, published by {item["PUBLISHER"]}')
        click.echo('')
    click.echo('********************************')
    click.echo('')

    # The user selects a book from the books returned above ...
    user_pick = (int(input("Nice! Which book would you like to add to your list? (Please Enter a number): ")))
    click.echo('')

    # ... We confirm the book that user selects ...
    user_selection = combine_dict[user_pick-1]
    click.echo(f'Great! You picked No. {user_pick}: "{user_selection["TITLE"]}"')
    
    # ... And then we append that selection to our reading list
    reading_list.append(user_selection)
    click.echo('We\'ve added it to your reading list.')
    click.echo('_____________')
    click.echo(' ')

    # Will delete the below later, but now just good to have for reference ...
    click.echo(('Reading List').upper())
    for item in reading_list:
        click.echo(f'** "{item["TITLE"]}" by {item["AUTHOR"]}, published by {item["PUBLISHER"]}')

if __name__ == "__main__":
    main()