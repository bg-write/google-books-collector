# Brady Gerber's Google Books CLI Collector

First draft completed June 16, 2021. Second draft completed June 29. Worked on this app locally before creating this repo on June 15th.

## Getting Started

1. Install the Click python package: "pip install click"
2. View the app: "python3 books.py"
3. Follow the prompted instructions
4. Enjoy!

## Technologies Used

- Python
- [Click](https://click.palletsprojects.com/en/8.0.x/)
- [Google Books API](https://developers.google.com/books/docs/v1/getting_started)
- GitHub
- Git
- Visual Studio Code
- Google
- Coffee
- Breaks

## Updates Made for the Second draft
- Cleaned up the overall copy and code to be less repetitive and more useful in guiding users from start to end.
- Updated Author information to return multiple names by removing [0] author index and adding a join method to combine multiple book authors with “&”. (Tested this with a search for “taco” and seeing book #2.)
- Added a for loop to make the book search more flexible to return any number of books specified by the user (the Google Books API can return up to 40 books per query). This code is easy to adjust and hardcode if we only wish to consistently return 5 books per search no matter what.
- Imported csv and DictWriter to append and store books in “reading_list.txt” file rather than in-memory. I chose csv for its ease and for its ability to be used with other applications as needed. (I considered installing Pandas, yet I felt it wasn’t necessary for this simple CLI.)
- Broke down the overall search function into smaller functions: "search" became "search", "reformat_search", "print_search", "check_duplicates", and "append_dict_as_row".

## Next Steps (Icebox)

- Further refactor and break down the search command algorithm (can always simplify).
- Add the ability to remove specific books from current reading list (a "remove" ability was not explicitly requested for this technical assessment).
- Better account for user mistakes and error handling while searching for books. Ex. typing "harry potter" instead of "harry-potter", searching for more than 40 books in one search, adding the same row twice instead of just the same book title twice (and letting a user add another book instead of exiting the script).

## The Developer

[Brady Gerber](https://github.com/bg-write), and thank you for reading this README!

## Credits

The initial Click and Google Books API logic was made with references to a tutorial written by [Oyetoke Tobi Emmanuel](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df).
