# RateLimitedErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.rate_limited_error_rep import RateLimitedErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitedErrorRep from a JSON string
rate_limited_error_rep_instance = RateLimitedErrorRep.from_json(json)
# print the JSON string representation of the object
print(RateLimitedErrorRep.to_json())

# convert the object into a dict
rate_limited_error_rep_dict = rate_limited_error_rep_instance.to_dict()
# create an instance of RateLimitedErrorRep from a dict
rate_limited_error_rep_from_dict = RateLimitedErrorRep.from_dict(rate_limited_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


