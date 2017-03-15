############### List of All Functions Contained Within & Their Descriptions #####

#get_company_links(startup_url) - '''This takes some webpage like http://www.digital.nyc/startups?page=1
#    and first creates a company tuple of the form (company name, company url), and then appends this tuple to
#    an object is called companies_list'''




################################################################################
def get_company_links(startup_url):
    '''This takes some webpage like http://www.digital.nyc/startups?page=1
    and first creates a company tuple of the form (company name, company url), and then appends this tuple to
    an object is called companies_list'''
    response = requests.get(startup_url)
    page_html = response.text
    soup = BeautifulSoup(page_html)
    # Retrieve all of the link tags
    links_collection = soup.find_all('a')
    companies_list = []
    for link in links_collection:
        try:
            # There are some links without href -- this keeps the code from 
            # breaking when it gets to them
            #print link["href"]
            if "/startups/" in link["href"]:    #This selects only htose links of startups
                #print True
                company_url = "http://www.digital.nyc/" + str(link["href"])
                #print company_url
                company_name = link["href"][10:]
                #print company_name
                company_tuple = (company_name,company_url)
                if company_tuple not in companies_list:
                    companies_list.append(company_tuple)
        except:
            pass
    return companies_list