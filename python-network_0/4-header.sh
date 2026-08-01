#!/bin/bash
# sends a GET request with a custom header and displays the body
curl -s -X GET -H 'X-HolbertonSchool-User-Id: 98' "$1"
