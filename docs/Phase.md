# Phase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The phase ID | 
**audiences** | [**List[Audience]**](Audience.md) |  | 
**name** | **str** | The release phase name | 
**configuration** | **object** |  | [optional] 

## Example

```python
from launchdarkly_api.models.phase import Phase

# TODO update the JSON string below
json = "{}"
# create an instance of Phase from a JSON string
phase_instance = Phase.from_json(json)
# print the JSON string representation of the object
print(Phase.to_json())

# convert the object into a dict
phase_dict = phase_instance.to_dict()
# create an instance of Phase from a dict
phase_from_dict = Phase.from_dict(phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


