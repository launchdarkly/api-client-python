# VariationSkillPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the agent skill to attach. | 
**version** | **int** | The version of the skill to use. | 

## Example

```python
from launchdarkly_api.models.variation_skill_post import VariationSkillPost

# TODO update the JSON string below
json = "{}"
# create an instance of VariationSkillPost from a JSON string
variation_skill_post_instance = VariationSkillPost.from_json(json)
# print the JSON string representation of the object
print(VariationSkillPost.to_json())

# convert the object into a dict
variation_skill_post_dict = variation_skill_post_instance.to_dict()
# create an instance of VariationSkillPost from a dict
variation_skill_post_from_dict = VariationSkillPost.from_dict(variation_skill_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


