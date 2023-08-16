## `Member`
---
### `Member.__init__`
`Member` constructor
    
**params:**
- **`user_id (str)`**: User id of the member.
- **`nickname (str)`**: Nickname of the member.
- **`muted (bool)`**: `True` if the member is muted, else `False`.
- **`image_url (str)`**: URL to the profile picture of the member.
- **`autokicked (bool)`**: `True` if the member was autokicked, else `False`.
- **`member_id (str)`**: The group member id of the member.


### `Member.from_dict`
Returns a `Member` object initialized using the `member_dict` parameter.
    
**params:**
- **`message_dict (dict)`**: Used to initialize the returned `Member` object.
Must contain keys and values corresponding to the parameters in
`Member.__init__`


### `Member._add`
[Official GroupMe Add Member Documentation](https://dev.groupme.com/docs/v3#members_add)
    
Add one or more members to the group given by `group_id`. Returns a GUID 
that can be used to query the status of the member's addition to the group

**params:**
- **`group_id (str)`**: ID of the group you wish to add users to.
- **`members (list[dict])`**: Members to add to the group; Must have key `nickname`
and optionally keys `user_id`, `phone_number`, `email`, `guid`

raises:
- `UnexpectedStatusCodeError`


### `Member._add_result`
Get the membership addition results. Successfully created members will be
returned. Failed memberships and invites are omitted.

**params:**
- **`group_id (str)`**: ID of the group you wish to check the memberships result of.
- **`result_id (str)`**: GUID returned by a previous call to `Member._add()`.

**raises:**
- `UnexpectedStatusCodeError`


### `Member._remove`
Remove a member from the group given by `group_id`.

**params:**
- **`group_id (str)`**: ID of the group you wish to remove a member from.
- **`member_id (str)`**: ID of the member you wish to remove from the group.

**raises:**
- `UnexpectedStatusCodeError`


### `Member._update`
Change your nickname in the group given by `group_id`.
    
NOTE: You can only change your own nickname.

**params:**
- **`group_id (str)`**: ID of the group you wish to update your nickname in.
- **`nickname (str)`**: The new nickname for your user.

**raises:**
- `UnexpectedStatusCodeError`