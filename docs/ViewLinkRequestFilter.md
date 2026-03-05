# ViewLinkRequestFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filter string to match resources for linking. Uses the same syntax as list endpoints: flags use comma-separated field:value filters, segments use queryfilter syntax.  Supported filters by resource type: - flags: query, tags, maintainerId, maintainerTeamKey, type, status, state, staleState, sdkAvailability, targeting, hasExperiment, hasDataExport, evaluated, creationDate, contextKindTargeted, contextKindsEvaluated, filterEnv, segmentTargeted, codeReferences.min, codeReferences.max, excludeSettings, releasePipeline, applicationEvaluated, purpose, guardedRollout, view, key, name, archived, followerId - segments (queryfilter): query, tags, keys, excludedKeys, unbounded, external, view, type Some filters are only available when the corresponding feature is enabled on your account.  | 
**environment_id** | **str** | Required when using filter for segment resources. Specifies which environment to query for segments matching the filter. Ignored for flag resources (flags are global across environments).  | [optional] 
**comment** | **str** | Optional comment for the link/unlink operation | [optional] [default to '']

## Example

```python
from launchdarkly_api.models.view_link_request_filter import ViewLinkRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkRequestFilter from a JSON string
view_link_request_filter_instance = ViewLinkRequestFilter.from_json(json)
# print the JSON string representation of the object
print(ViewLinkRequestFilter.to_json())

# convert the object into a dict
view_link_request_filter_dict = view_link_request_filter_instance.to_dict()
# create an instance of ViewLinkRequestFilter from a dict
view_link_request_filter_from_dict = ViewLinkRequestFilter.from_dict(view_link_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


