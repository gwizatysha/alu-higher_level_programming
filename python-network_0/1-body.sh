#!/bin/bash
# displays the body of the response only if final status code is 200
curl -s -L -f "$1"
