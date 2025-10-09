# ContextSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | A collection of context filters | [optional] 
**sort** | **str** | Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying &lt;code&gt;ts&lt;/code&gt; for this value, or descending order by specifying &lt;code&gt;-ts&lt;/code&gt;. | [optional] 
**limit** | **int** | Specifies the maximum number of items in the collection to return (max: 50, default: 20) | [optional] 
**continuation_token** | **str** | Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the &lt;code&gt;next&lt;/code&gt; link instead, because this value is an obfuscated string. | [optional] 

## Example

```python
from launchdarkly_api.models.context_search import ContextSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ContextSearch from a JSON string
context_search_instance = ContextSearch.from_json(json)
# print the JSON string representation of the object
print(ContextSearch.to_json())

# convert the object into a dict
context_search_dict = context_search_instance.to_dict()
# create an instance of ContextSearch from a dict
context_search_from_dict = ContextSearch.from_dict(context_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


