# PatchSegmentInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of change to make to the user&#39;s removal date from this segment | 
**user_key** | **str** | A unique key used to represent the user | 
**target_type** | **str** | The segment&#39;s target type | 
**value** | **int** | The time, in Unix milliseconds, when the user should be removed from this segment. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;addExpireUserTargetDate&lt;/code&gt; or &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt;. | [optional] 
**version** | **int** | The version of the segment to update. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt;. | [optional] 

## Example

```python
from launchdarkly_api.models.patch_segment_instruction import PatchSegmentInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSegmentInstruction from a JSON string
patch_segment_instruction_instance = PatchSegmentInstruction.from_json(json)
# print the JSON string representation of the object
print(PatchSegmentInstruction.to_json())

# convert the object into a dict
patch_segment_instruction_dict = patch_segment_instruction_instance.to_dict()
# create an instance of PatchSegmentInstruction from a dict
patch_segment_instruction_from_dict = PatchSegmentInstruction.from_dict(patch_segment_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


