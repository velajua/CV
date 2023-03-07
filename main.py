from google.cloud import storage
from flask import make_response


def main(request):
    client = storage.Client()
    bucket = client.get_bucket("showcv")        # Name of the bucket in GCS
    blob = bucket.blob("CV.pdf")                # Path to the file in the GCS bucket
    cv_content = blob.download_as_string()
    
    response = make_response(cv_content)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=cv.pdf"
    return response
