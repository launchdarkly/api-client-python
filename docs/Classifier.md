# Classifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**type** | **str** |  | 
**instructions** | **str** |  | 
**criteria** | **object** | Type-specific criteria. An enum classifier uses a map of option keys to descriptions. A float classifier uses an ordered list of level labels. A bool classifier uses optional true and false descriptions.  | [optional] 

## Example

```python
from launchdarkly_api.models.classifier import Classifier

# TODO update the JSON string below
json = "{}"
# create an instance of Classifier from a JSON string
classifier_instance = Classifier.from_json(json)
# print the JSON string representation of the object
print(Classifier.to_json())

# convert the object into a dict
classifier_dict = classifier_instance.to_dict()
# create an instance of Classifier from a dict
classifier_from_dict = Classifier.from_dict(classifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


