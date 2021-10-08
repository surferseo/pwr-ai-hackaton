bq extract 'pwr_hackaton.data_table' gs://pwr_hackaton/data-*.csv \
&& \
gsutil compose gs://pwr_hackaton/data-*.csv gs://pwr_hackaton/data.csv \
&& \
gsutil rm gs://pwr_hackaton/data-*.csv \
&& \
gsutil cp gs://pwr_hackaton/data.csv .