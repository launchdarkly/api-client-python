# SourceFlag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The environment key for the source environment | 
**version** | **int** | The version of the source flag from which to copy | [optional] 

## Example

```python
from launchdarkly_api.models.source_flag import SourceFlag

# TODO update the JSON string below
json = "{}"
# create an instance of SourceFlag from a JSON string
source_flag_instance = SourceFlag.from_json(json)
# print the JSON string representation of the object
print(SourceFlag.to_json())

# convert the object into a dict
source_flag_dict = source_flag_instance.to_dict()
# create an instance of SourceFlag from a dict
source_flag_from_dict = SourceFlag.from_dict(source_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


