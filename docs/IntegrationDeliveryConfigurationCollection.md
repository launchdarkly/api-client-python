# IntegrationDeliveryConfigurationCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**IntegrationDeliveryConfigurationCollectionLinks**](IntegrationDeliveryConfigurationCollectionLinks.md) |  | 
**items** | [**List[IntegrationDeliveryConfiguration]**](IntegrationDeliveryConfiguration.md) | An array of integration delivery configurations | 

## Example

```python
from launchdarkly_api.models.integration_delivery_configuration_collection import IntegrationDeliveryConfigurationCollection

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDeliveryConfigurationCollection from a JSON string
integration_delivery_configuration_collection_instance = IntegrationDeliveryConfigurationCollection.from_json(json)
# print the JSON string representation of the object
print(IntegrationDeliveryConfigurationCollection.to_json())

# convert the object into a dict
integration_delivery_configuration_collection_dict = integration_delivery_configuration_collection_instance.to_dict()
# create an instance of IntegrationDeliveryConfigurationCollection from a dict
integration_delivery_configuration_collection_from_dict = IntegrationDeliveryConfigurationCollection.from_dict(integration_delivery_configuration_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


