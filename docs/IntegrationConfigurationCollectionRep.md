# IntegrationConfigurationCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IntegrationConfigurationsRep]**](IntegrationConfigurationsRep.md) | An array of integration configurations | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.integration_configuration_collection_rep import IntegrationConfigurationCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationConfigurationCollectionRep from a JSON string
integration_configuration_collection_rep_instance = IntegrationConfigurationCollectionRep.from_json(json)
# print the JSON string representation of the object
print(IntegrationConfigurationCollectionRep.to_json())

# convert the object into a dict
integration_configuration_collection_rep_dict = integration_configuration_collection_rep_instance.to_dict()
# create an instance of IntegrationConfigurationCollectionRep from a dict
integration_configuration_collection_rep_from_dict = IntegrationConfigurationCollectionRep.from_dict(integration_configuration_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


