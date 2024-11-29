import wikipedia


def get_wikipedia_page():
    while True:
        query = input("Enter a Wikipedia search term (or leave blank to exit): ")
        if not query:
            break

        try:
            # Use autosuggest=False to avoid automatic suggestions altering the search
            page = wikipedia.page(query, auto_suggest=False)
            print("\nTitle:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)
        except wikipedia.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")
            continue  # Optionally, let user try a more specific term from the options listed
        except wikipedia.PageError:
            print("Error: Page not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        print("\n")  # Print a newline for better separation between entries


if __name__ == "__main__":
    get_wikipedia_page()
