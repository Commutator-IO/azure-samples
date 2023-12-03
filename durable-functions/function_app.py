import azure.functions as func
import azure.durable_functions as df
from activities.hello import run

myApp = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)


# HTTP Triggers
@myApp.route(route="orchestrators/{functionName}")
@myApp.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    function_name = req.route_params.get("functionName")
    instance_id = await client.start_new(function_name)
    response = client.create_check_status_response(req, instance_id)
    return response


# Orchestrators
@myApp.orchestration_trigger(context_name="context")
def orchestrator_chaining(context):
    result1 = yield context.call_activity("hello", "Seattle")
    result2 = yield context.call_activity("hello", "Tokyo")
    result3 = yield context.call_activity("hello", "London")

    return [result1, result2, result3]


@myApp.orchestration_trigger(context_name="context")
def orchestrator_faninout(context):
    cities = ["Seattle", "Tokyo", "London"]
    parallel_tasks = [context.call_activity("hello", city) for city in cities]
    outputs = yield context.task_all(parallel_tasks)

    return list(outputs)


# Activities
@myApp.activity_trigger(input_name="city")
def hello(city: str) -> str:
    return run(city)
