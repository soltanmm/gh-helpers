import json
import requests

# You should add a file `config.py` with the global member 'access_token' with
# your GitHub personal access token. `config.py` is .gitignore'd for your
# convenience.
import config

headers = {'Authorization': 'token {}'.format(config.access_token)}

def op(op, path):
  return getattr(requests, op)('https://api.github.com{}'.format(path), headers=headers)

def get(path):
  return op('get', path)
