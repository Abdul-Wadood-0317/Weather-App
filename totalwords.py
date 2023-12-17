import requests
from bs4 import BeautifulSoup
import re

def scrape_website(url):
    try:
        # Send an HTTP request
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text (modify based on the structure of the website)
        text_content = soup.get_text()

        # Remove extra spaces and newlines
        text_content = re.sub(r'\s+', ' ', text_content).strip()

        return text_content

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def is_urdu_word(word):
    # Function to check if a word is likely to be Urdu
    return not bool(re.search(r'[a-zA-Z]', word))

def count_and_save_urdu_words(websites, output_file):
    all_urdu_words = []

    with open(output_file, 'w', encoding='utf-8') as file:
        for website in websites:
            content = scrape_website(website)

            # Check if content is None
            if content is not None:
                # Tokenize the content into words
                words = re.findall(r'\b\w+\b', content.lower())

                # Filter out English words and update the list of Urdu words
                urdu_words = [word for word in words if is_urdu_word(word)]
                all_urdu_words.extend(urdu_words)

                # Write the content to the file
                #file.write(f"Content from {website}:\n{content}\n{'='*50}\n")

        # Write Urdu words to the file with 10-15 words per line
        file.write("\nUrdu Words:\n")
        words_per_line = 15
        for i in range(0, len(all_urdu_words), words_per_line):
            line_words = all_urdu_words[i:i + words_per_line]
            file.write(" ".join(line_words) + "\n")

        # Write total word count to the file
        total_urdu_word_count = len(all_urdu_words)
        file.write("\nTotal Urdu Word Count:\n")
        file.write(f"Total Urdu Words: {total_urdu_word_count}\n")

# List of websites to scrape
websites_to_scrape = [
    "https://jang.com.pk/",
    "https://dunya.com.pk/index.php",
    "https://urdu.geo.tv/",
    "https://dailykhabrain.com.pk/",
    "https://mashriq.com.pk/",
    "https://www.urdupoint.com/",
    "https://www.bbc.com/urdu",
    "https://bbc.com/urdu/topics/cjgn7n9zzq7t",
    "https://www.bbc.com/urdu/topics/cynd7qxprq0t",
    "https://www.bbc.com/urdu/topics/cl8l9mveql2t",
    "https://www.bbc.com/urdu/topics/cw57v2pmll9t",
    "https://www.bbc.com/urdu/topics/c340q0p2585t",
    "https://www.bbc.com/urdu/topics/ckdxnx900n5t",
    "https://www.bbc.com/urdu/topics/c40379e2ymxt",
    "https://www.bbc.com/urdu/topics/c1e0mzr3r2yt",
    "https://www.express.pk/" ,
    "https://www.express.pk/latest-news/",
    "https://www.express.pk/pakistan/",
    "https://www.express.pk/world/",
    "https://www.express.pk/sports/",
    "https://www.express.pk/saqafat/",
    "https://www.express.pk/weird-news/",
    "https://www.express.pk/science/",
    "https://www.express.pk/health/",
    "https://www.express.pk/business/",
    "https://express.pk/blog/",
    "https://www.worldurdurnp.com/%D8%B4%D8%B1%D8%94%D8%B1-%DA%A9%DB%8C-%DA%A9%D8%B1%D8%AF%D8%A7%D8%B1-%D9%86%DA%AF%D8%A7%D8%B1%DB%8C-%D9%81%D8%B1%D8%AF%D9%88%D8%B3-%D8%A8%D8%B1%DB%8C%DA%BA-%DA%A9%DB%92-%D8%AD%D9%88/",
	"https://urdunotes.com/lesson/essay-on-discipline-in-urdu-%d9%86%d8%b8%d9%85-%d9%88-%d8%b6%d8%a8%d8%b7-%d9%85%d8%b6%d9%85%d9%88%d9%86/",	
	"https://www.qaumiawaz.com/national/sudden-deaths-rise-in-country-most-deaths-from-heart-attacks-ncrb-report-reveals",
	"https://urdu.dunyanews.tv/",
	"https://urdunotes.com/lesson/essay-on-fashion-in-urdu-%D9%81%DB%8C%D8%B4%D9%86-%D9%BE%D8%B1-%D8%A7%DB%8C%DA%A9-%D9%85%D8%B6%D9%85%D9%88%D9%86/",
	"https://trt.net.tr/urdu/trykh-myn-aj-kh-dn/2019/01/19/trykh-myn-aj-kh-dn-19-1129128",
	"https://pakmag.net/history.php?pid=163",
	"https://balagh.pk/language/urdu/page/4/?product_count=50&product_orderby=price&product_view=list",
	"https://dailyurducolumns.com/column/orya-maqbool-jan/aik-aham-tehqeeqi-kitab-ka-urdu-tarjuma.aspx",	
	"https://urdunotes.com/lesson/essay-on-importance-of-education-in-urdu-%D8%AA%D8%B9%D9%84%DB%8C%D9%85-%DA%A9%DB%8C-%D8%A7%DB%81%D9%85%DB%8C%D8%AA-%D9%BE%D8%B1-%D9%85%D8%B6%D9%85%D9%88%D9%86/",	"https://www.bbc.com/urdu/articles/c032r3kkl71o",	
	"https://www.bbc.com/urdu/articles/cp3pgr2601xo",	
	"https://www.bbc.com/urdu/live/pakistan-67668567",	
	"https://www.bbc.com/urdu/articles/c162yw1kl6jo	",
	"https://www.bbc.com/urdu/articles/cl4pk4rd52lo	",
	"https://www.bbc.com/urdu/articles/c0k2dd0gz95o	",
	"https://www.bbc.com/urdu/articles/c3g2j1ypldyo	",
	"https://www.bbc.com/urdu/articles/cd1p5x1242qo	",
	"https://www.bbc.com/urdu/articles/ceqp3022573o	",
	"https://www.bbc.com/urdu/articles/cz724g9ex5yo	",
	"https://www.bbc.com/urdu/articles/cg3pld98vyno	",
	"https://www.bbc.com/urdu/articles/cg6p9x7ey43o	",
	"https://www.bbc.com/urdu/articles/c8786e0vyxxo",	
	"https://www.bbc.com/urdu/live/pakistan-67656654",	
	"https://www.bbc.com/urdu/articles/c89qn2r37z2o",	
	"https://www.bbc.com/urdu/articles/cglpp2j3v2lo",	
	"https://www.bbc.com/urdu/articles/cgxp5ezgqpzo",
	"https://www.bbc.com/urdu/articles/ce9p73lejv4o",	
	"https://www.bbc.com/urdu/articles/cw82z2e393vo",	
	"https://www.bbc.com/urdu/articles/c3g2l512wgwo",	
	"https://www.bbc.com/urdu/articles/cp9pwpj2044o",	
	"https://www.bbc.com/urdu/articles/cv2zypj9j4qo",	
	"https://www.bbc.com/urdu/articles/cx91d89r8ylo",	
	"https://www.bbc.com/urdu/articles/cl7pre58n2yo",	
	"https://www.bbc.com/urdu/articles/c0d234p71yeo",
	"https://www.bbc.com/urdu/articles/c032r3rk1j0o",	
	"https://www.bbc.com/urdu/articles/cydgedl3r0lo",	
	"https://www.bbc.com/urdu/articles/czd4q9zypdeo",	
	"https://www.bbc.com/urdu/articles/c985v2xv59wo",	
	"https://www.bbc.com/urdu/articles/c3g2j1ypldyo",	
	"https://www.bbc.com/urdu/articles/cp3pgr2601xo",	
	"https://www.bbc.com/urdu/articles/cp4pgkrr7rdo",	
	"https://www.bbc.com/urdu/articles/cp4pgkrr7rdo",	
	"https://www.bbc.com/urdu/articles/cv2z9vlqk8do",	
	"https://www.bbc.com/urdu/articles/cevpe8nkwzlo",
	"https://www.bbc.com/urdu/articles/cevpe8nkwzlo",	
	"https://www.bbc.com/urdu/live/pakistan-67605178",	
	"https://www.bbc.com/urdu/articles/cyd2em264ypo",	
	"https://www.bbc.com/urdu/articles/cyd2em264ypo",	
	"https://www.bbc.com/urdu/articles/cjrpj2x277ro",	
	"https://www.bbc.com/urdu/articles/cqvp62063lgo",	
	"https://www.bbc.com/urdu/articles/crgplv085veo",	
	"https://www.bbc.com/urdu/articles/cv2vxpd8glgo",	
	"https://www.bbc.com/urdu/articles/c84v29ep7kzo",	
	"https://www.bbc.com/urdu/articles/cn0ppry5vv9o",
    "https://www.bbc.com/urdu/articles/cd1mgk2nme5o",
    
     
            # Add other URLs from your list
]

# Output file
output_file_path = "scraped_urdu_content_with_word_count.txt"

# Scrape the websites, save content, and count Urdu words
count_and_save_urdu_words(websites_to_scrape, output_file_path)

print(f"Scraped content and total Urdu word count saved to {output_file_path}")
