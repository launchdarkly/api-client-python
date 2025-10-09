# ContextInstanceEvaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the flag. | 
**key** | **str** | Key of the flag. | 
**value** | **object** | The value of the flag variation that the context receives. If there is no defined default rule, this is null. | 
**reason** | [**ContextInstanceEvaluationReason**](ContextInstanceEvaluationReason.md) |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.context_instance_evaluation import ContextInstanceEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of ContextInstanceEvaluation from a JSON string
context_instance_evaluation_instance = ContextInstanceEvaluation.from_json(json)
# print the JSON string representation of the object
print(ContextInstanceEvaluation.to_json())

# convert the object into a dict
context_instance_evaluation_dict = context_instance_evaluation_instance.to_dict()
# create an instance of ContextInstanceEvaluation from a dict
context_instance_evaluation_from_dict = ContextInstanceEvaluation.from_dict(context_instance_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


