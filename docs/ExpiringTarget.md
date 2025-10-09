# ExpiringTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this expiring target | 
**version** | **int** | The version of this expiring target | 
**expiration_date** | **int** |  | 
**context_kind** | **str** | The context kind of the context to be removed | 
**context_key** | **str** | A unique key used to represent the context to be removed | 
**target_type** | **str** | A segment&#39;s target type, &lt;code&gt;included&lt;/code&gt; or &lt;code&gt;excluded&lt;/code&gt;. Included when expiring targets are updated on a segment. | [optional] 
**variation_id** | **str** | A unique ID used to represent the flag variation. Included when expiring targets are updated on a feature flag. | [optional] 
**resource_id** | [**ResourceId**](ResourceId.md) |  | 

## Example

```python
from launchdarkly_api.models.expiring_target import ExpiringTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringTarget from a JSON string
expiring_target_instance = ExpiringTarget.from_json(json)
# print the JSON string representation of the object
print(ExpiringTarget.to_json())

# convert the object into a dict
expiring_target_dict = expiring_target_instance.to_dict()
# create an instance of ExpiringTarget from a dict
expiring_target_from_dict = ExpiringTarget.from_dict(expiring_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


