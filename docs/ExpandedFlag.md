# ExpandedFlag

Flag representation for Views API - contains only fields actually used by the Views service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key used to reference the flag | 
**name** | **str** | A human-friendly name for the flag | 
**description** | **str** | Description of the flag | [optional] 
**creation_date** | **int** | Creation date in milliseconds | [optional] 
**version** | **int** | Version of the flag | [optional] 
**archived** | **bool** | Whether the flag is archived | [optional] 
**tags** | **List[str]** | Tags for the flag | [optional] 
**temporary** | **bool** | Whether the flag is temporary | [optional] 
**include_in_snippet** | **bool** | Whether to include in snippet | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_flag import ExpandedFlag

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedFlag from a JSON string
expanded_flag_instance = ExpandedFlag.from_json(json)
# print the JSON string representation of the object
print(ExpandedFlag.to_json())

# convert the object into a dict
expanded_flag_dict = expanded_flag_instance.to_dict()
# create an instance of ExpandedFlag from a dict
expanded_flag_from_dict = ExpandedFlag.from_dict(expanded_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


