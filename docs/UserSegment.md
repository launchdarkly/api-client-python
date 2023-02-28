# UserSegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the segment. | 
**tags** | **[str]** | Tags for the segment. Defaults to an empty array. | 
**creation_date** | **int** |  | 
**key** | **str** | A unique key used to reference the segment | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**rules** | [**[UserSegmentRule]**](UserSegmentRule.md) | An array of the targeting rules for this segment. | 
**version** | **int** | Version of the segment | 
**deleted** | **bool** | Whether the segment has been deleted | 
**generation** | **int** | For Big Segments, how many times this segment has been created | 
**description** | **str** | A description of the segment&#39;s purpose. Defaults to &lt;code&gt;null&lt;/code&gt; and is omitted in the response if not provided. | [optional] 
**included** | **[str]** | An array of keys for included targets. Included individual targets are always segment members, regardless of segment rules. For Big Segments this array is either empty or omitted. | [optional] 
**excluded** | **[str]** | An array of keys for excluded targets. Segment rules bypass individual excluded targets, so they will never be included based on rules. Excluded targets may still be included explicitly. This value is omitted for Big Segments. | [optional] 
**included_contexts** | [**[SegmentTarget]**](SegmentTarget.md) |  | [optional] 
**excluded_contexts** | [**[SegmentTarget]**](SegmentTarget.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**flags** | [**[FlagListingRep]**](FlagListingRep.md) |  | [optional] 
**unbounded** | **bool** | Whether this is a standard segment (&lt;code&gt;false&lt;/code&gt;) or a Big Segment (&lt;code&gt;true&lt;/code&gt;). If omitted, the segment is a standard segment. | [optional] 
**unbounded_context_kind** | **str** |  | [optional] 
**unbounded_metadata** | [**SegmentMetadata**](SegmentMetadata.md) |  | [optional] 
**external** | **str** | The external data store backing this segment. Only applies to Big Segments. | [optional] 
**external_link** | **str** | The URL for the external data store backing this segment. Only applies to Big Segments. | [optional] 
**import_in_progress** | **bool** | Whether an import is currently in progress for the specified segment. Only applies to Big Segments. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


