# This script exports data from BigQuery
import subprocess


def call(cmd):
    print(cmd, subprocess.Popen(cmd.split(), stdout=subprocess.PIPE).communicate())


bucket_name = "pwr_hackaton"
source_table = "data_table"
target_file = "data"

extract_cmd = f"bq extract --compression GZIP --destination_format CSV --noprint_header '{bucket_name}.{source_table}' gs://{bucket_name}/{target_file}-*.csv.gz"
first_files = [
    f"gs://{bucket_name}/{target_file}-00000000000{i}.csv.gz" for i in range(10)
]
first_files_str = " ".join(first_files)
tmp_file = f"gs://{bucket_name}/{target_file}-000000000100.csv.gz"
first_files_compose_cmd = f"gsutil compose {first_files_str} {tmp_file}"
first_files_delete_cmd = f"gsutil rm {first_files_str}"
all_files_compose_cmd = f"gsutil compose gs://{bucket_name}/{target_file}-*.csv.gz gs://p{bucket_name}/{target_file}.csv.gz"
first_files_delete_cmd = f"gsutil rm {first_files_str}"
all_files_delete_cmd = f"gsutil rm gs://{bucket_name}/{target_file}-*.csv.gz"
download_cmd = f"gsutil cp gs://{bucket_name}/{target_file}.csv.gz ."

pipeline = [
    extract_cmd,
    first_files_compose_cmd,
    first_files_delete_cmd,
    all_files_compose_cmd,
    all_files_delete_cmd,
    download_cmd,
]
for cmd in pipeline:
    call(cmd)
