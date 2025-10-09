# IntegrationDeliveryConfigurationCollectionLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**parent** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.integration_delivery_configuration_collection_links import IntegrationDeliveryConfigurationCollectionLinks

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDeliveryConfigurationCollectionLinks from a JSON string
integration_delivery_configuration_collection_links_instance = IntegrationDeliveryConfigurationCollectionLinks.from_json(json)
# print the JSON string representation of the object
print(IntegrationDeliveryConfigurationCollectionLinks.to_json())

# convert the object into a dict
integration_delivery_configuration_collection_links_dict = integration_delivery_configuration_collection_links_instance.to_dict()
# create an instance of IntegrationDeliveryConfigurationCollectionLinks from a dict
integration_delivery_configuration_collection_links_from_dict = IntegrationDeliveryConfigurationCollectionLinks.from_dict(integration_delivery_configuration_collection_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


