# Show a friendly welcome message
print("Welcome to the HTML5 template generator!")

# Ask user to pick a website language
print("What is the language of the site?")
print("Choose one of the following options:")
print("1. English")
print("2. Dutch")
print("3. German")
print("4. French")
print("5. Spanish")

# Store language codes for easy lookup
language_codes = {
    "1": "en",
    "2": "nl",
    "3": "de",
    "4": "fr",
    "5": "es"
}

# Keep asking until user picks a valid language option
while True:
    choice = input("Enter your choice (1-5): ")
    if choice in language_codes:
        selected_language = language_codes[choice]
        break
    else:
        print("Invalid choice. Please try again.")

# Collect basic website information
# Get the main title for the website
print("\nWhat is the title of your website?")
page_title = input("Enter title: ")

# Get the author's name for meta tags
print("\nWho is the author of the site?")
author = input("Enter author: ")

# Get website description for search engines
print("\nWhat is the description of the site?")
description = input("Enter description: ")

# Get keywords for search engine optimization
print("\nWhat are the keywords of the site?")
keywords = input("Enter keywords: ")        

# Let user choose character encoding
print("\nChoose character encoding: ")
print("1. UTF-8")
print("2. ISO-8859-1")
print("3. Windows-1252")

# Store encoding options for easy lookup
encoding_options = {
    "1": "UTF-8",
    "2": "ISO-8859-1",
    "3": "Windows-1252"
}   

# Keep asking until user picks a valid encoding option
while True:
    choice = input("Enter your choice (1-3): ")
    if choice in encoding_options:
        selected_encoding = encoding_options[choice]
        break
    else:
        print("Invalid choice. Please try again.")

# Ask about optional features
# Check if user wants social media sharing tags
print("\nDo you want to add basic social media meta tags? (y/n)")
social_media = input().lower() == 'y'

# Check if user wants a CSS file
print("\nDo you want to add basic CSS file? (y/n)")
css = input().lower() == 'y'

# Check if user wants a JavaScript file
print("\nDo you want to add basic JavaScript file? (y/n)")
js = input().lower() == 'y' 

def generate_html():
    """Generate HTML5 template based on user inputs"""
    # Create the basic HTML structure
    html_template = "<!DOCTYPE html>\n"
    html_template += f'<html lang="{selected_language}">\n'

    # Start the head section with meta information
    html_template += "<head>\n"
    html_template += f'    <meta charset="{selected_encoding}">\n'
    html_template += f'    <title>{page_title}</title>\n'

    # Add SEO meta tags (helps search engines understand the page)
    html_template += f'    <meta name="author" content="{author}">\n'
    html_template += f'    <meta name="description" content="{description}">\n'
    html_template += f'    <meta name="keywords" content="{keywords}">\n'
    html_template += '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'

    # Add social media sharing tags if user requested them
    if social_media:
        html_template += f'    <meta property="og:title" content="{page_title}">\n'
        html_template += f'    <meta property="og:description" content="{description}">\n'
        html_template += f'    <meta property="og:type" content="website">\n'

    # Add links to CSS and JavaScript files if requested
    if css:
        html_template += '    <link rel="stylesheet" href="styles.css">\n'
    if js:
        html_template += '    <script src="script.js"></script>\n'

    html_template += '</head>\n'

    # Create the body section with a main heading
    html_template += '<body>\n'
    html_template += f'    <h1>{page_title}</h1>\n'
    html_template += '</body>\n'
    html_template += '</html>'

    return html_template

# Generate the HTML content
html_content = generate_html()

# Save the HTML file with proper encoding
with open('index.html', 'w', encoding=selected_encoding) as f:
    f.write(html_content)

# Show success message for HTML file
print("\nHTML5 template has been generated successfully!")
print("Created file: 'index.html'")

# Create and save CSS file if requested
if css:
    with open('styles.css', 'w', encoding=selected_encoding) as f:
        f.write('/* Add your CSS styles here */\n')
    print("Created file: 'styles.css'")

# Create and save JavaScript file if requested
if js:
    with open('script.js', 'w', encoding=selected_encoding) as f:
        f.write('// Add your JavaScript code here\n')
    print("Created file: 'script.js'")

