# MetricEventDefaultRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Whether to disable defaulting missing unit events when calculating results. Defaults to false | [optional] 
**value** | **float** | The default value applied to missing unit events. Set to 0 when &lt;code&gt;disabled&lt;/code&gt; is false. No other values are currently supported. | [optional] 

## Example

```python
from launchdarkly_api.models.metric_event_default_rep import MetricEventDefaultRep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricEventDefaultRep from a JSON string
metric_event_default_rep_instance = MetricEventDefaultRep.from_json(json)
# print the JSON string representation of the object
print(MetricEventDefaultRep.to_json())

# convert the object into a dict
metric_event_default_rep_dict = metric_event_default_rep_instance.to_dict()
# create an instance of MetricEventDefaultRep from a dict
metric_event_default_rep_from_dict = MetricEventDefaultRep.from_dict(metric_event_default_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


