# FlagImportIntegrationCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**FlagImportIntegrationCollectionLinks**](FlagImportIntegrationCollectionLinks.md) |  | 
**items** | [**List[FlagImportIntegration]**](FlagImportIntegration.md) | An array of flag import configurations | 

## Example

```python
from launchdarkly_api.models.flag_import_integration_collection import FlagImportIntegrationCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FlagImportIntegrationCollection from a JSON string
flag_import_integration_collection_instance = FlagImportIntegrationCollection.from_json(json)
# print the JSON string representation of the object
print(FlagImportIntegrationCollection.to_json())

# convert the object into a dict
flag_import_integration_collection_dict = flag_import_integration_collection_instance.to_dict()
# create an instance of FlagImportIntegrationCollection from a dict
flag_import_integration_collection_from_dict = FlagImportIntegrationCollection.from_dict(flag_import_integration_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


