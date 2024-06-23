from django.conf import settings
from imagekitio import ImageKit
import tempfile
import os
import base64
from ..resources import IMAGEKIT_PUBLIC_KEY, IMAGEKIT_PRIVATE_KEY, IMAGEKIT_URL_ENDPOINT

imagekit = ImageKit(
	private_key=IMAGEKIT_PRIVATE_KEY, 
	public_key=IMAGEKIT_PUBLIC_KEY, 
	url_endpoint=IMAGEKIT_URL_ENDPOINT,
)
class Storage:
	def upload(self, name, file):
		upload = imagekit.upload_file(file=file, file_name=name)
		response = upload.response_metadata.raw
		return response.get("url")

	def upload_base64_image(self, name, base64_img):
		try:
			upload_url = self.upload(name=f"{name}.jpg", file=base64_img)
			return upload_url
		except Exception as e:
			print(f"Error uploading image: {e}")
			return None

