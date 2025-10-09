# PatchSegmentExpiringTargetInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of change to make to the context&#39;s removal date from this segment | 
**context_key** | **str** | A unique key used to represent the context | 
**context_kind** | **str** | The kind of context | 
**target_type** | **str** | The segment&#39;s target type | 
**value** | **int** | The time, in Unix milliseconds, when the context should be removed from this segment. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;addExpiringTarget&lt;/code&gt; or &lt;code&gt;updateExpiringTarget&lt;/code&gt;. | [optional] 
**version** | **int** | The version of the expiring target to update. Optional and only used if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;updateExpiringTarget&lt;/code&gt;. If included, update will fail if version doesn&#39;t match current version of the expiring target. | [optional] 

## Example

```python
from launchdarkly_api.models.patch_segment_expiring_target_instruction import PatchSegmentExpiringTargetInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSegmentExpiringTargetInstruction from a JSON string
patch_segment_expiring_target_instruction_instance = PatchSegmentExpiringTargetInstruction.from_json(json)
# print the JSON string representation of the object
print(PatchSegmentExpiringTargetInstruction.to_json())

# convert the object into a dict
patch_segment_expiring_target_instruction_dict = patch_segment_expiring_target_instruction_instance.to_dict()
# create an instance of PatchSegmentExpiringTargetInstruction from a dict
patch_segment_expiring_target_instruction_from_dict = PatchSegmentExpiringTargetInstruction.from_dict(patch_segment_expiring_target_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


