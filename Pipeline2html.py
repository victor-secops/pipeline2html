import sys
import json
import os
from json2html import *
import re
jsonfile = 'results.json'
   
def pipelinescan():
    os.system('java -jar pipeline-scan.jar --veracode_api_id "api id" --veracode_api_key "api key" --file "application.zip" --issue_details true  --json_output true --filtered_json_output_file filtered.json')

def getHTML():
    with open(jsonfile) as json_file:
        pipelinedata = json.load(json_file)
        data = json.dumps(pipelinedata, indent=4)
        
        clean = re.sub('<[^<]+?>', '', data)
        clean = clean.replace('\n', '')
        html = json2html.convert(json=clean, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
        html2 = """
        <html>
        <head>
        
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
        </head>
        <body>
        """+html+"""
        </body>
        </html>
        """
        f = open("pipeline-report.html", "w")
        f.write(html2)
        f.close()

pipelinescan()		

getHTML()

