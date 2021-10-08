bq extract 'pwr_hackaton.pages_table' gs://pwr_hackaton/scrapes-*.csv \
&& \
gsutil compose gs://pwr_hackaton/scrapes-*.csv gs://pwr_hackaton/scrapes.csv \
&& \
gsutil rm gs://pwr_hackaton/scrapes-*.csv \
&& \
gsutil cp gs://pwr_hackaton/scrapes.csv .