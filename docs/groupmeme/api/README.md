# groupmeme.api

Contains classes and functions used to interface with the GroupMe API.

## `Group`
---
### `Group.__init__`
`Group` constructor

**Params:**

- **`id (str)`**: ID of the Group.
- **`name (str)`**: The name of the Group
- **`type (str)`**: The type of Group (`'public'` or `'private'`)
- **`description (str)`**: The description of the Group
- **`image_url (str)`**: URL for the Group's profile image
- **`members (list[`[`Member`](/groupmeme/api/#member)`])`**- Members of the Group
- **`created_at (str)`**: The time (Unix time) that the Group was created
- **`updated_at (str)`**: The time (Unix time) that the Group was last updated
- **`creator_user_id (str)`**: ID of the creator of the Group
- **`share_url (str)`**: URL that can be used to join the Group
- **`messages (list[`[`Message`](/groupmeme/api/#message)`])`**: Messages in the Group

### `Group.from_dict`
Initializes a `Group` object using the `group_dict` `dict`.

**Params**:
- **`group_dict (dict)`**: `dict` used to initialize the Group
**Returns**: `Group`

### `Group._groups`
**Params**:

**Returns**: `list[Group]`
### `Group._former_groups`
**Params**:

**Returns**: `list[Group]`
### `Group._get`
**Params**:

**Returns**: `Group`
### `Group._create`
**Params**:

**Returns**: `Group`
### `Group._update`
**Params**:

**Returns**: `Group`
### `Group._destroy`
**Params**:

**Returns**: `status_code (int)`

## `Bot`
---
### `Bot.__init__`
### `Bot.from_dict`
**Params**:

**Returns**:

### `Bot._create`
**Params**:

**Returns**:

### `Bot._send_message`
**Params**:

**Returns**:

### `Bot.send_message`
**Params**:

**Returns**:

### `Bot._get_bots`
**Params**:

**Returns**:

### `Bot._destroy_bot`
**Params**:

**Returns**:


## `Member`
---
### `Member.__init__`
**Params**:

**Returns**:

### `Member.from_dict`
**Params**:

**Returns**:

### `Member._add`
**Params**:

**Returns**:

### `Member._add_result`
**Params**:

**Returns**:

### `Member._remove`
**Params**:

**Returns**:

### `Member._update`
**Params**:

**Returns**:


## `Message`
---
### `Message.__init__`
### `Message.from_dict`
**Params**:

**Returns**:

### `Message._messages`
**Params**:

**Returns**:

### `Message._create`
**Params**:

**Returns**:


## `Pictures`
---
### `upload_picture`
**Params**:

**Returns**:


## `User`
---
### `User.__init__`
### `User.from_dict`
**Params**:

**Returns**:

### `User._me`
**Params**:

**Returns**:

### `User._update_me`
**Params**:

**Returns**:


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