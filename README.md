# Brady Gerber's Google Books CLI Collector

First draft completed June 16, 2021. Worked on this app locally before creating this repo on June 15th.

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

- Refactor and break down the search command algorithm.
- Add loops to the search command to allow users to add more than just one book to their reading list; encountered a bug here and ran out of time to address this for the first draft.
- Store updated user data from the search command into the reading list found in the view command.
- Better account for user mistakes and error handling while searching for books - typing in "harry potter" with spaces, picking book #6 (algorithm is set to only return 5 books), and more.

## Questions Ahead of the Second Draft

- I used Click, but I first attempted to make this CLI app with Argparse - are there other preferred python modules to help make similar CLI apps? Is the preference not to use any when it comes to Python?
- I'm able to append the user-selected book to the list, but once the terminal restarts, that data is lost. Is there a way to save that data post-script only using the CLI?

## The Developer

[Brady Gerber](https://github.com/bg-write): Software Engineer & Music Journalist

## Credits

The initial Click and Google Books API logic was made with references to a tutorial written by [Oyetoke Tobi Emmanuel](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df).
