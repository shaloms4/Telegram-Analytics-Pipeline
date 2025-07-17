from dagster import job
from dagster_project.ops.scraper_op import scrape_telegram_data
from dagster_project.ops.db_loader_op import load_raw_to_postgres
from dagster_project.ops.dbt_op import run_dbt_transformations
from dagster_project.ops.yolo_op import run_yolo_enrichment

@job
def telegram_analytics_pipeline():
    scrape_telegram_data()
    load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment()
