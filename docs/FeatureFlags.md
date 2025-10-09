# FeatureFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FeatureFlag]**](FeatureFlag.md) | An array of feature flags | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**total_count** | **int** | The total number of flags | [optional] 
**total_count_with_differences** | **int** | The number of flags that have differences between environments. Only shown when query parameter &lt;code&gt;compare&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 

## Example

```python
from launchdarkly_api.models.feature_flags import FeatureFlags

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlags from a JSON string
feature_flags_instance = FeatureFlags.from_json(json)
# print the JSON string representation of the object
print(FeatureFlags.to_json())

# convert the object into a dict
feature_flags_dict = feature_flags_instance.to_dict()
# create an instance of FeatureFlags from a dict
feature_flags_from_dict = FeatureFlags.from_dict(feature_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


