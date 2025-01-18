def handler(event, context):
    print("Function invoked from Python")
    print(event)

    return {
        "statusCode": 200,
        "body": "hello from python!",
    }
