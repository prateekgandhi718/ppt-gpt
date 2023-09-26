import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('Python HTTP trigger function processed a request.')
        name = req.params.get('name')
        response_data = {
            "providedName": name,
            "message": "Fetched the data successfully."
        }
        return func.HttpResponse(json.dumps(response_data), status_code=200, mimetype="application/json")
    except Exception as e:
        error_message = f"An error occured: {str(e)}"
        logging.exception(error_message)
        response_data = {
            "providedName": None,
            "message": error_message
        }
