# CovariateInfoRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the covariate matrix | 
**file_name** | **str** | The file name of the uploaded covariate matrix | 
**created_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.covariate_info_rep import CovariateInfoRep

# TODO update the JSON string below
json = "{}"
# create an instance of CovariateInfoRep from a JSON string
covariate_info_rep_instance = CovariateInfoRep.from_json(json)
# print the JSON string representation of the object
print(CovariateInfoRep.to_json())

# convert the object into a dict
covariate_info_rep_dict = covariate_info_rep_instance.to_dict()
# create an instance of CovariateInfoRep from a dict
covariate_info_rep_from_dict = CovariateInfoRep.from_dict(covariate_info_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


