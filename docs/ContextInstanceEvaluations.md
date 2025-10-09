# ContextInstanceEvaluations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ContextInstanceEvaluation]**](ContextInstanceEvaluation.md) | Details on the flag evaluations for this context instance | 
**total_count** | **int** | The number of flags | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.context_instance_evaluations import ContextInstanceEvaluations

# TODO update the JSON string below
json = "{}"
# create an instance of ContextInstanceEvaluations from a JSON string
context_instance_evaluations_instance = ContextInstanceEvaluations.from_json(json)
# print the JSON string representation of the object
print(ContextInstanceEvaluations.to_json())

# convert the object into a dict
context_instance_evaluations_dict = context_instance_evaluations_instance.to_dict()
# create an instance of ContextInstanceEvaluations from a dict
context_instance_evaluations_from_dict = ContextInstanceEvaluations.from_dict(context_instance_evaluations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


