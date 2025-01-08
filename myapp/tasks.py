from celery import shared_task
from .scraper import start_scrape

@shared_task(bind=True)
def start_scraping_job(self, region):
    print(f"Region in Task: {region}")
    print("Starting Scraping Job")
    status, message = start_scrape(region=region)
    print(status, message)
    print("Scraping Job Done...")