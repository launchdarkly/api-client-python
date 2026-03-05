# ViewLinkRequestKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | Keys of the resources (flags, segments) to link/unlink | 
**filter** | **str** | Optional filter string to determine which resources should be linked. Resources only need to match either the filter or explicitly-listed keys to be linked (union). Uses the same syntax as list endpoints: flags use comma-separated field:value filters, segments use queryfilter syntax.  Supported filters by resource type: - flags: query, tags, maintainerId, maintainerTeamKey, type, status, state, staleState, sdkAvailability, targeting, hasExperiment, hasDataExport, evaluated, creationDate, contextKindTargeted, contextKindsEvaluated, filterEnv, segmentTargeted, codeReferences.min, codeReferences.max, excludeSettings, releasePipeline, applicationEvaluated, purpose, guardedRollout, view, key, name, archived, followerId - segments (queryfilter): query, tags, keys, excludedKeys, unbounded, external, view, type Some filters are only available when the corresponding feature is enabled on your account.  | [optional] 
**comment** | **str** | Optional comment for the link/unlink operation | [optional] [default to '']

## Example

```python
from launchdarkly_api.models.view_link_request_keys import ViewLinkRequestKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkRequestKeys from a JSON string
view_link_request_keys_instance = ViewLinkRequestKeys.from_json(json)
# print the JSON string representation of the object
print(ViewLinkRequestKeys.to_json())

# convert the object into a dict
view_link_request_keys_dict = view_link_request_keys_instance.to_dict()
# create an instance of ViewLinkRequestKeys from a dict
view_link_request_keys_from_dict = ViewLinkRequestKeys.from_dict(view_link_request_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


