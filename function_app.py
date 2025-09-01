import azure.functions as func
from functions import hello_world

app = func.FunctionApp()

# Register the simple function
app.route(route="hello")(hello_world.main)
