# CountBucketsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**List[CountBucket]**](CountBucket.md) |  | 
**total_count** | **int** |  | 
**bucket_interval_ms** | **int** |  | 

## Example

```python
from launchdarkly_api.models.count_buckets_result import CountBucketsResult

# TODO update the JSON string below
json = "{}"
# create an instance of CountBucketsResult from a JSON string
count_buckets_result_instance = CountBucketsResult.from_json(json)
# print the JSON string representation of the object
print(CountBucketsResult.to_json())

# convert the object into a dict
count_buckets_result_dict = count_buckets_result_instance.to_dict()
# create an instance of CountBucketsResult from a dict
count_buckets_result_from_dict = CountBucketsResult.from_dict(count_buckets_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


