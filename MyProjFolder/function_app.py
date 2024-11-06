import azure.functions as func
import datetime
import json
import logging
import re  # Import the re module for regular expressions

app = func.FunctionApp()

def highlight_numbers(text):
    text = re.sub(r'(\d+,\d+\.?\d*)', r'<b style="color:red;">\1</b>', text)
    
    highlight_words = ["Ciao", "Bello", "Aurora", "Amo", "William"]
    if highlight_words:
        pattern = r'\b(' + '|'.join(re.escape(word) for word in highlight_words) + r')\b'
        text = re.sub(pattern, r'<span style="color:yellow">\1</span>', text)
    
    return text

@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.params.get('text')

    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req_body.get('text')

    if text:
        highlighted_text = highlight_numbers(text)
        return func.HttpResponse(f"Processed text: {highlighted_text}", mimetype="text/html")
    else:
        return func.HttpResponse(
             "No text provided.",
             status_code=400
        )