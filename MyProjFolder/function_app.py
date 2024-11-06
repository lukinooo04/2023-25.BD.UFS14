import azure.functions as func
import json
import logging

app = func.FunctionApp()

def checknumero(numero):
    if numero % 2 == 0:
        return True  # Restituisce True se il numero è pari
    else:
        return False  # Restituisce False se il numero è dispari

@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numero = req.params.get('numero')

    if numero:
        try:
            numero = int(numero)  # Converti il valore in intero
            if checknumero(numero):
                return func.HttpResponse("Il numero è pari.", status_code=200)
            else:
                return func.HttpResponse("Il numero è dispari.", status_code=200)
        except ValueError:
            return func.HttpResponse("Il valore fornito non è un numero valido.", status_code=400)
    else:
        return func.HttpResponse("Nessun numero fornito.", status_code=400)