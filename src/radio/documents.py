from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import  RadioStationModel


@registry.register_document
class RadiostationmodelDocument(Document):
    station_frequency= fields.TextField()
    
    def prepare_station_frequency(self, instance):
        return instance.get_passstation_frequency_for_es()
    
    class Index:
        name = "radio_station"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }


    class Django:
        model = RadioStationModel

        fields = [
            "id",
            "station_name",
            #"station_frequency",
            "station_url",
            "station_cover",
            "station_description",
            "encoder_FUI",
            "created_at",
            "updated_at"
        ]
        
