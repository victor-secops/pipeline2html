# pipeline2html
generates a human-readable .HTML file from the Veracode pipeline verification results.json file.<br />
tested in python 3.7<br />

# How to Use
<p>
In directory where requirements.txt is located.<br />
run: pip install -r requirements.txt to install json2html package.<br />
Edit the code to insert your Veracode credentials in --veracode_api_id and --veracode_api_key parameters.<br />

Obtain the Pipeline Scan Files in https://downloads.veracode.com/securityscan/pipeline-scan-LATEST.zip<br />

extract pipelinescan to the same folder as the python script.<br />

Run python script<br />

Open pipeline-report.html in same folder as the python script<br />

</p>
