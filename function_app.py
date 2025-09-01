import azure.functions as func
from functions import hello_world

app = func.FunctionApp()

@app.route(route="hello")   # 👈 register route
def hello(req: func.HttpRequest) -> func.HttpResponse:
    return hello_world.main(req)
