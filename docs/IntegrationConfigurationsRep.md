# IntegrationConfigurationsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**id** | **str** | The unique identifier for this integration configuration | 
**name** | **str** | A human-friendly name for the integration | 
**created_at** | **int** |  | [optional] 
**integration_key** | **str** | The type of integration | [optional] 
**tags** | **List[str]** | An array of tags for this integration | [optional] 
**enabled** | **bool** | Whether the integration is currently active | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**config_values** | **Dict[str, object]** | Details on configuration for an integration of this type. Refer to the &lt;code&gt;formVariables&lt;/code&gt; field in the corresponding &lt;code&gt;manifest.json&lt;/code&gt; for a full list of fields for each integration. | [optional] 
**capability_config** | [**CapabilityConfigRep**](CapabilityConfigRep.md) |  | [optional] 
**snowflake_setup_script** | **str** | Consolidated SQL script for Snowflake Warehouse Native Experimentation setup. Present only for setup endpoint responses. | [optional] 
**redshift_setup_scripts** | **List[str]** | SQL setup scripts (4 parts) for Redshift Native Experimentation setup. Present only for setup endpoint responses. | [optional] 
**redshift_iam_permissions_policy** | **str** | IAM permissions policy JSON for the customer&#39;s Redshift IAM role. Present only for setup endpoint responses. | [optional] 
**redshift_iam_trust_policy** | **str** | IAM trust policy JSON for the customer&#39;s Redshift IAM role. Present only for setup endpoint responses. | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this integration configuration. Defaults to the member who created it. | [optional] 

## Example

```python
from launchdarkly_api.models.integration_configurations_rep import IntegrationConfigurationsRep

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationConfigurationsRep from a JSON string
integration_configurations_rep_instance = IntegrationConfigurationsRep.from_json(json)
# print the JSON string representation of the object
print(IntegrationConfigurationsRep.to_json())

# convert the object into a dict
integration_configurations_rep_dict = integration_configurations_rep_instance.to_dict()
# create an instance of IntegrationConfigurationsRep from a dict
integration_configurations_rep_from_dict = IntegrationConfigurationsRep.from_dict(integration_configurations_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


