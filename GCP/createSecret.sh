# gcloud sql databases create kinmusic-radio-database-dev --instance=kinmusic-postgresql-v14

gcloud secrets create radio_service_settings_dev --replication-policy automatic
gcloud secrets versions add radio_service_settings_dev --data-file .env.dev

gcloud secrets add-iam-policy-binding radio_service_settings_dev \
    --member serviceAccount:299791645258@cloudbuild.gserviceaccount.com \
    --role roles/secretmanager.secretAccessor