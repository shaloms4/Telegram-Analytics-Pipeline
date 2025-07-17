from dagster import ScheduleDefinition
from dagster_project.pipeline import telegram_analytics_pipeline

daily_schedule = ScheduleDefinition(
    job=telegram_analytics_pipeline,
    cron_schedule="0 6 * * *",  # Run daily at 6 AM
    name="daily_telegram_schedule"
)
