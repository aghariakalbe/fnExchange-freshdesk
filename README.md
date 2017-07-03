# fnExchange Freshdesk Plugin
This is a plugin for the fnExchange API router for interacting with Freshdesk's ticket management system

This plugin currently provides actions that include creating, updating, deleting, viewing tickets and contacts

# Installation
To install this change current working directory to fnexchange-freshdesk and run
```
$ pip install .
```

# Configuration
To use this plugin with fnExchange, add the appropriate configuration to the `fnexchange.yml`
configuration file under `plugins_enabled`. A sample configuration is provided below.
Of course, note that you can use any alias instead of "freshdesk".

The plugin **requires** the `url` configuration.

```yaml
...
  plugins_enabled:
    ...
    freshdesk:
      class_name: 'fnexchange_slack.FreshdeskPlugin'
      config:
        url: 'www.domain.freshdesk.com'
        api_key:'Freshdesk Api key'
    ...
...
```
