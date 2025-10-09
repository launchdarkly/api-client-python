# FlagSempatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instructions** | **List[Dict[str, object]]** |  | 
**comment** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_sempatch import FlagSempatch

# TODO update the JSON string below
json = "{}"
# create an instance of FlagSempatch from a JSON string
flag_sempatch_instance = FlagSempatch.from_json(json)
# print the JSON string representation of the object
print(FlagSempatch.to_json())

# convert the object into a dict
flag_sempatch_dict = flag_sempatch_instance.to_dict()
# create an instance of FlagSempatch from a dict
flag_sempatch_from_dict = FlagSempatch.from_dict(flag_sempatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


