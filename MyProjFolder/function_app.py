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

    if not numero:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            numero = req_body.get('numero')

    if numero:
        try:
            numero = int(numero)  # Converti il valore in intero
            risultato = checknumero(numero)
            return func.HttpResponse(f"Processed text: {risultato}", mimetype="text/html")
        except ValueError:
            return func.HttpResponse(
                "Il valore fornito non è un numero valido.",
                status_code=400
            )
    else:
        return func.HttpResponse(
             "Nessun numero fornito.",
             status_code=400
        )