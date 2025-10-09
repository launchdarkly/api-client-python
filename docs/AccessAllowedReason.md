# AccessAllowedReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | **List[str]** | Resource specifier strings | [optional] 
**not_resources** | **List[str]** | Targeted resources are the resources NOT in this list. The &lt;code&gt;resources&lt;/code&gt; and &lt;code&gt;notActions&lt;/code&gt; fields must be empty to use this field. | [optional] 
**actions** | **List[str]** | Actions to perform on a resource | [optional] 
**not_actions** | **List[str]** | Targeted actions are the actions NOT in this list. The &lt;code&gt;actions&lt;/code&gt; and &lt;code&gt;notResources&lt;/code&gt; fields must be empty to use this field. | [optional] 
**effect** | **str** | Whether this statement should allow or deny actions on the resources. | 
**role_name** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.access_allowed_reason import AccessAllowedReason

# TODO update the JSON string below
json = "{}"
# create an instance of AccessAllowedReason from a JSON string
access_allowed_reason_instance = AccessAllowedReason.from_json(json)
# print the JSON string representation of the object
print(AccessAllowedReason.to_json())

# convert the object into a dict
access_allowed_reason_dict = access_allowed_reason_instance.to_dict()
# create an instance of AccessAllowedReason from a dict
access_allowed_reason_from_dict = AccessAllowedReason.from_dict(access_allowed_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


