# VariationSkill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the attached agent skill. | 
**version** | **int** | The pinned skill version. | 

## Example

```python
from launchdarkly_api.models.variation_skill import VariationSkill

# TODO update the JSON string below
json = "{}"
# create an instance of VariationSkill from a JSON string
variation_skill_instance = VariationSkill.from_json(json)
# print the JSON string representation of the object
print(VariationSkill.to_json())

# convert the object into a dict
variation_skill_dict = variation_skill_instance.to_dict()
# create an instance of VariationSkill from a dict
variation_skill_from_dict = VariationSkill.from_dict(variation_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


