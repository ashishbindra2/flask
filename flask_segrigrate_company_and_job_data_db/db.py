from pymongo import MongoClient 

from bson.objectid import ObjectId

client = MongoClient()

# db_list = client.list_database_names()
# print(db_list)

manga_db = client.testdb

comapny_collection = manga_db.comapny
job_collection = manga_db.job

def get_comapny():
    comapnies = comapny_collection.find({})
    return list(comapnies)

def get_job():
    jobs = job_collection.find()
    return list(jobs)

def company_exists(company_name):
    try:
        # Search for a document with the given company name
        result = comapny_collection.find_one({"company_name": company_name})

        # If a document result['_id'] is found, the company exists
        return result['_id'] if result else None
    except Exception as e:
        print(f"Error checking if company exists: {str(e)}")
        return False
    
def is_company_location(cid,company_location):
    try:
        print("in")
        result = comapny_collection.find_one({"_id": ObjectId(cid)} ,{"company_location":   1})
        if result is not None and "company_location" in result:
            # Document exists and has the company_location field
            print("Location exists:", result["company_location"])
            if company_location in  result["company_location"]:
                return True
        else:
            # Document does not exist or does not have the company_location field
            comapny_collection.update_one({"_id": ObjectId(cid)},{"$set":{"company_location":[]}})
            print("empty Array created!!!")
    except Exception as e:
        print(f"Error checking if company exists: {str(e)}")
    return False
    
def insert_job_and_company(job_company_list):
    
    for item in job_company_list:
        try:
            source_name = item.get('source_name', "")
            company_name = item.get('company_details', {}).get('company_name')

            if company_name:
                company_id = company_exists(company_name)
                company_details = item.get('company_details', {})
                job_details = item.get('job_details', "")
                
                if company_id is None or company_id is False:
                    company_details = item.get('company_details', {})
                    company_details['source_name'] = source_name
                    # print(company_details)
                    company_id = comapny_collection.insert_one(company_details).inserted_id
                else:
                    location = job_details['location']
                    
                    is_comapny = is_company_location(company_id,location)
                    
                    if is_comapny is False:
                        
                        result = comapny_collection.update_one(
                                {"_id": company_id},
                                {"$push": {"company_location": location}}
                        )
                        if result.modified_count > 0:
                            print("Value appended to array successfully.")
                        else:
                            print("No document found or value not appended.")


                job_details['source_name'] = source_name
                job_details['company_id'] = company_id
                # print(job_details)
                # job_collection.insert_one(job_details)

            else:
                print(f"Details will not store because of bad data!!! and source is {source_name}")

        except Exception as e:
            print(f"Error inserting company details: {str(e)}")
            continue

is_company_location("660a98427e4d3ad7031cb872","Nationale Bank van België")