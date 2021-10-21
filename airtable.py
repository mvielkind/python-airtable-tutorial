import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

AIRTABLE_TOKEN = os.getenv("AIRTABLE_TOKEN")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")

AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"


def add_new_scores(scores):
    """Add scores to the Airtable."""
    # Check if more than 10 records are trying to be added.
    if len(scores["records"]) > 10:
        print("Cannot add more than 10 records in a single request.")
        return None

    url = f"{AIRTABLE_URL}/golf-scores"
    headers = {
      'Authorization': f'Bearer {AIRTABLE_TOKEN}',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(scores))

    return response


def get_golf_scores():
    """Retrieve records from Airtable."""
    url = f"{AIRTABLE_URL}/golf-scores"
    headers = {
      'Authorization': f'Bearer {AIRTABLE_TOKEN}',
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    return response


def get_golf_scores_by_page(offset=None):
    """Retrieve records from Airtable and apply offset is necessary."""
    url = f"{AIRTABLE_URL}/golf-scores"
    headers = {
      'Authorization': f'Bearer {AIRTABLE_TOKEN}',
      'Content-Type': 'application/json'
    }

    params = {
        "pageSize": 100
    }

    if offset:
        params["offset"] = offset

    response = requests.request("GET", url, headers=headers, params=params)

    return response


def get_scores_for_hole(hole):
    """Get scores for a specific hole."""
    url = f"{AIRTABLE_URL}/golf-scores"
    headers = {
      'Authorization': f'Bearer {AIRTABLE_TOKEN}',
      'Content-Type': 'application/json'
    }

    params = {
        "fields": ["Hole", "Score"],
        "filterByFormula": f"Hole={hole}"
    }

    response = requests.request("GET", url, headers=headers, params=params)

    return response


def update_record_fields(updated_records):
    """Updates the records."""
    url = f"{AIRTABLE_URL}/golf-scores"
    headers = {
        'Authorization': f'Bearer {AIRTABLE_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=json.dumps(updated_records))

    return response


def replace_record_fields(updated_records):
    """Updates the records."""
    url = f"{AIRTABLE_URL}/golf-scores"
    headers = {
        'Authorization': f'Bearer {AIRTABLE_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=json.dumps(updated_records))

    return response


def delete_records(records):
    """Deletes records from the table."""
    url = f"{AIRTABLE_URL}/golf-scores"
    headers = {
        'Authorization': f'Bearer {AIRTABLE_TOKEN}',
        'Content-Type': 'application/json'
    }

    params = {
        "records[]": records
    }

    response = requests.request("DELETE", url, headers=headers, params=params)

    return response
