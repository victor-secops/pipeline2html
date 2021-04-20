# pipeline2html
performs the pipeline scan and generates an human-readable html file with the result of the analysis.<br />
tested in python 3.7<br />
System Requirements for Veracode Pipeline Scan:<br />
You must have installed Java 8 or later.<br />
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
