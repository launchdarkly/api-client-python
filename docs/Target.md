# Target


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** | A list of the keys for targets that will receive this variation because of individual targeting | 
**variation** | **int** | The index, from the array of variations for this flag, of the variation to serve this list of targets | 
**context_kind** | **str** | The context kind of the individual target | [optional] 

## Example

```python
from launchdarkly_api.models.target import Target

# TODO update the JSON string below
json = "{}"
# create an instance of Target from a JSON string
target_instance = Target.from_json(json)
# print the JSON string representation of the object
print(Target.to_json())

# convert the object into a dict
target_dict = target_instance.to_dict()
# create an instance of Target from a dict
target_from_dict = Target.from_dict(target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


