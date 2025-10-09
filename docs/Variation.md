# Variation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the variation. Leave empty when you are creating a flag. | [optional] 
**value** | **object** | The value of the variation. For boolean flags, this must be &lt;code&gt;true&lt;/code&gt; or &lt;code&gt;false&lt;/code&gt;. For multivariate flags, this may be a string, number, or JSON object. | 
**description** | **str** | Description of the variation. Defaults to an empty string, but is omitted from the response if not set. | [optional] 
**name** | **str** | A human-friendly name for the variation. Defaults to an empty string, but is omitted from the response if not set. | [optional] 

## Example

```python
from launchdarkly_api.models.variation import Variation

# TODO update the JSON string below
json = "{}"
# create an instance of Variation from a JSON string
variation_instance = Variation.from_json(json)
# print the JSON string representation of the object
print(Variation.to_json())

# convert the object into a dict
variation_dict = variation_instance.to_dict()
# create an instance of Variation from a dict
variation_from_dict = Variation.from_dict(variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


