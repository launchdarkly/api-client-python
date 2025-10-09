# View


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**ViewsAccessRep**](ViewsAccessRep.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**id** | **str** | Unique ID of this view | 
**account_id** | **str** | ID of the account that owns this view | 
**project_id** | **str** | ID of the project this view belongs to | 
**project_key** | **str** | Key of the project this view belongs to | 
**key** | **str** | Unique key for the view within the account/project | 
**name** | **str** | Human-readable name for the view | 
**description** | **str** | Optional detailed description of the view | 
**generate_sdk_keys** | **bool** | Whether to generate SDK keys for this view. Defaults to false. | 
**version** | **int** | Version number for tracking changes | 
**tags** | **List[str]** | Tags associated with this view | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**archived** | **bool** | Whether this view is archived | [default to False]
**archived_at** | **int** |  | [optional] 
**deleted_at** | **int** |  | [optional] 
**deleted** | **bool** | Whether this view is deleted | [default to False]
**maintainer** | [**Maintainer**](Maintainer.md) |  | [optional] 
**flags_summary** | [**FlagsSummary**](FlagsSummary.md) |  | [optional] 
**segments_summary** | [**SegmentsSummary**](SegmentsSummary.md) |  | [optional] 
**metrics_summary** | [**MetricsSummary**](MetricsSummary.md) |  | [optional] 
**ai_configs_summary** | [**AIConfigsSummary**](AIConfigsSummary.md) |  | [optional] 
**resource_summary** | [**ResourceSummary**](ResourceSummary.md) |  | [optional] 
**flags_expanded** | [**ExpandedLinkedFlags**](ExpandedLinkedFlags.md) |  | [optional] 
**segments_expanded** | [**ExpandedLinkedSegments**](ExpandedLinkedSegments.md) |  | [optional] 
**metrics_expanded** | [**ExpandedLinkedMetrics**](ExpandedLinkedMetrics.md) |  | [optional] 
**ai_configs_expanded** | [**ExpandedLinkedAIConfigs**](ExpandedLinkedAIConfigs.md) |  | [optional] 
**resources_expanded** | [**ExpandedLinkedResources**](ExpandedLinkedResources.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.view import View

# TODO update the JSON string below
json = "{}"
# create an instance of View from a JSON string
view_instance = View.from_json(json)
# print the JSON string representation of the object
print(View.to_json())

# convert the object into a dict
view_dict = view_instance.to_dict()
# create an instance of View from a dict
view_from_dict = View.from_dict(view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


