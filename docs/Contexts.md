# Contexts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** | The number of contexts | [optional] 
**environment_id** | **str** | The environment ID where the context was evaluated | 
**continuation_token** | **str** | An obfuscated string that references the last context instance on the previous page of results. You can use this for pagination, however, we recommend using the &lt;code&gt;next&lt;/code&gt; link instead. | [optional] 
**items** | [**List[ContextRecord]**](ContextRecord.md) | A collection of contexts. Can include multiple versions of contexts that have the same &lt;code&gt;kind&lt;/code&gt; and &lt;code&gt;key&lt;/code&gt;, but different &lt;code&gt;applicationId&lt;/code&gt;s. | 

## Example

```python
from launchdarkly_api.models.contexts import Contexts

# TODO update the JSON string below
json = "{}"
# create an instance of Contexts from a JSON string
contexts_instance = Contexts.from_json(json)
# print the JSON string representation of the object
print(Contexts.to_json())

# convert the object into a dict
contexts_dict = contexts_instance.to_dict()
# create an instance of Contexts from a dict
contexts_from_dict = Contexts.from_dict(contexts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


