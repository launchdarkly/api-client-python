# IntegrationMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | 
**external_status** | [**IntegrationStatus**](IntegrationStatus.md) |  | 
**external_url** | **str** |  | 
**last_checked** | **int** |  | 

## Example

```python
from launchdarkly_api.models.integration_metadata import IntegrationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationMetadata from a JSON string
integration_metadata_instance = IntegrationMetadata.from_json(json)
# print the JSON string representation of the object
print(IntegrationMetadata.to_json())

# convert the object into a dict
integration_metadata_dict = integration_metadata_instance.to_dict()
# create an instance of IntegrationMetadata from a dict
integration_metadata_from_dict = IntegrationMetadata.from_dict(integration_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


