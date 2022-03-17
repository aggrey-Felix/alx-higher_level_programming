#!/bin/bash
#Script sends a DELETE request to URL passed as 1st argument, displays body of response
curl -s '$1' -X DELETE
