DynatraceBackendApp


For requirements refer to requirements.txt.


To start server run command:
uvicorn main:app --reload


Server runs on localhost:8000

Swagger UI on localhost:8000/docs

Open any operation, by expanding corresponding task, then click "Try it out", provide parameters and click "Execute".

The result will be visible in the "Response body" section under "Responses".

Alternatively you can run the operations separately, for example for operation 1:

localhost:8000/task1

It opens up with default parameters being code "USD" and current date.

To change parameters, add them in the URL, for example:

localhost:8000/task1/?code=EUR&date=2023-01-02

Examples for task 2 and 3 would be:

localhost:8000/task2/?code=EUR&N=200 (by default code=USD, N=255)

localhost:8000/task3/?code=EUR&N=200 (by default code=USD, N=255)


___________________________________________________


To run tests run command:

"pytest"

in the project directory.

Values for operations 2 and 3 might change as new quotations are added.
