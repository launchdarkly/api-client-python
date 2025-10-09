# FlagImportConfigurationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** |  | 
**tags** | **List[str]** | Tags to associate with the configuration | [optional] 
**name** | **str** | Name to identify the configuration | [optional] 

## Example

```python
from launchdarkly_api.models.flag_import_configuration_post import FlagImportConfigurationPost

# TODO update the JSON string below
json = "{}"
# create an instance of FlagImportConfigurationPost from a JSON string
flag_import_configuration_post_instance = FlagImportConfigurationPost.from_json(json)
# print the JSON string representation of the object
print(FlagImportConfigurationPost.to_json())

# convert the object into a dict
flag_import_configuration_post_dict = flag_import_configuration_post_instance.to_dict()
# create an instance of FlagImportConfigurationPost from a dict
flag_import_configuration_post_from_dict = FlagImportConfigurationPost.from_dict(flag_import_configuration_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


