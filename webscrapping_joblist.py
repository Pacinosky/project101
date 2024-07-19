import requests
from bs4 import BeautifulSoup
import time

'''This project is webscrapping a job website and retrieve 
the following information;
job title
company name
employment type
job location
job info or link
application deadline

'''

#define the function jobSearch

def jobSearch():
    '''ask the user to enter the city they want the job 
    by accepting input and filtering the input from the
    job list and you can exit the program by pressing q to 
    quit.
'''
    print('find your city or area')
    find_myCity=input('>>>').capitalize()
    print(f'filtering my {find_myCity}')
    print()

    if find_myCity.lower() == 'q':
        print('quit the search')
        quit()


    #import requests and BeautifulSoup and 
    #copy the url from the website you want to webscrap
    #you can use 'lxml' or 'html parser'
    #find all info after inspecting the html
    html_text=requests.get('https://www.jobsinghana.com/jobs/indexnew.php?device=d').text

    soup=BeautifulSoup(html_text, 'lxml')

    job_search=soup.find_all('div' , class_ = "joblistitem row")
    ''' set up condition for your search and scrap from the joblist,
    job title
company name
employment type
job location
job info or link
print your results
'''                   
    for index, job in enumerate(job_search):
        application_deadline=job.find('span', class_ = "posted_date").text.replace('Expires','') #remove the expires and display only the date
        companyName=job.find('h4').text
        jobTitle=job.find('h3').text.strip()
        jobLink=job.h3.a['href']
        employment_type=job.find('span', property="employmentType").text.replace('\n',"")
        
        locate_Job=job.find('span', property="jobLocation").span.text
        if find_myCity in locate_Job:
            with open(f'webscrab_joblist/{index}.txt', 'w') as f:
        #set up condition to search for the location of the job 
        #save into a file 
                f.write(f'Job Title : {jobTitle} \n')
                f.write(f'Company Name:  {companyName} \n')
                f.write(f'Location :\t{locate_Job.lstrip()} \n')
                f.write(f'Employment Type : {employment_type} \n')
                f.write(f'Job Info : {jobLink} \n')
                f.write(f'Application Deadline : {application_deadline.lstrip()} ')
            print(f'file saved: {index}')
                

if __name__ == '__main__':
    #call the fuction jobSearch and time wait
    while True:
        jobSearch()
        time_wait=2
        print(f'waiting {time_wait} seconds...')
        time.sleep(time_wait*2)
    
        
        