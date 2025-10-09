# FlagTriggerInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update | [optional] 
**instructions** | **List[Dict[str, object]]** | The instructions to perform when updating. This should be an array with objects that look like &lt;code&gt;{\&quot;kind\&quot;: \&quot;trigger_action\&quot;}&lt;/code&gt;. | [optional] 

## Example

```python
from launchdarkly_api.models.flag_trigger_input import FlagTriggerInput

# TODO update the JSON string below
json = "{}"
# create an instance of FlagTriggerInput from a JSON string
flag_trigger_input_instance = FlagTriggerInput.from_json(json)
# print the JSON string representation of the object
print(FlagTriggerInput.to_json())

# convert the object into a dict
flag_trigger_input_dict = flag_trigger_input_instance.to_dict()
# create an instance of FlagTriggerInput from a dict
flag_trigger_input_from_dict = FlagTriggerInput.from_dict(flag_trigger_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


