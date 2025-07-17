from dagster import op

@op
def scrape_telegram_data():
    import subprocess
    subprocess.run(["python", "scraper/scrape_telegram.py"])
