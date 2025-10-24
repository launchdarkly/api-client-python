# CovarianceInfoRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the covariance matrix | 
**file_name** | **str** | The file name of the uploaded covariance matrix | 
**created_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.covariance_info_rep import CovarianceInfoRep

# TODO update the JSON string below
json = "{}"
# create an instance of CovarianceInfoRep from a JSON string
covariance_info_rep_instance = CovarianceInfoRep.from_json(json)
# print the JSON string representation of the object
print(CovarianceInfoRep.to_json())

# convert the object into a dict
covariance_info_rep_dict = covariance_info_rep_instance.to_dict()
# create an instance of CovarianceInfoRep from a dict
covariance_info_rep_from_dict = CovarianceInfoRep.from_dict(covariance_info_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


