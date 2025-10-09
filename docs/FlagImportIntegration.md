# FlagImportIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**FlagImportIntegrationLinks**](FlagImportIntegrationLinks.md) |  | 
**id** | **str** | The integration ID | 
**integration_key** | **str** | The integration key | 
**project_key** | **str** | The project key | 
**config** | **Dict[str, object]** |  | 
**tags** | **List[str]** | List of tags for this configuration | 
**name** | **str** | Name of the configuration | 
**version** | **int** | Version of the current configuration | 
**access** | [**Access**](Access.md) |  | [optional] 
**status** | [**FlagImportStatus**](FlagImportStatus.md) |  | 

## Example

```python
from launchdarkly_api.models.flag_import_integration import FlagImportIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of FlagImportIntegration from a JSON string
flag_import_integration_instance = FlagImportIntegration.from_json(json)
# print the JSON string representation of the object
print(FlagImportIntegration.to_json())

# convert the object into a dict
flag_import_integration_dict = flag_import_integration_instance.to_dict()
# create an instance of FlagImportIntegration from a dict
flag_import_integration_from_dict = FlagImportIntegration.from_dict(flag_import_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


