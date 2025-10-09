# ReleasePipelineCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReleasePipeline]**](ReleasePipeline.md) | An array of release pipelines | 
**total_count** | **int** | Total number of release pipelines | 

## Example

```python
from launchdarkly_api.models.release_pipeline_collection import ReleasePipelineCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePipelineCollection from a JSON string
release_pipeline_collection_instance = ReleasePipelineCollection.from_json(json)
# print the JSON string representation of the object
print(ReleasePipelineCollection.to_json())

# convert the object into a dict
release_pipeline_collection_dict = release_pipeline_collection_instance.to_dict()
# create an instance of ReleasePipelineCollection from a dict
release_pipeline_collection_from_dict = ReleasePipelineCollection.from_dict(release_pipeline_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


