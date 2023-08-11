# groupmeme.api

Contains classes and functions used to interface with the GroupMe API.

## `Group`
---
### `Group.__init__`
`Group` constructor

**params:**

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
Returns a [`Group`](#group) object initialized using a `dict`.

The dict must contain keys corresponding to the parameters in the [`Group constructor`](#group__init__) (`id`, `name`, `type`, `description`, `image_url`, `members`, `created_at`, `updated_at`, `creator_user_id`, `share_url`, `messages`)

**params**:
- **`group_dict (dict)`**: `dict` used to initialize the Group

### `Group._groups`
Returns a paginated list of [`Group`](#group) objects that the user is a part of.

**params**:
- **`page (int)`**: Page of results, defaults to `1`
- **`per_page (int)`**: `Group` results per page, defaults to `10`
- **`omit (str)`**: Comma seperated list of fields to omit from each `Group` result. The only currently supported value is just `"memberships"` which results in the `members` field being empty

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)

### `Group._former_groups`
Returns a list of all the [`Group`](#group)s that the user has previously left.

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)

### `Group._get`
Returns a [`Group`](#group) matching the supplied `group_id`.

**params**:
- **`group_id (str)`**: ID of a group

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)

### `Group._create`
Creates a GroupMe `Group`.

**params**:
- **`name (str)`**: The name of the `Group`
- **`description (str)`** *optional*:  Description of the `Group`
- **`image_url (str)`** *optional*: URL of the `Group`'s profile image
- **`share (bool)`**: *optional*: If `True` a share URL will be generated for the `Group`, if `False` a share URL will not be generated for the `Group`. Defaults to `False`

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)


### `Group._update`
Update the information for a `Group`.

Only the group's creator has authority to update the group.

**params**:
- **`group_id (str)`**: ID of the `Group` you wish to update the information of
- **`name (str)`** *optional*: The new name of the `Group`
- **`description (str)`** *optional*: The new description of the `Group`
- **`image_url (str)`** *optional*: The new URL of the profile picture of the `Group`
- **`office_mode (bool)`** *optional*: The new value of `office_mode` for the `Group`, if `office_mode` is `False` notifications from this group won't buzz your phone
- **`share (bool)`** *optional*: The new value of `share` for the `Group`, if `True` then a share URL will be generated that can be used to join the `Group`

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)


### `Group._destroy`
Destroy a `Group`.

Only the group's creator has authority to destroy the group.

**params**:
- **`group_id (str)`**: The ID of the `Group` to delete

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)


### `Group._join`
Join a `Group`.

**params**:
- **`group_id (str)`**: ID of the `Group` you wish to join
- **`share_token (str)`**: Share token of the `Group` you wish to join

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)


### `Group._rejoin`
Rejoin a `Group`.

You have to have previously left (not banned or kicked) in order to rejoin a group.

**params**:
- **`group_id (str)`**: ID of the `Group` you wish to join
- **`share_token (str)`**: Share token of the `Group` you wish to join

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)

### `Group._change_ownership`
Change ownership of the `Group` to another user.

Only the owner of the group has the authorization to change the ownership of the group.

**params**:
- **`group_id (str)`**: ID of the `Group` you wish to change the owner of
- **`owner_id (str)`**: ID of the user you wish to transfer ownership to

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)

### `Group.update`
Updates the information for a `Group`.

Only the group's creator has authority to update the group.

**params**:
- **`name (str)`** *optional*: The new name of the `Group`
- **`description (str)`** *optional*: The new description of the `Group`
- **`image_url (str)`** *optional*: The new URL of the profile picture of the `Group`
- **`office_mode (bool)`** *optional*: The new value of `office_mode` for the `Group`, if `office_mode` is `False` notifications from this group won't buzz your phone
- **`share (bool)`** *optional*: The new value of `share` for the `Group`, if `True` then a share URL will be generated that can be used to join the `Group`

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)

### `Group.destroy`
Destroys a `Group`.

Only the group's creator has authority to destroy the group.

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)

### `Group.rejoin`
Rejoin a `Group`.

You have to have previously left (not banned or kicked) in order to rejoin a group.

**params**:
- **`share_token (str)`**: Share token of the `Group` you wish to join

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)

### `Group.change_ownership`
Change ownership of the `Group` to another user

Only the owner of the group has the authorization to change the ownership of the group

**params**:
- **`owner_id (str)`**: ID of the user you wish to transfer ownership to

**raises**:
- [`UnexpectedStatusCodeError`](/groupmeme/api/errors#unexpectedstatuscodeerror)


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