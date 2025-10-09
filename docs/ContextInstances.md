# ContextInstances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** | The number of unique context instances | [optional] 
**environment_id** | **str** | The environment ID | 
**continuation_token** | **str** | An obfuscated string that references the last context instance on the previous page of results. You can use this for pagination, however, we recommend using the &lt;code&gt;next&lt;/code&gt; link instead. | [optional] 
**items** | [**List[ContextInstanceRecord]**](ContextInstanceRecord.md) | A collection of context instances. Can include multiple versions of context instances that have the same &lt;code&gt;id&lt;/code&gt;, but different &lt;code&gt;applicationId&lt;/code&gt;s. | 

## Example

```python
from launchdarkly_api.models.context_instances import ContextInstances

# TODO update the JSON string below
json = "{}"
# create an instance of ContextInstances from a JSON string
context_instances_instance = ContextInstances.from_json(json)
# print the JSON string representation of the object
print(ContextInstances.to_json())

# convert the object into a dict
context_instances_dict = context_instances_instance.to_dict()
# create an instance of ContextInstances from a dict
context_instances_from_dict = ContextInstances.from_dict(context_instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


