# ReleasePipeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the release pipeline was created | 
**description** | **str** | The release pipeline description | [optional] 
**key** | **str** | The release pipeline key | 
**name** | **str** | The release pipeline name | 
**phases** | [**List[Phase]**](Phase.md) | An ordered list of the release pipeline phases. Each phase is a logical grouping of one or more environments that share attributes for rolling out changes. | 
**tags** | **List[str]** | A list of the release pipeline&#39;s tags | [optional] 
**version** | **int** | The release pipeline version | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**is_project_default** | **bool** | Whether this release pipeline is the default pipeline for the project | [optional] 
**is_legacy** | **bool** | Whether this release pipeline is a legacy pipeline | [optional] 

## Example

```python
from launchdarkly_api.models.release_pipeline import ReleasePipeline

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePipeline from a JSON string
release_pipeline_instance = ReleasePipeline.from_json(json)
# print the JSON string representation of the object
print(ReleasePipeline.to_json())

# convert the object into a dict
release_pipeline_dict = release_pipeline_instance.to_dict()
# create an instance of ReleasePipeline from a dict
release_pipeline_from_dict = ReleasePipeline.from_dict(release_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


