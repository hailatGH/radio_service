gcloud sql databases create kinmusic-radio-database --instance=kinmusic-postgresql-v14

gcloud secrets create radio_service_settings --replication-policy automatic
gcloud secrets versions add radio_service_settings --data-file .env

gcloud secrets add-iam-policy-binding radio_service_settings \
    --member serviceAccount:299791645258@cloudbuild.gserviceaccount.com \
    --role roles/secretmanager.secretAccessor