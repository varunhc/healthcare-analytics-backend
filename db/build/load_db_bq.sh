#!/bin/bash

bucket="mimic-data"
dataset_prefix="mimic4_v2_0"
schema_local_folder="~/mimic-code/mimic-iv/buildmimic/bigquery/schemas"


for module in hosp icu;
do
    FILES=$(gsutil ls gs://$bucket/v2.0/$module/*.csv.gz)

    for file in $FILES
    do

    base=${file##*/}
    filename=${base%.*}
    tablename=${filename%.*}

    bq load --allow_quoted_newlines --skip_leading_rows=1 --source_format=CSV --replace ${dataset_prefix}_${module}.$tablename gs://$bucket/v2.0/$module/$tablename.csv.gz $schema_local_folder/$module/$tablename.json

    if [ $? -eq 0 ];then
        echo "OK....$tablename"
    else
        echo "FAIL..$tablename"
    fi

    done
done
exit 0