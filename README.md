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
        url: 'https://domain.freshdesk.com/api/v2/tickets'
        url1: 'https://domain.freshdesk.com/api/v2/contacts'
        api_key: 'Freshdesk Api key'      
 ```

# Payload Format
To create a ticket the following payload format is required

      "payload":{"elements": [ {
                                 "subject" : "Ticket title",
                                 "description" : "Ticket detail",
                                 "email": "example@example.com",
                                 "priority" : 2,
                                 "status" : 2,
                                  "cc_emails" : ["sample_email@domain.com", "user_email@domain.com"]
                                                 }],
                 "metadata":{}}
To update a ticket

       "payload":{"elements": [{
                                 "subject" : "Updted Subject",
                                  "description" : "Updated description",
                                  "priority" : 3},
                                {"ticket_id":3}],
                  "metadata":{}}
To delete,view or restore a ticket

        "payload":{"elements": [{"ticket_id":3}],
                  "metadata":{}}

Similarly to create a contact

        "payload":{"elements":[ {
                           "contact_info":{"name":"jkkkhjh",
                                     "email":"t1111iles@dshfkjkjfh.com"
                           }}],
                   "metadata":{}}
Update a contact

        "payload":{"elements":[ {"contact_info":{"name":"Douglas Adams","email":"slartibartfast@dirt.com"}},             
                                {"contact_id":"29000301593"}], 
        "metadata":{}}
Delete a contact

        "payload":{"elements":[ {"contact_id":"31000292499"}],
        "metadata":{}}
