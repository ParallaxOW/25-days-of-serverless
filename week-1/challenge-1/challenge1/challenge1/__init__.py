import logging
import azure.functions as func
import os
from datetime import datetime, timedelta
from azure.storage.blob import (
    BlockBlobService,
    ContainerPermissions,
)
from azure.storage.blob.sharedaccesssignature import BlobSharedAccessSignature
from random import seed, random, choice

seed = (1)

account_name = os.getenv("AccountName")
account_key=os.getenv("AccountKey")
container_name = os.getenv("ContainerName")

def main(req: func.HttpRequest) -> func.HttpResponse:
	logging.info('Python HTTP trigger function processed a request.')
	blob_name = determine_file()
	image = get_image(blob_name)
	return func.HttpResponse(image, mimetype="image/png")

def determine_file():
	sequence = ["nun.png","gimmel.png","hay.png","shin.png"]
	return choice(sequence)

def get_image(filename):
	blobService = BlockBlobService(account_name, account_key)
	blob = blobService.get_blob_to_bytes(container_name, filename)
	return blob.content
