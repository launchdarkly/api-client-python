# TriggerPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the trigger | [optional] 
**instructions** | **List[Dict[str, object]]** | The action to perform when triggering. This should be an array with a single object that looks like &lt;code&gt;{\&quot;kind\&quot;: \&quot;flag_action\&quot;}&lt;/code&gt;. Supported flag actions are &lt;code&gt;turnFlagOn&lt;/code&gt; and &lt;code&gt;turnFlagOff&lt;/code&gt;. | [optional] 
**integration_key** | **str** | The unique identifier of the integration for your trigger. Use &lt;code&gt;generic-trigger&lt;/code&gt; for integrations not explicitly supported. | 

## Example

```python
from launchdarkly_api.models.trigger_post import TriggerPost

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerPost from a JSON string
trigger_post_instance = TriggerPost.from_json(json)
# print the JSON string representation of the object
print(TriggerPost.to_json())

# convert the object into a dict
trigger_post_dict = trigger_post_instance.to_dict()
# create an instance of TriggerPost from a dict
trigger_post_from_dict = TriggerPost.from_dict(trigger_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


