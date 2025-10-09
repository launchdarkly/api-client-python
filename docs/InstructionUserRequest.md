# InstructionUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of change to make to the removal date for this user from individual targeting for this flag. | 
**flag_key** | **str** | The flag key | 
**variation_id** | **str** | ID of a variation on the flag | 
**value** | **int** | The time, in Unix milliseconds, when LaunchDarkly should remove the user from individual targeting for this flag. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;addExpireUserTargetDate&lt;/code&gt; or &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt;. | [optional] 
**version** | **int** | The version of the expiring user target to update. Optional and only used if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt;. If included, update will fail if version doesn&#39;t match current version of the expiring user target. | [optional] 

## Example

```python
from launchdarkly_api.models.instruction_user_request import InstructionUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstructionUserRequest from a JSON string
instruction_user_request_instance = InstructionUserRequest.from_json(json)
# print the JSON string representation of the object
print(InstructionUserRequest.to_json())

# convert the object into a dict
instruction_user_request_dict = instruction_user_request_instance.to_dict()
# create an instance of InstructionUserRequest from a dict
instruction_user_request_from_dict = InstructionUserRequest.from_dict(instruction_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


