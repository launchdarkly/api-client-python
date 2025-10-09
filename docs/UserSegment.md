# UserSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the segment. | 
**description** | **str** | A description of the segment&#39;s purpose. Defaults to &lt;code&gt;null&lt;/code&gt; and is omitted in the response if not provided. | [optional] 
**tags** | **List[str]** | Tags for the segment. Defaults to an empty array. | 
**creation_date** | **int** |  | 
**last_modified_date** | **int** |  | 
**key** | **str** | A unique key used to reference the segment | 
**included** | **List[str]** | An array of keys for included targets. Included individual targets are always segment members, regardless of segment rules. For list-based segments over 15,000 entries, also called big segments, this array is either empty or omitted. | [optional] 
**excluded** | **List[str]** | An array of keys for excluded targets. Segment rules bypass individual excluded targets, so they will never be included based on rules. Excluded targets may still be included explicitly. This value is omitted for list-based segments over 15,000 entries, also called big segments. | [optional] 
**included_contexts** | [**List[SegmentTarget]**](SegmentTarget.md) |  | [optional] 
**excluded_contexts** | [**List[SegmentTarget]**](SegmentTarget.md) |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**rules** | [**List[UserSegmentRule]**](UserSegmentRule.md) | An array of the targeting rules for this segment. | 
**version** | **int** | Version of the segment | 
**deleted** | **bool** | Whether the segment has been deleted | 
**access** | [**Access**](Access.md) |  | [optional] 
**flags** | [**List[FlagListingRep]**](FlagListingRep.md) | A list of flags targeting this segment. Only included when getting a single segment, using the &lt;code&gt;getSegment&lt;/code&gt; endpoint. | [optional] 
**unbounded** | **bool** | Whether this is a standard segment (&lt;code&gt;false&lt;/code&gt;) or a big segment (&lt;code&gt;true&lt;/code&gt;). Standard segments include rule-based segments and smaller list-based segments. Big segments include larger list-based segments and synced segments. If omitted, the segment is a standard segment. | [optional] 
**unbounded_context_kind** | **str** | For big segments, the targeted context kind. | [optional] 
**generation** | **int** | For big segments, how many times this segment has been created. | 
**unbounded_metadata** | [**SegmentMetadata**](SegmentMetadata.md) |  | [optional] 
**external** | **str** | The external data store backing this segment. Only applies to synced segments. | [optional] 
**external_link** | **str** | The URL for the external data store backing this segment. Only applies to synced segments. | [optional] 
**import_in_progress** | **bool** | Whether an import is currently in progress for the specified segment. Only applies to big segments. | [optional] 

## Example

```python
from launchdarkly_api.models.user_segment import UserSegment

# TODO update the JSON string below
json = "{}"
# create an instance of UserSegment from a JSON string
user_segment_instance = UserSegment.from_json(json)
# print the JSON string representation of the object
print(UserSegment.to_json())

# convert the object into a dict
user_segment_dict = user_segment_instance.to_dict()
# create an instance of UserSegment from a dict
user_segment_from_dict = UserSegment.from_dict(user_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


