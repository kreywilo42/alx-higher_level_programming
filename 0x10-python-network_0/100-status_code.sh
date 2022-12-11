#!/bin/bash
# sends a request to a URL passed, and displays only the status code of the response
curl -sI -w '%{response_code}' "$1" -o /dev/null
