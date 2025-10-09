# ExpandedFlagRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the feature flag | 
**kind** | **str** | Kind of feature flag | 
**description** | **str** | Description of the feature flag | [optional] 
**key** | **str** | A unique key used to reference the flag in your code | 
**version** | **int** | Version of the feature flag | 
**creation_date** | **int** |  | 
**include_in_snippet** | **bool** | Deprecated, use &lt;code&gt;clientSideAvailability&lt;/code&gt;. Whether this flag should be made available to the client-side JavaScript SDK | [optional] 
**client_side_availability** | [**ClientSideAvailability**](ClientSideAvailability.md) |  | [optional] 
**variations** | [**List[Variation]**](Variation.md) | An array of possible variations for the flag | 
**temporary** | **bool** | Whether the flag is a temporary flag | 
**tags** | **List[str]** | Tags for the feature flag | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**maintainer_id** | **str** | The ID of the member who maintains the flag | [optional] 
**maintainer** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**custom_properties** | [**Dict[str, CustomProperty]**](CustomProperty.md) |  | 
**archived** | **bool** | Boolean indicating if the feature flag is archived | 
**archived_date** | **int** |  | [optional] 
**defaults** | [**Defaults**](Defaults.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_flag_rep import ExpandedFlagRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedFlagRep from a JSON string
expanded_flag_rep_instance = ExpandedFlagRep.from_json(json)
# print the JSON string representation of the object
print(ExpandedFlagRep.to_json())

# convert the object into a dict
expanded_flag_rep_dict = expanded_flag_rep_instance.to_dict()
# create an instance of ExpandedFlagRep from a dict
expanded_flag_rep_from_dict = ExpandedFlagRep.from_dict(expanded_flag_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


