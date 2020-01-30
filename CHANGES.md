# hpeOneView-stackstorm
stackstorm integration pack for HPE One View

## Configuration
Copy the example configuration in [hpeoneview.yaml.example](./hpeoneview.yaml.example) to
`/opt/stackstorm/configs/hpeoneview.yaml` and edit as required.

It must contain:

```
ipaddress - Your OneView appliance IP address
username - OneView Username
password - OneView Password
```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  ipaddress: "10.10.10.10"
  username: "Administrator"
  password: "password"
```
You can also run `st2 pack config hpeoneview` and answer the promts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_``
* ``get_switches``
* ``get_events``
* ``post_fit``

### Orquestra Workflows: will not
* ``sendsnow``
* ``performfit``
* ``getswitches``
* ``getfabric_for_fit``
