import os

def handle_uploaded_file(f):
    with open("customer/static/upload/"+f.name, "wb") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def delete_upload_file(f):
    if os.path.exists("customer/static/upload/"+f.name):
        os.remove("customer/static/upload/"+f.name)
