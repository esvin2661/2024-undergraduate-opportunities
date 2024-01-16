import requests
from bs4 import BeautifulSoup

# Define a list of company URLs to scrape
company_urls = [
    "https://www.google.com/careers/jobs/results/?job_category=Engineering&job_type=Internship&q=software%20engineer%20internship",
    "https://careers.apple.com/us/jobs/searchResults/?keyword=software%20engineer%20internship",
    "https://www.amazon.jobs/en/jobs/results/internship/software%20engineer",
    "https://www.microsoft.com/en-us/careers/students/search/?sid=internships&og=software%20engineer",
    "https://careers.facebook.com/jobs/search/?q=software%20engineer%20internship",
]

# Define data fields to extract
data_fields = ["title", "company", "location", "description", "application_url"]

# Initialize an empty list to store internship data
internships = []


for url in company_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    job_postings = soup.find_all("div", class_="job-posting")
    for job_posting in job_postings:
        data = {}
        for field in data_fields:
            element = job_posting.find("span", class_=f"{field}-text")
            if element:
                data[field] = element.text.strip()
            else:
                data[field] = None
        internships.append(data)

# Print the extracted internship data
for internship in internships:
    print(f"Title: {internship['title']}")
    print(f"Company: {internship['company']}")
    print(f"Location: {internship['location']}")
    print(f"Description: {internship['description']}")
    print(f"Application URL: {internship['application_url']}")
    print("---")

