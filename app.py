
from flask import Flask, jsonify
import pyodbc
import pandas as pd

app = Flask(__name__)
server = 'ifieldsmartsandbox.c4ilsrawbonz.us-east-1.rds.amazonaws.com' 
database = 'IFBIMIntegration_1' 
database1 = 'IFMasterDatabase_1' 
username = 'ifsearch' 
password = 'ifsearch#2020'
AWS_ACCESS_KEY_ID = 'AKIAIZ5ADQQ5V3X4CW2A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'us-east-1'

def userConnection():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database1+';UID='+username+';PWD='+ password+';TrustServerCertificate=Yes')
    return cnxn
def tableConnection():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=Yes')
    return cnxn
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def Projects():
    pd.set_option('display.max_columns', None)
    pr = pd.read_sql("select * from Projects where projectid in (select projectid from tbl_mapping_User_Project where userid=461)", tableConnection()) 
    projName = pr['ProjectName'].to_list()
    projId = pr['ProjectID'].to_list()
    project = {
        "ProjectName":projName,
        "projectId":projId
    }
    return project


# main driver function
if __name__ == '__main__':
    app.run()
