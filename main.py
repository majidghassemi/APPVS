# HTTP requests
from os import write
import requests 
# Web scraping library
from bs4 import BeautifulSoup
# Sending the emails
import smtplib
# Email Body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# System datetime manipulation
import datetime
# Import pdf creator
from fpdf import FPDF

# save FPDF() class into a variable pdf
pdf = FPDF()

# For showing the appropriate time in Email
current_time = datetime.datetime.now()


def job_with_visa():
    website_link = "https://stackoverflow.com/jobs"
    html_content = requests.get(website_link).text
    soup = BeautifulSoup(html_content, 'lxml')
    jobs = soup.find_all(
        'div', class_="-job js-result js-dismiss-overlay-container ps-relative  p12 pl24 ")
    for job, index in enumerate(jobs):
        job_info = job.find('h2', class_='mb4 fc-black-800 fs-body3').a
        job_title = job_info.text.strip()
        job_url = job_info['href'].strip()
        company_name = job.find(
            'h3', class_='fc-black-700 fs-body1 mb4').span.text.strip()
        location = job.find('span', class_='fc-black-500').text.split(',')[0]
        requirements = job.find_all('div', class_='d-inline-flex gs4 fw-wrap').a.text
        posted_date = job.find('span', class_ = 'fc-orange-400 fw-bold').text
        if index == 0:
            with open('jobs.txt', 'w') as f:
                f.write(f'''
                    {index}. Job title: {job_title}
                    Link to the job: {website_link}{job_url}
                    Company : {company_name}
                    Located in: {location.strip()}
                    Requirements: {requirements.strip()}
                    Posted at: {posted_date}
                    ***********************************************************************
                ''')
        else:
            with open('jobs.txt', 'a') as f:
                f.write(f'''
                    {index}. Job title: {job_title}
                    Link to the job: {website_link}{job_url}
                    Company : {company_name}
                    Located in: {location.strip()}
                    Requirements: {requirements.strip()}
                    Posted at: {posted_date}
                    ***********************************************************************
                ''')



if __name__ == "__main__":
    while True:
        job_with_visa()
        # wait_time = 1440
        # time.sleep(wait_time * 60)