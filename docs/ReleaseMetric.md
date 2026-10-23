# ReleaseMetric

A metric shared by every phase of a guarded release.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_key** | **str** |  | 
**metric_version_id** | **UUID** |  | [optional] [readonly] 
**auto_rollback** | **bool** | Whether a regression automatically reverts the release. | 
**definition** | [**EnvironmentReleasesMetricListingRep**](EnvironmentReleasesMetricListingRep.md) | Present only when the caller requests &#x60;expand&#x3D;metrics&#x60; and the pinned metric version still exists. A metric whose pinned version has been deleted keeps its &#x60;metricKey&#x60; and &#x60;metricVersionId&#x60; but has no definition.  | [optional] [readonly] 

## Example

```python
from launchdarkly_api.models.release_metric import ReleaseMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseMetric from a JSON string
release_metric_instance = ReleaseMetric.from_json(json)
# print the JSON string representation of the object
print(ReleaseMetric.to_json())

# convert the object into a dict
release_metric_dict = release_metric_instance.to_dict()
# create an instance of ReleaseMetric from a dict
release_metric_from_dict = ReleaseMetric.from_dict(release_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


