
# Google Contacts to Notion Sync

## *THIS IS UNTESTED ALPHA CODE WRITTEN BY AI, USE WITH CAUTION!*

This is a collab notebook that syncs your Google contacts with a Notion database.

## Table of Contents

- [Overview](#overview)

- [Features](#features)

- [Setup and Prerequisites](#setup-and-prerequisites)

- [Instructions for Use](#instructions-for-use)

- [Limitations](#limitations)

- [Helpful Hints and Tips](#helpful-hints-and-tips)

## Overview

This notebook uses the Google Contacts and Notion APIs to fetch your contacts from both sources and sync them based on their IDs. It creates a new page in Notion for each contact that is not already in the database, and updates the existing pages for the contacts that are already in the database. It also handles some basic errors and logging.

[Back to top](#table-of-contents)

## Features

- Fetches your Google contacts as a JSON object using the Google Contacts API

- Fetches your Notion contacts as a JSON object using the Notion API

- Creates a mapping of Google contacts IDs to Notion page IDs

- Loops through your Google contacts and syncs them with your Notion contacts

- Creates a new page in Notion for each contact that is not already in the database

- Updates the existing page in Notion for each contact that is already in the database

- Handles some basic errors and logging using the requests and logging libraries

[Back to top](#table-of-contents)

## Setup and Prerequisites

To run this notebook, you need to have the following:

- A Google account with some contacts

- A Notion account with a "Contacts" database with the schema (additional fields are ok):

| Field Name     | Field Type |

| -------------- | ---------- |

| Name           | Title      |

| First Name     | Text       |

| Last Name      | Text       |

| Organization   | Text       |

| Title          | Text       |

| Email Address  | Email      |

| Phone Number   | Phone      |

| contactId      | Text       |

- A Google access token for accessing the Google Contacts API. You can obtain one by following the steps [here](https://developers.google.com/people/contacts-api-migration#authorizing_requests_with_oauth_20).

- A Notion access token for accessing the Notion API. You can obtain one by following the steps [here](https://developers.notion.com/docs/getting-started#step-2-create-an-integration).

- A Notion database ID for your "Contacts" database. You can find it in the URL when viewing your database. For example: https://www.notion.so/username/DATABASE_ID?

[Back to top](#table-of-contents)

## Instructions for Use

To use this notebook, follow these steps:

1. Open the notebook in collab or download it to your local machine.

2. Install the requests and json libraries if you don't have them already.

3. Run the first code cell to import the libraries and set up logging.

4. Run the second code cell to define some constants for the API URLs.

5. Run the third code cell to prompt you for input credentials and tokens. Enter your Google access token, Notion access token, and Notion database ID when prompted.

6. Run the fourth code cell to define some helper functions for getting, creating, and updating contacts.

7. Run the fifth code cell to execute the main logic of syncing your contacts.

8. Check the output and logs for any errors or messages.

[Back to top](#table-of-contents)

## Limitations

This notebook has some limitations that you should be aware of:

- It does not handle the case when a contact is deleted from Google or Notion. It only syncs the contacts that are present in both sources. To handle this case, it would need to keep track of the deleted contacts and remove them from the other source accordingly.

- It does not handle the case when a contact has multiple fields of the same type, such as multiple email addresses or phone numbers. It only takes the first one from the Google contact and syncs it with the Notion contact. To handle this case, it would need to loop through all the fields of the same type and sync them with the corresponding fields in Notion.

- It does not run periodically. It only runs once when the notebook is executed. To run it periodically, it would need to use a scheduling tool, such as cron or APScheduler, to trigger the sync at regular intervals. Alternatively, it could use a webhook or a cloud function to trigger the sync whenever there is a change in either source.

[Back to top](#table-of-contents)

## Helpful Hints and Tips

Here are some helpful hints and tips for using this notebook:

- You can use any programming language that can interact with the Google Contacts and Notion APIs. For example, you can use node.js, which is another popular language for web development and automation.

- You can use some tools and libraries that can help you with code quality, testing, formatting, and analysis. For example, you can use pylint, unittest, black, or sonarqube for Python; or eslint, jest, prettier, or logrocket for node.js.

- You can customize your Notion database by adding more fields or changing the view. For example, you can add fields for notes, tags, or photos; or change the view to board, list, timeline, or calendar.

[Back to top](#table-of-contents)


## Obtaining Credentials and Tokens

To run this notebook, you need to have the following credentials and tokens:

- A Google access token for accessing the Google Contacts API

- A Notion access token for accessing the Notion API

- A Notion database ID for your "Contacts" database

To obtain these credentials and tokens, follow these steps:

### Google Access Token

1. Go to the [Google API Console](https://console.developers.google.com/) and create a new project or select an existing one.

2. Enable the [People API](https://console.developers.google.com/apis/library/people.googleapis.com) for your project.

3. Go to the [Credentials](https://console.developers.google.com/apis/credentials) page and click on "Create Credentials" and select "OAuth client ID".

4. Choose "Web application" as the application type and enter a name for your client.

5. Under "Authorized redirect URIs", enter `https://developers.google.com/oauthplayground`.

6. Click on "Create" and note down your client ID and client secret.

7. Go to the [OAuth 2.0 Playground](https://developers.google.com/oauthplayground) and click on the settings icon at the top right corner.

8. Check the box for "Use your own OAuth credentials" and enter your client ID and client secret in the fields below.

9. In the left panel, select "People API v1" and expand it. Check the box for `https://www.googleapis.com/auth/contacts`.

10. Click on "Authorize APIs" and follow the prompts to sign in with your Google account and grant permissions.

11. Click on "Exchange authorization code for tokens" and note down your access token.

### Notion Access Token

1. Go to [Notion](https://www.notion.so/) and sign in with your account or create a new one if you don't have one already.

2. Go to [My Integrations](https://www.notion.so/my-integrations) and click on "New integration".

3. Enter a name for your integration and choose a workspace to connect it to.

4. Click on "Submit" and note down your internal integration token.

5. Go to your "Contacts" database in Notion and click on the "Share" button at the top right corner.

6. Under "Invite", select your integration from the dropdown menu and click on "Invite".

7. Your integration should now have access to your database.

### Notion Database ID

1. Go to your "Contacts" database in Notion and open it in a new tab or window.

2. Look at the URL of your database and find the part that looks like this: `https://www.notion.so/username/DATABASE_ID?`

3. Copy the DATABASE_ID part (without the question mark) and note it down.

[Back to top](#table-of-contents)

## Handling Limitations

This notebook has some limitations that you should be aware of and handle accordingly:

- It does not handle the case when a contact is deleted from Google or Notion. It only syncs the contacts that are present in both sources. To handle this case, you can either manually delete the contact from the other source, or modify the code to keep track of the deleted contacts and remove them from the other source accordingly.

- It does not handle the case when a contact has multiple fields of the same type, such as multiple email addresses or phone numbers. It only takes the first one from the Google contact and syncs it with the Notion contact. To handle this case, you can either manually add or edit the fields in Notion, or modify the code to loop through all the fields of the same type and sync them with the corresponding fields in Notion.

- It does not run periodically. It only runs once when the notebook is executed. To run it periodically, you can either manually run it at regular intervals, or use a scheduling tool, such as cron or APScheduler, to trigger the sync at regular intervals. Alternatively, you can use a webhook or a cloud function to trigger the sync whenever there is a change in either source.

[Back to top](#table-of-contents)

## References and Links

Here are some references and links to more resources that can help you learn more about this project:

- [Google Contacts API Documentation](https://developers.google.com/people/contacts-api-migration)

- [Notion API Documentation](https://developers.notion.com/docs)

- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)

- [JSON Library Documentation](https://docs.python.org/3/library/json.html)

- [Logging Library Documentation](https://docs.python.org/3/library/logging.html)

- [How to Sync Google Contacts with Notion (Tutorial)](https://www.youtube.com/watch?v=QwZvNjxJfoc)

- [How to Use Google Contacts API with Python (Article)](https://medium.com/@paulrohan/how-to-use-google-contacts-api-with-python-ba9c5739e567)

- [How to Use Notion API with Python (Article)](https://towardsdatascience.com/how-to-use-the-notion-api-with-python-bcdd703e0d98)

[Back to top](#table-of-contents)




