
# Import libraries
import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
GOOGLE_CONTACTS_API_URL = 'https://www.google.com/m8/feeds/contacts/default/full'
GOOGLE_CONTACTS_API_PARAMS = {'alt': 'json', 'max-results': 1000}
NOTION_API_URL = 'https://api.notion.com/v1/databases/YOUR_NOTION_DATABASE_ID/query'
NOTION_CREATE_PAGE_URL = 'https://api.notion.com/v1/pages'
NOTION_UPDATE_PAGE_URL = 'https://api.notion.com/v1/pages/{page_id}'

# Prompt the user for input credentials and tokens
google_access_token = input('Please enter your Google access token: ')
notion_access_token = input('Please enter your Notion access token: ')
notion_database_id = input('Please enter your Notion database ID: ')

# Set up headers for API requests
GOOGLE_CONTACTS_API_HEADERS = {'Authorization': f'Bearer {google_access_token}', 'GData-Version': 3.0}
NOTION_API_HEADERS = {'Authorization': f'Bearer {notion_access_token}', 'Notion-Version': '2021-08-16'}

# Define helper functions
def get_google_contacts():
  """Get a list of Google contacts as a JSON object."""
  try:
    response = requests.get(GOOGLE_CONTACTS_API_URL, params=GOOGLE_CONTACTS_API_PARAMS, headers=GOOGLE_CONTACTS_API_HEADERS)
    response.raise_for_status()
    logging.info('Successfully fetched Google contacts')
    return response.json()
  except requests.exceptions.RequestException as e:
    logging.error(f'Failed to fetch Google contacts: {e}')
    return None

def get_notion_contacts():
  """Get a list of Notion contacts as a JSON object."""
  try:
    response = requests.post(NOTION_API_URL, headers=NOTION_API_HEADERS)
    response.raise_for_status()
    logging.info('Successfully fetched Notion contacts')
    return response.json()
  except requests.exceptions.RequestException as e:
    logging.error(f'Failed to fetch Notion contacts: {e}')
    return None

def create_notion_contact(contact):
  """Create a new Notion contact from a Google contact."""
  # Extract relevant fields from Google contact
  name = contact['title']['$t']
  first_name = contact['gd$name']['gd$givenName']['$t'] if 'gd$name' in contact and 'gd$givenName' in contact['gd$name'] else ''
  last_name = contact['gd$name']['gd$familyName']['$t'] if 'gd$name' in contact and 'gd$familyName' in contact['gd$name'] else ''
  organization = contact['gd$organization'][0]['gd$orgName']['$t'] if 'gd$organization' in contact and len(contact['gd$organization']) > 0 and 'gd$orgName' in contact['gd$organization'][0] else ''
  title = contact['gd$organization'][0]['gd$orgTitle']['$t'] if 'gd$organization' in contact and len(contact['gd$organization']) > 0 and 'gd$orgTitle' in contact['gd$organization'][0] else ''
  email = contact['gd$email'][0]['address'] if 'gd$email' in contact and len(contact['gd$email']) > 0 else ''
  phone = contact['gd$phoneNumber'][0]['$t'] if 'gd$phoneNumber' in contact and len(contact['gd$phoneNumber']) > 0 else ''
  contact_id = contact['id']['$t']

  # Construct Notion contact data
  data = {
    "parent": {
      "database_id": notion_database_id
    },
    "properties": {
      "Name": {
        "title": [
          {
            "text": {
              "content": name
            }
          }
        ]
      },
      "First Name": {
        "rich_text": [
          {
            "text": {
              "content": first_name
            }
          }
        ]
      },
      "Last Name": {
        "rich_text": [
          {
            "text": {
              "content": last_name
            }
          }
        ]
      },
      "Organization": {
        "rich_text": [
          {
            "text": {
              "content": organization
            }
          }
        ]
      },
      "Title": {
        "rich_text": [
          {
            "text": {
              "content": title
            }
          }
        ]
      },
      "Email Address": {
        "email": email
      },
      "Phone Number": {
        "phone_number": phone
      },
      "contactId": {
        "rich_text": [
          {
            "text": {
              "content": contact_id
            }
          }
        ]
      }
    }
  }

  # Send request to Notion API to create a new page (contact)
  try:
    response = requests.post(NOTION_CREATE_PAGE_URL, headers=NOTION_API_HEADERS, data=json.dumps(data))
    response.raise_for_status()
    logging.info(f'Successfully created Notion contact: {name}')
    return response.json()
  except requests.exceptions.RequestException as e:
    logging.error(f'Failed to create Notion contact: {name} - {e}')
    return None

def update_notion_contact(contact, page_id):
  """Update an existing Notion contact from a Google contact."""
   # Extract relevant fields from Google contact
   name = contact['title']['$t']
   first_name = contact['gd$name']['gd$givenName']['$t'] if 'gd$name' in contact and 'gd$givenName' in contact['gd$name'] else ''
   last_name = contact['gd$name']['gd$familyName']['$t'] if 'gd$name' in contact and 'gd$familyName' in contact['gd$name'] else ''
   organization = contact['gd$organization'][0]['gd$orgName']['$t'] if 'gd$organization' in contact and len(contact['gd$organization']) > 0 and 'gd$orgName' in contact['gd$organization'][0] else ''
   title = contact['gd$organization'][0]['gd$orgTitle']['$t'] if 'gd$organization' in contact and len(contact['gd$organization']) > 0 and 'gd$orgTitle' in contact['gd$organization'][0] else ''
   email = contact['gd$email'][0]['address'] if 'gd$email' in contact and len(contact['gd$email']) > 0 else ''
   phone = contact['gd$phoneNumber'][0]['$t'] if 'gd$phoneNumber' in contact and len(contact['gd$phoneNumber']) > 0 else ''
   # Construct Notion update data
   data = {
     "properties": {
       "Name": {
         "title": [
           {
             "text": {
               "content": name
             }
           }
         ]
       },
       "First Name": {
         "rich_text": [
           {
             "text": {
               "content": first_name
             }
           }
         ]
       },
       "Last Name": {
         "rich_text": [
           {
             "text": {
               "content": last_name
             }
           }
         ]
       },
       "Organization": {
         "rich_text": [
           {
             "text": {
               "content": organization
             }
           }
         ]
       },
       "Title": {
         "rich_text": [
           {
             "text": {
               "content": title
             }
           }
         ]
       },
       "Email Address": {
         "email": email
       },
       "Phone Number": {
         "phone_number": phone
       }
     }
   }

   # Send request to Notion API to update an existing page (contact)
   try:
     response = requests.patch(NOTION_UPDATE_PAGE_URL.format(page_id=page_id), headers=NOTION_API_HEADERS, data=json.dumps(data))
     response.raise_for_status()
     logging.info(f'Successfully updated Notion contact: {name}')
     return response.json()
   except requests.exceptions.RequestException as e:
     logging.error(f'Failed to update Notion contact: {name} - {e}')
     return None

# Main logic

# Get Google contacts
google_contacts = get_google_contacts()
if not google_contacts:
  logging.error('No Google contacts found')
else:
  # Get Notion contacts
  notion_contacts = get_notion_contacts()
  if not notion_contacts:
    logging.error('No Notion contacts found')
  
# Create a mapping of Google contacts IDs to Notion page IDs
mapping = {}
for result in notion_contacts.get('results', []):
  page_id = result.get('id', '')
  properties = result.get('properties', {})
  google_contact_id = properties.get('contactId', {}).get('rich_text', [{}])[0].get('text', {}).get('content', '')
  
if google_contact_id:
    mapping[google_contact_id] = page_id

# Loop through Google contacts and sync them with Notion contacts
for entry in google_contacts.get('feed', {}).get('entry', []):
  # Check if the contact has a name
  if entry.get('title', {}).get('$t', ''):

# Loop through Google contacts and sync them with Notion contacts
for entry in google_contacts.get('feed', {}).get('entry', []):
  # Check if the contact has a name
  if entry.get('title', {}).get('$t', ''):
    # Check if the contact is already in Notion
    if entry.get('id', {}).get('$t', '') in mapping:
      # Update the existing Notion contact
      update_notion_contact(entry, mapping[entry.get('id', {}).get('$t', '')])
    else:
      # Create a new Notion contact
      create_notion_contact(entry)


