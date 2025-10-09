# FlagLinkRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**key** | **str** | The flag link key | [optional] 
**integration_key** | **str** | The integration key for an integration whose &lt;code&gt;manifest.json&lt;/code&gt; includes the &lt;code&gt;flagLink&lt;/code&gt; capability, if this is a flag link for an existing integration | [optional] 
**id** | **str** | The ID of this flag link | 
**deep_link** | **str** | The URL for the external resource the flag is linked to | 
**timestamp** | [**TimestampRep**](TimestampRep.md) |  | 
**title** | **str** | The title of the flag link | [optional] 
**description** | **str** | The description of the flag link | [optional] 
**metadata** | **Dict[str, str]** | The metadata required by this integration in order to create a flag link, if this is a flag link for an existing integration. Defined in the integration&#39;s &lt;code&gt;manifest.json&lt;/code&gt; file under &lt;code&gt;flagLink&lt;/code&gt;. | [optional] 
**created_at** | **int** |  | 
**member** | [**FlagLinkMember**](FlagLinkMember.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_link_rep import FlagLinkRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagLinkRep from a JSON string
flag_link_rep_instance = FlagLinkRep.from_json(json)
# print the JSON string representation of the object
print(FlagLinkRep.to_json())

# convert the object into a dict
flag_link_rep_dict = flag_link_rep_instance.to_dict()
# create an instance of FlagLinkRep from a dict
flag_link_rep_from_dict = FlagLinkRep.from_dict(flag_link_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


