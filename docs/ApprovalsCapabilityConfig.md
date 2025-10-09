# ApprovalsCapabilityConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_form_variables** | [**List[FormVariable]**](FormVariable.md) | The additional form variables for the approvals capability | [optional] 

## Example

```python
from launchdarkly_api.models.approvals_capability_config import ApprovalsCapabilityConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalsCapabilityConfig from a JSON string
approvals_capability_config_instance = ApprovalsCapabilityConfig.from_json(json)
# print the JSON string representation of the object
print(ApprovalsCapabilityConfig.to_json())

# convert the object into a dict
approvals_capability_config_dict = approvals_capability_config_instance.to_dict()
# create an instance of ApprovalsCapabilityConfig from a dict
approvals_capability_config_from_dict = ApprovalsCapabilityConfig.from_dict(approvals_capability_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


