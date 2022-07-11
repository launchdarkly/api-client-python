# UserSegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the segment | 
**tags** | **[str]** | Tags for the segment | 
**creation_date** | **int** |  | 
**key** | **str** | A unique key used to reference the segment | 
**links** | [**{str: (Link,)}**](Link.md) | Links to other resources within the API. Includes the URL and content type of those resources. | 
**rules** | [**[UserSegmentRule]**](UserSegmentRule.md) | An array of the targeting rules for this segment. | 
**version** | **int** | Version of the segment | 
**deleted** | **bool** | Whether the segment has been deleted | 
**generation** | **int** | For Big Segments, how many times this segment has been created | 
**description** | **str** | A description of the segment&#39;s purpose | [optional] 
**included** | **[str]** | An array of user keys for included users. Included users are always segment members, regardless of segment rules. For Big Segments this array is either empty or omitted. | [optional] 
**excluded** | **[str]** | An array of user keys for excluded users. Segment rules bypass excluded users, so they will never be included based on rules. Excluded users may still be included explicitly. This value is omitted for Big Segments. | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**flags** | [**[FlagListingRep]**](FlagListingRep.md) |  | [optional] 
**unbounded** | **bool** | Whether this is a standard segment (false) or a Big Segment (true) | [optional] 
**unbounded_metadata** | [**SegmentMetadata**](SegmentMetadata.md) |  | [optional] 
**external** | **str** | The external data store backing this segment. Only applies to Big Segments. | [optional] 
**external_link** | **str** | The URL for the external data store backing this segment. Only applies to Big Segments. | [optional] 
**import_in_progress** | **bool** | Whether an import is currently in progress for the specified segment. Only applies to Big Segments. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


