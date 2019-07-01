# Notifications action for all issues
def save_default_business_rules1(orm):
    for businessRule in [
            orm.BusinessRule(aggregation_period=30, action_params='{ "userGroup" : 0 }', event_type=3, action_type=7, event_state=2, event_condition='{  }'),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=4, action_type=7, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=5, action_type=7, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=6, action_type=7, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=7, action_type=7, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=8, action_type=7, event_state=2, event_condition="{  }")
        ]:
        businessRule.save()

# Email action for all issues
def save_default_business_rules2(orm):
    # If called from code -> orm is vms.models module. If from migration it's a FakeORM class
    user_class = orm.User if type(orm).__name__ == 'module' else orm['auth.User']
    instance, _ = user_class.objects.get_or_create(username='admin', is_superuser=True)
    xtype, _ = orm.ResourceType.objects.get_or_create(name='User')
    admin_profile, _ = orm.UserProfile.objects.get_or_create(user=instance, xtype=xtype, name=instance.username)

    for businessRule in [
            orm.BusinessRule(aggregation_period=21600, action_params="{  }", event_type=3, action_type=5, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=21600, action_params="{  }", event_type=4, action_type=5, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=21600, action_params="{  }", event_type=5, action_type=5, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=21600, action_params="{  }", event_type=6, action_type=5, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=21600, action_params="{  }", event_type=7, action_type=5, event_state=2, event_condition="{  }"),
            orm.BusinessRule(aggregation_period=21600, action_params="{  }", event_type=8, action_type=5, event_state=2, event_condition="{  }") ]:
        businessRule.save()
        businessRule.action_resources.add(admin_profile)

# Diagnostics action for all issues
def save_default_business_rules3(orm):
    for businessRule in [
            orm.BusinessRule(aggregation_period=30, action_params='{  }', event_type=3, action_type=6, event_state=2, event_condition='{  }', system = True),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=4, action_type=6, event_state=2, event_condition="{  }", system = True),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=5, action_type=6, event_state=2, event_condition="{  }", system = True),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=6, action_type=6, event_state=2, event_condition="{  }", system = True),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=7, action_type=6, event_state=2, event_condition="{  }", system = True),
            orm.BusinessRule(aggregation_period=30, action_params="{  }", event_type=8, action_type=6, event_state=2, event_condition="{  }", system = True)
        ]:
        businessRule.save()

def save_default_business_rules4(orm):
    orm.BusinessRule(aggregation_period=0, action_params='{  }', event_type=9, action_type=6, event_state=2, event_condition='{  }', system = True).save()

def save_all_default_business_rules(orm):
    save_default_business_rules1(orm)
    save_default_business_rules2(orm)
    save_default_business_rules3(orm)
    save_default_business_rules4(orm)

