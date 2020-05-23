# Log Traceback

Occasionally, there may be an issue with the logic of my program where it does not behave as intended, however no traceback is provided within the server logs in the terminal. In this case, I can place this snippet of code within the Python code at the point where the code is initialised. This will give a complete traceback of the code prettily logged within a log file `'stack-trace.log'`

```python
        # DEBUG: START DEBUG -->
        import traceback

        with open('logs/stack-trace.log', 'w') as file:
            traceback.print_stack(file=file)
        # DEBUG: END DEBUG --!
```
