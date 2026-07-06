# AnalysisConfigRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bayesian_threshold** | **str** | The threshold for the Probability to Beat Baseline (PBBL) and Probability to Be Best (PBB) comparisons for the Bayesian results analysis approach.  Value should be between 0-100 inclusive. | [optional] 
**significance_threshold** | **str** | The significance threshold for the frequentist results analysis approach. Value should be between 0.0-1.0 inclusive. | [optional] 
**test_direction** | **str** | The test sided direction for the frequentist results analysis approach. | [optional] 
**multiple_comparison_correction_method** | **str** | The method for multiple comparison correction. | [optional] 
**multiple_comparison_correction_scope** | **str** | The scope for multiple comparison correction. | [optional] 
**sequential_testing_enabled** | **bool** | Whether sequential testing is enabled for Frequentist analysis | [optional] 

## Example

```python
from launchdarkly_api.models.analysis_config_rep import AnalysisConfigRep

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisConfigRep from a JSON string
analysis_config_rep_instance = AnalysisConfigRep.from_json(json)
# print the JSON string representation of the object
print(AnalysisConfigRep.to_json())

# convert the object into a dict
analysis_config_rep_dict = analysis_config_rep_instance.to_dict()
# create an instance of AnalysisConfigRep from a dict
analysis_config_rep_from_dict = AnalysisConfigRep.from_dict(analysis_config_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


