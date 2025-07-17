from dagster import op

@op
def run_yolo_enrichment():
    import subprocess
    subprocess.run(["python", "scripts/run_yolo_inference.py"])
