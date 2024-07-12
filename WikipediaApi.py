import wikipediaapi

# Initialize the Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

# Get the page for "Python (programming language)"
page_py = wiki_wiki.page("Python (programming language)")

# Print the page title and summary
print("Page - Title: %s" % page_py.title)
print("Page - Summary: %s" % page_py.summary[0:60])

    # Page - Summary: Python is a widely used high-level programming language for