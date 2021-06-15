# Brady Gerber's Google Books CLI Collector

First draft completed June 16, 2021.

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

## Next Steps (Icebox)

- Refactor and break down search command algorithm and add loops to allow users to add more than just one book to their reading list.
- Store updated user data from the search command into the reading list found in the view command.
- Better account for user mistakes and error handling when searching for books - typing in "harry potter" with spaces, picking book #6 (algorithm is set to only return 5 books), and more.

## Questions Ahead of the Second Draft

- I used Click but first attempted making this with Argparse - are there other preferred python modules to help make similar CLI apps?
- I'm able to append the user-selected book to the list, but once the terminal restarts, that data is lost. Is there ever a way to save that data post-script only using CLI?

## The Developer

[Brady Gerber](https://github.com/bg-write) (Software Engineer & Music Journalist)

## Credits

Initial Click and Google Books API logic was made with references to a tutorial written by [Oyetoke Tobi Emmanuel](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df).
