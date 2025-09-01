import azure.functions as func

app = func.FunctionApp()

@app.route(route="hello")  # 👈 defines the HTTP-triggered function
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get("name")

    if name:
        return func.HttpResponse(f"Hello, {name}!", status_code=200)
    else:
        return func.HttpResponse(
            "Please pass a name in the query string or request body",
            status_code=400
        )
