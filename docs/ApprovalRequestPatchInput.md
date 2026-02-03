# ApprovalRequestPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update | [optional] 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.approval_request_patch_input import ApprovalRequestPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequestPatchInput from a JSON string
approval_request_patch_input_instance = ApprovalRequestPatchInput.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequestPatchInput.to_json())

# convert the object into a dict
approval_request_patch_input_dict = approval_request_patch_input_instance.to_dict()
# create an instance of ApprovalRequestPatchInput from a dict
approval_request_patch_input_from_dict = ApprovalRequestPatchInput.from_dict(approval_request_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


