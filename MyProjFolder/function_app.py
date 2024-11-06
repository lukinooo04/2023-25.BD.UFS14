import azure.functions as func
import json
import logging

app = func.FunctionApp()

def checknumero(numero):
    if numero % 2 == 0:
        return f"{numero} è divisibile per 2 e quindi è un numero pari."
    else:
        return f"{numero} non è divisibile per 2 e quindi è un numero dispari."

@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numero = req.params.get('numero')

    if numero:
        fi = checknumero(numero)
        if fi:
            return func.HttpResponse("numero pari")
        else:
            return func.HttpResponse("numero dispari")