# temp_webservices


# use
# DISPLAY ALL
curl -i http://localhost:5000/company-data/api/v1.0/data

# DISPLAY ID
curl -i http://localhost:5000/company-data/api/v1.0/data/2

# CREATE
curl -i -H "Content-Type: application/json" -X POST -d "{\\"name\\":\\"Mark\\"}" http://localhost:5000/company-data/api/v1.0/data

# UPDATE
curl -i -H "Content-Type: application/json" -X PUT -d "{\\"name\\":\\"NEW_NAME\\"}" http://localhost:5000/company-data/api/v1.0/data/update/2

# DELETE:
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/company-data/api/v1.0/data/3
