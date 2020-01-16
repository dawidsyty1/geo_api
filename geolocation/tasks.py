import logging
from app import settings
from app.celery import app
from geolocation import models, client
import os

@app.task
def _add_or_update_geolocation_data(field):
    """Celery task making the external call to the IPStack service and save data in the database."""
    logging.info("Start updating/creating geolocatication data...")

    response = client.get_geolookup_data(field)

    gelocation_data, created = models.GeolocationData.objects.get_or_create(ip=response.get('ip'))

    response = gelocation_data.validate_fields(response)
    gelocation_data.update_from_dict(response)

    gelocation_data.save()


def add_or_update_geolocation_data(data):
    """Start task in asynchronous mode or not"""
    logging.info("Starting task in {} mode".format(
        "asynchronous" if settings.ASYNCHRONOUS_ON is True else "normal")
    )
    if settings.ASYNCHRONOUS_ON is True:
        _add_or_update_geolocation_data.delay(data)
    else:
        _add_or_update_geolocation_data(data)
