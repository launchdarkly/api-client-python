# CountBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.count_bucket import CountBucket

# TODO update the JSON string below
json = "{}"
# create an instance of CountBucket from a JSON string
count_bucket_instance = CountBucket.from_json(json)
# print the JSON string representation of the object
print(CountBucket.to_json())

# convert the object into a dict
count_bucket_dict = count_bucket_instance.to_dict()
# create an instance of CountBucket from a dict
count_bucket_from_dict = CountBucket.from_dict(count_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


