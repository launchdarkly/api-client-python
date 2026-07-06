# AnalysisConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bayesian_threshold** | **str** | The threshold for the Probability to Beat Baseline (PBBL) and Probability to Be Best (PBB) comparisons for the Bayesian results analysis approach. | [optional] 
**significance_threshold** | **str** | The significance threshold for the frequentist results analysis approach. | [optional] 
**test_direction** | **str** | The test sided direction for the frequentist results analysis approach. | [optional] 
**multiple_comparison_correction_method** | **str** | The method to use for multiple comparison correction. | [optional] 
**multiple_comparison_correction_scope** | **str** | The scope of the multiple comparison correction. | [optional] 
**sequential_testing_enabled** | **bool** | Whether sequential testing is enabled for Frequentist analysis | [optional] 

## Example

```python
from launchdarkly_api.models.analysis_config_input import AnalysisConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisConfigInput from a JSON string
analysis_config_input_instance = AnalysisConfigInput.from_json(json)
# print the JSON string representation of the object
print(AnalysisConfigInput.to_json())

# convert the object into a dict
analysis_config_input_dict = analysis_config_input_instance.to_dict()
# create an instance of AnalysisConfigInput from a dict
analysis_config_input_from_dict = AnalysisConfigInput.from_dict(analysis_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


