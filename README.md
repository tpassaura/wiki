# Wikipedia-like Online Encyclopedia

This project is a Wikipedia-like online encyclopedia built using Django and Markdown. It allows users to view, search, create, edit, and browse random encyclopedia entries.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd wiki`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the Django development server: `python manage.py runserver`
5. Open your web browser and visit: `http://localhost:8000`

## Features

### Entry Page

Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, will render a page displaying the contents of that encyclopedia entry.

- The content of the entry is obtained using the appropriate utility function.
- If an entry is requested that does not exist, the user will be presented with an error page indicating that the requested page was not found.
- If the entry exists, the user will be presented with a page displaying the content of the entry. The title of the page will include the name of the entry.

### Index Page

The index page lists all the encyclopedia entries, and clicking on any entry name will take the user directly to that entry page.

### Search

The search feature allows users to search for encyclopedia entries by typing a query into the search box in the sidebar.

- If the query matches the name of an encyclopedia entry exactly, the user will be redirected to that entry's page.
- If the query does not match any entry exactly, the user will be taken to a search results page displaying a list of all encyclopedia entries that contain the query as a substring.
- Clicking on any entry name in the search results page will take the user to that entry's page.

### New Page

Clicking "Create New Page" in the sidebar takes the user to a page where they can create a new encyclopedia entry.

- Users can enter a title for the page and, in a textarea, enter the Markdown content for the page.
- Users can save their new page by clicking a button.
- If an encyclopedia entry already exists with the provided title, the user will be presented with an error message.
- Otherwise, the encyclopedia entry will be saved to disk, and the user will be taken to the new entry's page.

### Edit Page

On each entry page, users can click a link to be taken to a page where they can edit that entry's Markdown content in a textarea.

- The textarea is pre-populated with the existing Markdown content of the page.
- Users can click a button to save the changes made to the entry.
- Once the entry is saved, the user will be redirected back to that entry's page.

### Random Page

Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion

On each entry's page, the Markdown content is converted to HTML before being displayed to the user.

## Technologies Used

- Django: a Python web framework
- Markdown: a lightweight markup language
- python-markdown2: a library for converting Markdown to HTML

## Acknowledgements

The project is based on the curriculum of CS50's Web Programming with Python and JavaScript course by Harvard University.

