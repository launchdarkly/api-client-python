# IntegrationDeliveryConfigurationLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**parent** | [**Link**](Link.md) |  | 
**project** | [**Link**](Link.md) |  | 
**environment** | [**Link**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.integration_delivery_configuration_links import IntegrationDeliveryConfigurationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDeliveryConfigurationLinks from a JSON string
integration_delivery_configuration_links_instance = IntegrationDeliveryConfigurationLinks.from_json(json)
# print the JSON string representation of the object
print(IntegrationDeliveryConfigurationLinks.to_json())

# convert the object into a dict
integration_delivery_configuration_links_dict = integration_delivery_configuration_links_instance.to_dict()
# create an instance of IntegrationDeliveryConfigurationLinks from a dict
integration_delivery_configuration_links_from_dict = IntegrationDeliveryConfigurationLinks.from_dict(integration_delivery_configuration_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


