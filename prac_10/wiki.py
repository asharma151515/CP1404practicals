import wikipedia


def main():
    """Main function to interact with the Wikipedia API."""
    print("Welcome to the Wikipedia Search Tool!")
    print("Type a page title or search phrase (or press Enter to quit):")

    while True:
        # Get user input
        search_query = input("Search: ").strip()

        # Exit if the input is blank
        if not search_query:
            print("Goodbye!")
            break

        try:
            # Search for the page
            page = wikipedia.page(search_query)
            print(f"\nTitle: {page.title}")
            print(f"Summary: {page.summary}\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")
            print("Please be more specific.")
        except wikipedia.exceptions.PageError:
            print("Page not found. Please try a different search term.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
