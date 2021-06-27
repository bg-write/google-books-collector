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
# ICEBOX: I want to refactor this very long function into smaller functions; I first wanted to get this working as a whole before breaking it down and simplifying.
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
    
    # For each of the books called by the API, reformat them to only return the title, author(s), and publisher, and return default data if any information is missing ("~X not available~") ...
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


    # Now save everything out of the above loop, and return None if there are less than 5 books available ...
    # try:
    #     search_result_1 = combine_dict[0]
    # except IndexError:
    #     search_result_1 = None
    # try:
    #     search_result_2 = combine_dict[1]
    # except IndexError:
    #     search_result_2 = None
    # try:
    #     search_result_3 = combine_dict[2]
    # except IndexError:
    #     search_result_3 = None
    # try:
    #     search_result_4 = combine_dict[3]
    # except IndexError:
    #     search_result_4 = None
    # try:
    #     search_result_5 = combine_dict[4]
    # except IndexError:
    #     search_result_5 = None

    # ... And return the necessary search results, reformatted as their own dictionaries.
    # None if search_result_1 == None else click.echo(f'1: "{search_result_1["TITLE"]}" by {search_result_1["AUTHOR"]}, published by {search_result_1["PUBLISHER"]}')
    # None if search_result_2 == None else click.echo(f'2: "{search_result_2["TITLE"]}" by {search_result_2["AUTHOR"]}, published by {search_result_2["PUBLISHER"]}')
    # None if search_result_3 == None else click.echo(f'3: "{search_result_3["TITLE"]}" by {search_result_3["AUTHOR"]}, published by {search_result_3["PUBLISHER"]}')
    # None if search_result_4 == None else click.echo(f'4: "{search_result_4["TITLE"]}" by {search_result_4["AUTHOR"]}, published by {search_result_4["PUBLISHER"]}')
    # None if search_result_5 == None else click.echo(f'5: "{search_result_5["TITLE"]}" by {search_result_5["AUTHOR"]}, published by {search_result_5["PUBLISHER"]}')
    # click.echo('********************************')
    # click.echo('')

    # # ICEBOX Break down into a smaller function
    # # The user selects a book from the 5 books returned above ...
    # user_pick = (int(input("Nice! Which book would you like to add to your list? (Please Enter 1, 2, 3, 4, or 5): ")))
    # click.echo('')
    
    # # ... We confirm the selection (1, 2, 3, 4, or 5) ...
    # choices = [search_result_1, search_result_2, search_result_3, search_result_4, search_result_5]
    # user_selection = choices[user_pick-1]
    
    # # ... And then we append that selection to our reading list!
    # reading_list.append(user_selection)
    # click.echo(f'Great! You picked No. {user_pick}: "{user_selection["TITLE"]}"')
    # click.echo('_____________')
    # click.echo(('Reading List').upper())
    # for item in reading_list:
    #     click.echo(f'** "{item["TITLE"]}" by {item["AUTHOR"]}, published by {item["PUBLISHER"]}')
    # click.echo('_____________')
    # click.echo('')

    #ICEBOX I am able to append the user selected book to this list, but once the terminal restarts, that data is lost, and I can only add one book. I need to add in some type of loop to continue the process of appending more books to the reading list.
    #ICEBOX Account for user going outside search parameters - typing in "harry potter" with spaces, or picking book #6.

if __name__ == "__main__":
    main()