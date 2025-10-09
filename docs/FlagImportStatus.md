# FlagImportStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The current status of the import integrations related import job | [optional] 
**last_import** | **int** |  | [optional] 
**last_error** | **int** |  | [optional] 
**errors** | [**List[StatusResponse]**](StatusResponse.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_import_status import FlagImportStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FlagImportStatus from a JSON string
flag_import_status_instance = FlagImportStatus.from_json(json)
# print the JSON string representation of the object
print(FlagImportStatus.to_json())

# convert the object into a dict
flag_import_status_dict = flag_import_status_instance.to_dict()
# create an instance of FlagImportStatus from a dict
flag_import_status_from_dict = FlagImportStatus.from_dict(flag_import_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


