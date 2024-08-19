import webbrowser

# Ask the user for the website
website = input("Which website would you like to visit? ")

# Check if the user added "https://" or "www"
if not website.startswith("https://") and not website.startswith("www."):
    website = "http://www." + website  # Add "http://www." if not provided

# Open the website in the default browser
webbrowser.open(website)