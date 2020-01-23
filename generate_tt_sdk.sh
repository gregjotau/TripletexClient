swagger-codegen generate -i http://tripletex.no/v2/swagger.json -l python -o ./tt_client

cd tt_client
python setup.py install