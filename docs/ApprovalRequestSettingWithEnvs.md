# ApprovalRequestSettingWithEnvs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environments** | [**Dict[str, ApprovalRequestSetting]**](ApprovalRequestSetting.md) | Environment-specific overrides. | [optional] 
**default** | [**ApprovalRequestSetting**](ApprovalRequestSetting.md) |  | [optional] 
**strict** | [**ApprovalRequestSetting**](ApprovalRequestSetting.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.approval_request_setting_with_envs import ApprovalRequestSettingWithEnvs

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequestSettingWithEnvs from a JSON string
approval_request_setting_with_envs_instance = ApprovalRequestSettingWithEnvs.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequestSettingWithEnvs.to_json())

# convert the object into a dict
approval_request_setting_with_envs_dict = approval_request_setting_with_envs_instance.to_dict()
# create an instance of ApprovalRequestSettingWithEnvs from a dict
approval_request_setting_with_envs_from_dict = ApprovalRequestSettingWithEnvs.from_dict(approval_request_setting_with_envs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


