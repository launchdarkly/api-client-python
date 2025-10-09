# ReviewOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**kind** | **str** |  | 
**creation_date** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**member_id** | **str** |  | [optional] 
**service_token_id** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.review_output import ReviewOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewOutput from a JSON string
review_output_instance = ReviewOutput.from_json(json)
# print the JSON string representation of the object
print(ReviewOutput.to_json())

# convert the object into a dict
review_output_dict = review_output_instance.to_dict()
# create an instance of ReviewOutput from a dict
review_output_from_dict = ReviewOutput.from_dict(review_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


