# FlagImportIntegrationLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**parent** | [**Link**](Link.md) |  | 
**project** | [**Link**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.flag_import_integration_links import FlagImportIntegrationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of FlagImportIntegrationLinks from a JSON string
flag_import_integration_links_instance = FlagImportIntegrationLinks.from_json(json)
# print the JSON string representation of the object
print(FlagImportIntegrationLinks.to_json())

# convert the object into a dict
flag_import_integration_links_dict = flag_import_integration_links_instance.to_dict()
# create an instance of FlagImportIntegrationLinks from a dict
flag_import_integration_links_from_dict = FlagImportIntegrationLinks.from_dict(flag_import_integration_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


