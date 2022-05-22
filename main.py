from flask import escape
import functions_framework
import requests
from requests.auth import HTTPBasicAuth
import json
import os

@functions_framework.http
def hook_root(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    protection = """
    {
   "required_status_checks":null,
   "enforce_admins":null,
   "required_pull_request_reviews":{
      "dismissal_restrictions":{
         
        },
      "dismiss_stale_reviews":false,
      "require_code_owner_reviews":true,
      "required_approving_review_count":1
        },
   "restrictions":null
    }
    """

    issue = """
    {
   "title":"Automated Branch Protection",
   "body":"Automating branch protection enabled @denialofself"
    }
    """

    PAT = os.environ.get('PAT')

    print("Got request")
    request_json = request.get_json(silent=True)
    print("Logging request body: ")
    print(request_json)

    if request_json['action'] == 'created':
        print("Repository action type was: " + request_json['action'])
        print("Automating protection of the default(main) branch")

        protection_response = requests.put(url=f"https://api.github.com/repos/ASampleOrg/{request_json['repository']['name']}/branches/main/protection", data=protection, auth=HTTPBasicAuth('denialofself', PAT))
        print("Protection response: ")
        print(protection_response.status_code)
        print(protection_response.text)

        print("Opening issue on repository create")
        issue_response = requests.post(url=f"https://api.github.com/repos/ASampleOrg/{request_json['repository']['name']}/issues", data=issue, auth=HTTPBasicAuth('denialofself', PAT))
        print("Issue response: ")
        print(issue_response.status_code)
        print(issue_response.text)

    else:
        print("Action was not created, skipping")

    return request_json
