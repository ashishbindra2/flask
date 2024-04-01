from db import insert_job_and_company
from datetime import datetime, timezone

data = {
        "job title": "Junior Functional analyst (V/M/X)", "company name": "Nationale Bank van ", 
        "location": "Brussel", "tags": "Permanent, Full-time", 
        "date of post": "Published on Jobat.be 4 days ago", "salary range": "", "industry": "Health care and medical accessories", 
        "company contact": [{"company_number": "", "company_email": ""}], "company website": "", 
        "job description": '''<div class="JobDetails-content">\n                <div class="JobDetails-contentParagraph">\n                    Vast Contract - Regio Antwerpen<br><br><str
ong>#IT #quality #GxP</strong><br><br><br><br>Onze partner is op zoek naar een IT Quality System Coördinator om hun IT team te versterken. Dit gerenommeerd dienstverlenend bedrijf 
is gelegen in <strong>Antwerpen </strong>en biedt een breed gamma aan services in diverse industrieën zoals petrochemie, voeding, farma,…. Ben je op zoek naar zo’n uitdaging? Lees 
dan zeker verder!\n                </div>\n                        <h2 class="JobDetails-contentTitle">\n                IT Quality System Coordinator\n            </h2>\n
       <h3 class="JobDetails-contentSubtitle ttl-function">Job description</h3>\n                <div class="JobDetails-contentParagraph" itemprop="responsibilities">\n
        Als IT Quality System Coördinator krijg je de verantwoordelijkheid over het <strong>opstellen en onderhouden van de IT kwaliteitsdocumentatie en de planning, de implementat
ie en opvolging van de IT projecten</strong> vanuit kwaliteit. Jouw takenpakket bestaat uit een aantal gevarieerde activiteiten:&nbsp;<br><br>&nbsp;<br><br>• <strong>Procedures en 
standaarden opstellen</strong> voor het IT departement<br><br>• Het IT team begeleiden doorheen de vereisten van het <strong>kwaliteitssysteem</strong><br><br>• Optreden als <stron
g>eerste contactpersoon</strong> m.b.t. kwaliteit<br><br>• Interne en externe <strong>audits </strong>uitvoeren en begeleiden<br><br>• Afwijkingen<strong> </strong>beheren doormidd
el van <strong>CAPA’s</strong><br><br>• <strong>Periodieke reviews</strong> van de IT kwaliteitsprocessen opvolgen<br><br>• De bestaande IT processen regelmatig evalueren en aligne
ren met de corporate richtlijnen<br><br>• Opmaken van <strong>gedetailleerde projectplanningen</strong> inclusief budgetbepaling en opvolging<br><br>• Organiseren en leiden van pro
ject meetings met alle betrokken partijen\n                </div>\n                            <h3 class="JobDetails-contentSubtitle ttl-profile">Profile</h3>\n                <div
 class="JobDetails-contentParagraph" itemprop="skills qualifications">\n                    Als IT Quality System Coördinator ben je minimaal in het bezit van een <strong>bachelor 
</strong>opleiding aangevuld met enkele jaren<strong> relevante ervaring in quality en IT</strong>. Ervaring in een farmaceutische omgeving is een pluspunt. <strong>Capa’s, SOP’s</
strong> en het <strong>begeleiden van audits</strong> kennen geen geheimen voor jou. Kennis &nbsp;van GxP, ISO27001, NIS2 regelgeving zijn sterke pluspunten. Je bent een geboren <s
trong>facilitator </strong>met goede <strong>planmatige </strong>en <strong>organisatorisch </strong>vaardigheden die zich vlot kan uitdrukken in het <strong>Nederlands </strong>en
 <strong>Engels</strong>. Tot slot heb je een <strong>kritische </strong>mindset en kan je vlot in <strong>multidisciplinaire </strong>team kan werken.\n                </div>\n   
                         <h3 class="JobDetails-contentSubtitle ttl-offer">Offer</h3>\n                <div itemprop="jobBenefits">\n                        <ul class="jobCard-benef
itsList">\n                                                            <li class="jobCard-benefitsList-item bedrijfswagen">\n                                    Company car\n      
                          </li>\n                        </ul>\n                    <div class="JobDetails-contentParagraph">\n                        Als IT Quality System Coördin
ator mag je rekenen op uitgebreide <strong>trainingen </strong>en <strong>opleidingen </strong>om jezelf te ontplooien op professioneel vlak. Daarnaast kan je genieten van een <str
ong>competitieve verloning</strong> met een <strong>compleet pakket aan extralegale voordelen</strong>. Tot slot kom je terecht in een dynamische omgeving en kan je werken in <stro
ng>glijdende uren</strong> en krijg je de mogelijkheid tot <strong>telewerken</strong>.&nbsp;<br><br><br><br>Voldoet deze functie aan jouw verwachtingen? Solliciteer dan rechtstree
ks via de website of contacteer Matthias Kegels op het nummer <span class="track-phone" style="cursor:pointer;" data-tealium-id="jobdetail-show-tel"><a>Show number</a><span class="
phone-number hidden">+32 (0)4 76 35 74 35</span></span> of via <span class="track-other-email" style="cursor:pointer;" data-tealium-id="jobdetail-show-email"><a>Show emailaddress</
a><a href="mailto:matthias.kegels@experis.be?subject=Contact request from Jobat.be | IT Quality System Coordinator&amp;body=Dear, i would like to receive extra information about th
is vacancy posted on Jobat.be: https://www.jobat.be/en/jobs/it-quality-system-coordinator/job_3420212?filter=az1pdCZqb2JsYW5ndWFnZT0xJm9ubGluZT03ZCZwYWdlbnVtPTI=" class="email hidd
en">matthias.kegels@experis.be</a></span>.\n                    </div>\n                </div>\n\n\n        </div>'''}

def data_segregate(website_data: dict, source_name: str) -> list | None:
    try:
        date_of_scrap = datetime.now().timestamp()
        job_company_list = []
        data = website_data
        # for index, data in enumerate(website_data):
        job_details = {
            "job_id": data.get("job id", ""),
            "job_title": data.get("job title", ""),
            "salary_range": data.get("salary range", ""),
            "location": data.get("location", ""),
            "tags": data.get("tags", ""),
            "date_of_post": data.get("date of post", ""),
            "work_experience": data.get("Work Experience", ""),
            "job_language": data.get("Work Experience", ""),
            "job_description": data.get("job description", ""),
            "date_of_scrap": str(date_of_scrap),
        }

        company_details = {
            "company_name": data.get("company name", ""),
            "company_size": data.get("company size", ""),
            "company_address": data.get("address", ""),
            "company_location": data.get("location", []),
            "company_contact": data.get("company contact", ""),
            "company_email": data.get("company email", ""),
            "company_type": data.get("industry", "Computer/IT Services"),
            "company_website": data.get("company website", ""),
        }

        final_dict = {
            "job_details": job_details,
            "company_details": company_details,
            "source_name": source_name
        }

        job_company_list.append(final_dict)

        print(f"Data successfully segregated!!!!")
        return job_company_list

    except Exception as e:
        print(f"An unexpected error occurred : {e}")
        return None


def insert_scraped_data(data: dict, source: str) -> None | dict:
    try:
        if data:
            job_company_list = data_segregate(data, source)

            if job_company_list:
                try:
                    insert_job_and_company(job_company_list)
                except Exception as e:
                    print("Insertion problem", e)

            else:
                print("Data Segregate problem")
    except Exception as e:
        print(e)
        return {"error": str(e)}
