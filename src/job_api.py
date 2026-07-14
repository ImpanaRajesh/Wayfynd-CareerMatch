from apify_client import ApifyClient
import os 
from dotenv import load_dotenv
from urllib.parse import quote
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# # Fetch LinkedIn jobs based on search query and location
# def fetch_linkedin_jobs(search_query, location = "india", rows=60):
#     run_input = {
#             "title": search_query,
#             "location": location,
#             "rows": rows,
#             "proxy": {
#                 "useApifyProxy": True,
#                 "apifyProxyGroups": ["RESIDENTIAL"],
#             }
#         }
#     run = apify_client.actor("hKByXkMQaC5Qt9UMN").call(run_input=run_input)
#     jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
#     return jobs

def fetch_linkedin_jobs(search_query, location="usa", rows=60):
    search_url = f"https://www.linkedin.com/jobs/search/?keywords={quote(search_query)}&location={quote(location)}"

    run_input = {
        "urls": [search_url],
        "scrapeCompany": True,
        "count": rows,
        "splitByLocation": False
    }
    run = apify_client.actor("hKByXkMQaC5Qt9UMN").call(run_input=run_input)
    # jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    jobs = list(apify_client.dataset(run.default_dataset_id).iterate_items())
    return jobs

# Fetch Naukri jobs based on search query and location
def fetch_naukri_jobs(search_query, location = "india", rows=60):
    run_input = {
        "keyword": search_query,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    # jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    jobs = list(apify_client.dataset(run.default_dataset_id).iterate_items())
    return jobs