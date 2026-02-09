import requests
from bs4 import BeautifulSoup as bs 
import re
import time
import pandas as pd  
URL="https://realpython.github.io/fake-jobs/"
def loading_page(url):
    try:
       result=requests.get(url)
       return result
    except requests.RequstsException as e:
        print(f"error fetching the page {e}")
        return None
def parse_page(html):
    soup=bs(html.content, "html.parser")
    job_content=soup.find_all("div",class_="card-content")
    jobs=[]
    for job in job_content:
        try:
           title=job.find("h2",class_="title is-5").text.strip()
           
        except AttributeError:
           title = "N/A"

        company=job.find("h3", class_="subtitle is-6 company").get_text()
        location=job.find("p", class_="location").text.strip()
        apply_link=job.find("a", string="Apply")['href']
        jobs_info={
            "Title":title,
            "Company":company,
            "Location":location,
            "Apply Links":apply_link
        }
        jobs.append(jobs_info)
    time.sleep(1)
    return jobs
    
def emails_parse(email):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    email_content=re.findall(pattern, email.text)
    return email_content 

def main():
    print("Fetching page ....")
    content=loading_page(URL)
    if content:
        print("Parse job post...")
        jobs=parse_page(content)
        tables=pd.DataFrame(jobs)

        print("Extract email if avilable")
        emails=emails_parse(content)

        print("="*20 + "JOBS" + "="*20)
        print(tables)

        if emails:
            for e in emails:
                print(e)

        else:
            print("No email is found in this page")
    else:
        print("Error to fetch page")


if __name__ == "__main__":
    main()