# ExpiringUserTargetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this expiring user target | 
**version** | **int** | The version of this expiring user target | 
**expiration_date** | **int** |  | 
**user_key** | **str** | A unique key used to represent the user | 
**target_type** | **str** | A segment&#39;s target type. Included when expiring user targets are updated on a segment. | [optional] 
**variation_id** | **str** | A unique key used to represent the flag variation. Included when expiring user targets are updated on a feature flag. | [optional] 
**resource_id** | [**ResourceIDResponse**](ResourceIDResponse.md) |  | 

## Example

```python
from launchdarkly_api.models.expiring_user_target_item import ExpiringUserTargetItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringUserTargetItem from a JSON string
expiring_user_target_item_instance = ExpiringUserTargetItem.from_json(json)
# print the JSON string representation of the object
print(ExpiringUserTargetItem.to_json())

# convert the object into a dict
expiring_user_target_item_dict = expiring_user_target_item_instance.to_dict()
# create an instance of ExpiringUserTargetItem from a dict
expiring_user_target_item_from_dict = ExpiringUserTargetItem.from_dict(expiring_user_target_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


