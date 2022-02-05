import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import folium
import boto3

#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])
#app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])

s3_client = boto3.client('s3')
BUCKET = "map-2022-01-08"
FILE_NAME = "map.html"

response = s3_client.list_objects_v2(Bucket=BUCKET)
files = response.get("Contents")
for file in files:
    print(type(file))
    print(file)
    s3_client.download_file(BUCKET, file['Key'], "./downloads/"+ str(file['Key']))
    #print(f"file_name: {file&#91;'Key']}, size: {file&#91;'Size']}")
 

FILE_NAME = "map.html"
S3_PATH =  FILE_NAME
for my_bucket_object in BUCKET.objects.all():
    print(my_bucket_object)
#s3_client.download_file(BUCKET, FILE_NAME, "./downloads/mymap.html")
"""
        obj = s3_client.get_object(
        Bucket=BUCKET, 
        Key=S3_PATH, 
        )
        print("*******")
        print(type(obj))
        print(obj.keys())
        print(obj['Body'])
"""