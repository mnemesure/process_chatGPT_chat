chatGPT-chat-process
==============================
The code in this repository is used to process data from chatGPT share links.

## Quickstart
Python version is `python3.11`

Generate virtual environment

`python3 -m venv venv`

Activate environment

For windows:

`source venv/Scripts/activate`

for linux and MacOS

`source venv/bin/activate`

Navigate into `scripts/process_chat.py` and change the url to your chat link.

Now run `python3 process_chat.py` and it will generate a csv with your conversation.

## Getting your chat link from chatGPT

Once your conversation is finished, in the top righthand corner of chatGPT there is a share icon. Click this icon

A popup will appear on screen with a green button that says "copy link." This is what you paste into the url in `scripts/process_chat.py`


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    │ 
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── scripts            <- Where actual processing scripts live
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
