from google.cloud import storage
from flask import make_response


def main(request):
    client = storage.Client()
    bucket = client.get_bucket("showcv")
    blob = bucket.blob("CV.pdf")
    cv_content = blob.download_as_string()
    
    response = make_response(cv_content)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=cv.pdf"
    return response
