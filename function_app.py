import azure.functions as func
import json
import jwt


import logging
import socket
import urllib.error
from azure.identity import DefaultAzureCredential
from databricks import sql

# import modules from functions folder
from functions.oms_get_factories_by_user import main
from functions.oms_get_lock_period import main
from functions.oms_get_report_menu import main
from functions.oms_insert_example import main
from functions.oms_get_lock_period_log import main
from functions.oms_modify_lock_period import main
from functions.oms_modify_user_permission import main
from functions.oms_load_result import main



app = func.FunctionApp()

##TESTED SUCCESSFULLY
# @app.function_name(name="oms_get_factories_by_user")
# @app.route(route="oms_get_factories_by_user", auth_level=func.AuthLevel.FUNCTION)
# def oms_get_factories_by_user(req: func.HttpRequest) -> func.HttpResponse:
#     return main(req)
#==================================================================================================
##TESTED SUCCESSFULLY
# @app.function_name(name="oms_get_lock_period")
# @app.route(route="oms_get_lock_period", auth_level=func.AuthLevel.FUNCTION)
# def oms_get_lock_period(req: func.HttpRequest) -> func.HttpResponse:
#     return main(req)

##TESTED SUCCESSFULLY
# @app.function_name(name="oms_get_report_menu")
# @app.route(route="oms_get_report_menu", auth_level=func.AuthLevel.FUNCTION)
# def oms_get_report_menu(req: func.HttpRequest) -> func.HttpResponse:
#     return main(req)

#ERROR DURING TESTING
# @app.function_name(name="oms_insert_example")
# @app.route(route="oms_insert_example", auth_level=func.AuthLevel.FUNCTION)
# def oms_insert_example(req: func.HttpRequest) -> func.HttpResponse:
#     return main(req)

##TESTED SUCCESSFULLY
# @app.function_name(name="oms_get_lock_period_log")
# @app.route(route="oms_get_lock_period_log", auth_level=func.AuthLevel.FUNCTION)
# def oms_get_lock_period_log(req: func.HttpRequest) -> func.HttpResponse:
#     return main(req)

##TESTED SUCCESSFULLY
# @app.function_name(name="oms_modify_lock_period")
# @app.route(route="oms_modify_lock_period", auth_level=func.AuthLevel.FUNCTION)
# def oms_modify_lock_period(req: func.HttpRequest) -> func.HttpResponse:
#     return main(req)

#ERROR DURING TESTING
# @app.function_name(name="oms_modify_user_permission")
# @app.route(route="oms_modify_user_permission", auth_level=func.AuthLevel.FUNCTION)
# def oms_modify_user_permission(req: func.HttpRequest) -> func.HttpResponse:
#     return main(req)


@app.function_name(name="oms_load_result")
@app.route(route="oms_load_result", auth_level=func.AuthLevel.FUNCTION)
def oms_load_result(req: func.HttpRequest) -> func.HttpResponse:
    return main(req)