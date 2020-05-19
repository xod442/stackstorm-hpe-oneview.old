# HPE OneView Integration Pack
This pack allows you to integrate with HPE OneView

## Configuration
Copy the example configuration in [hpeoneview.yaml.example](./hpeoneview.yaml.example) to
`/opt/stackstorm/configs/hpeoneview.yaml` and edit as required.

It must contain:

```
ipaddress - Your OneView appliance IP address
username - OneView User name
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
* ``get_interconnects``
* ``get_network_sets``
* ``get_`enclosure`
* ``post_fabrics``

### Orquestra Workflows: will not
