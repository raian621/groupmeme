# groupmeme.api

Contains classes and functions used to interface with the GroupMe API.


- [`Group`](/groupmeme/api/group)
- [`Bot`](/groupmeme/api/bot)
- [`Member`](/groupmeme/api/member)
- [`Message`](/groupmeme/api/message)
- [`Pictures`](/groupmeme/api/pictures)
- [`User`](/groupmeme/api/user)


## Note on Static Class Functions and Class Functions
---
Most functions used to interface with the GroupMe API are static class methods from classes corresponding to the desired API category:

```py
Group._update(group_id='1234567890', name='Updated Name')
```

Some static class methods will have a corresponding class method that passes data from the object it is called on such as the object's id from the object it is called from to the static class method:

```py
# my_group is a Group object:
my_group.update(name='Updated Name')
---
# behind the scenes :3
class Group:
  ...
  def update(self, name, ...):
    return Group._update(self.id, name=name)
```

Static class methods that interact with the GroupMe API will always be prefixed with an underscore:

```py
Group._update()
```

Whereas regular ol' class methods will drop the underscore at the beginning of the method:
```py
Group.update()
```