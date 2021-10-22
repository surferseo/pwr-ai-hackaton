# This script exports data from BigQuery
import subprocess


def call(cmd):
    print(cmd, subprocess.Popen(cmd.split(), stdout=subprocess.PIPE).communicate())


bucket_name = "pwr_hackaton"
source_table = "data_content_unstructured"
target_file = "data_content_unstructured"
is_large = False

extract_cmd = f"bq extract --compression GZIP --destination_format CSV --noprint_header {bucket_name}.{source_table} gs://{bucket_name}/{target_file}-*.csv.gz"
first_files = [
    f"gs://{bucket_name}/{target_file}-00000000000{i}.csv.gz" for i in range(10)
]
first_files_str = " ".join(first_files)
tmp_file = f"gs://{bucket_name}/{target_file}-000000000100.csv.gz"
first_files_compose_cmd = f"gsutil compose {first_files_str} {tmp_file}"
first_files_delete_cmd = f"gsutil rm {first_files_str}"
all_files_compose_cmd = f"gsutil compose gs://{bucket_name}/{target_file}-*.csv.gz gs://{bucket_name}/{target_file}.csv.gz"
first_files_delete_cmd = f"gsutil rm {first_files_str}"
all_files_delete_cmd = f"gsutil rm gs://{bucket_name}/{target_file}-*.csv.gz"
download_cmd = f"gsutil cp gs://{bucket_name}/{target_file}.csv.gz ."


pipeline = [
    (extract_cmd, True),
    (first_files_compose_cmd, is_large),
    (first_files_delete_cmd, is_large),
    (all_files_compose_cmd, True),
    (all_files_delete_cmd, True),
    (download_cmd, True),
]
for cmd, include in pipeline:
    if include:
        call(cmd)
