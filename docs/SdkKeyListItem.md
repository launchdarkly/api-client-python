# SdkKeyListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**kind** | [**SdkKeyKind**](SdkKeyKind.md) |  | 
**key** | **str** | The user-defined identifying key of the SDK key. This is used solely to identify an SDK key and is distinct from the value field, which is the actual SDK key value. | 
**name** | **str** | The human-readable name of the SDK key. | 
**description** | **str** | The optional description of the SDK key. | [optional] 
**expiry** | **int** |  | [optional] 
**value** | **str** | The string value of the SDK key. Use this when configuring your SDK. | 
**is_default** | **bool** | Indicates if this SDK key is the system-defined default for the environment. There may also be an expiring default SDK key for the environment (not possible with mobile keys). | 
**created_by_member_id** | **str** | The ID of the member who created the SDK key. This field is immutable. | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**version** | **int** | The auto-incremented version number of the SDK key. | 
**environment_summary** | [**SdkKeysEnvironmentSummary**](SdkKeysEnvironmentSummary.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.sdk_key_list_item import SdkKeyListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SdkKeyListItem from a JSON string
sdk_key_list_item_instance = SdkKeyListItem.from_json(json)
# print the JSON string representation of the object
print(SdkKeyListItem.to_json())

# convert the object into a dict
sdk_key_list_item_dict = sdk_key_list_item_instance.to_dict()
# create an instance of SdkKeyListItem from a dict
sdk_key_list_item_from_dict = SdkKeyListItem.from_dict(sdk_key_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


