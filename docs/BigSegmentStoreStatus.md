# BigSegmentStoreStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether the persistent store integration is fully synchronized with the LaunchDarkly environment, and the &lt;code&gt;lastSync&lt;/code&gt; occurred within a few minutes | [optional] 
**potentially_stale** | **bool** | Whether the persistent store integration may not be fully synchronized with the LaunchDarkly environment. &lt;code&gt;true&lt;/code&gt; if the integration could be stale. | [optional] 
**last_sync** | **int** |  | [optional] 
**last_error** | **int** |  | [optional] 
**errors** | [**List[StoreIntegrationError]**](StoreIntegrationError.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.big_segment_store_status import BigSegmentStoreStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BigSegmentStoreStatus from a JSON string
big_segment_store_status_instance = BigSegmentStoreStatus.from_json(json)
# print the JSON string representation of the object
print(BigSegmentStoreStatus.to_json())

# convert the object into a dict
big_segment_store_status_dict = big_segment_store_status_instance.to_dict()
# create an instance of BigSegmentStoreStatus from a dict
big_segment_store_status_from_dict = BigSegmentStoreStatus.from_dict(big_segment_store_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


