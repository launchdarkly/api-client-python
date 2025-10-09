# FlagListingRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The flag name | 
**key** | **str** | The flag key | 
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**site** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_listing_rep import FlagListingRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagListingRep from a JSON string
flag_listing_rep_instance = FlagListingRep.from_json(json)
# print the JSON string representation of the object
print(FlagListingRep.to_json())

# convert the object into a dict
flag_listing_rep_dict = flag_listing_rep_instance.to_dict()
# create an instance of FlagListingRep from a dict
flag_listing_rep_from_dict = FlagListingRep.from_dict(flag_listing_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


