# ActionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of action for this stage | 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.action_output import ActionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ActionOutput from a JSON string
action_output_instance = ActionOutput.from_json(json)
# print the JSON string representation of the object
print(ActionOutput.to_json())

# convert the object into a dict
action_output_dict = action_output_instance.to_dict()
# create an instance of ActionOutput from a dict
action_output_from_dict = ActionOutput.from_dict(action_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


