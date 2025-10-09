# ExecutionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the execution of this workflow stage | 
**stop_date** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.execution_output import ExecutionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionOutput from a JSON string
execution_output_instance = ExecutionOutput.from_json(json)
# print the JSON string representation of the object
print(ExecutionOutput.to_json())

# convert the object into a dict
execution_output_dict = execution_output_instance.to_dict()
# create an instance of ExecutionOutput from a dict
execution_output_from_dict = ExecutionOutput.from_dict(execution_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


