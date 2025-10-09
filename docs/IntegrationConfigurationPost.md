# IntegrationConfigurationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the integration configuration | 
**enabled** | **bool** | Whether the integration configuration is enabled. If omitted, defaults to true | [optional] 
**tags** | **List[str]** | Tags for the integration | [optional] 
**config_values** | **Dict[str, object]** | The unique set of fields required to configure the integration. Refer to the &lt;code&gt;formVariables&lt;/code&gt; field in the corresponding &lt;code&gt;manifest.json&lt;/code&gt; at https://github.com/launchdarkly/integration-framework/tree/main/integrations for a full list of fields for the integration you wish to configure. | 
**capability_config** | [**CapabilityConfigPost**](CapabilityConfigPost.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.integration_configuration_post import IntegrationConfigurationPost

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationConfigurationPost from a JSON string
integration_configuration_post_instance = IntegrationConfigurationPost.from_json(json)
# print the JSON string representation of the object
print(IntegrationConfigurationPost.to_json())

# convert the object into a dict
integration_configuration_post_dict = integration_configuration_post_instance.to_dict()
# create an instance of IntegrationConfigurationPost from a dict
integration_configuration_post_from_dict = IntegrationConfigurationPost.from_dict(integration_configuration_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


