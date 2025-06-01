from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.task_list import TaskList
from ...models.taskindex_assignee_type import TaskindexAssigneeType
from ...models.taskindex_order import TaskindexOrder
from ...models.taskindex_permission import TaskindexPermission
from ...models.taskindex_priority import TaskindexPriority
from ...models.taskindex_status import TaskindexStatus
from ...models.taskindex_statuses import TaskindexStatuses
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assignee_id: Unset | int = UNSET,
    assignee_type: Unset | TaskindexAssigneeType = UNSET,
    assigner_id: Unset | int = UNSET,
    cascading_source_id: Unset | int = UNSET,
    client_id: Unset | int = UNSET,
    complete: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    due_at_from: Unset | str = UNSET,
    due_at_present: Unset | bool = UNSET,
    due_at_to: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | TaskindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    permission: Unset | TaskindexPermission = UNSET,
    priority: Unset | TaskindexPriority = UNSET,
    query: Unset | str = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    status: Unset | TaskindexStatus = UNSET,
    statuses: Unset | TaskindexStatuses = UNSET,
    statute_of_limitations: Unset | bool = UNSET,
    task_type_id: Unset | int = UNSET,
    time_entries_present: Unset | bool = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["assignee_id"] = assignee_id

    json_assignee_type: Unset | str = UNSET
    if not isinstance(assignee_type, Unset):
        json_assignee_type = assignee_type.value

    params["assignee_type"] = json_assignee_type

    params["assigner_id"] = assigner_id

    params["cascading_source_id"] = cascading_source_id

    params["client_id"] = client_id

    params["complete"] = complete

    params["created_since"] = created_since

    params["due_at_from"] = due_at_from

    params["due_at_present"] = due_at_present

    params["due_at_to"] = due_at_to

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    json_permission: Unset | str = UNSET
    if not isinstance(permission, Unset):
        json_permission = permission.value

    params["permission"] = json_permission

    json_priority: Unset | str = UNSET
    if not isinstance(priority, Unset):
        json_priority = priority.value

    params["priority"] = json_priority

    params["query"] = query

    params["responsible_attorney_id"] = responsible_attorney_id

    json_status: Unset | str = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_statuses: Unset | str = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses.value

    params["statuses[]"] = json_statuses

    params["statute_of_limitations"] = statute_of_limitations

    params["task_type_id"] = task_type_id

    params["time_entries_present"] = time_entries_present

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tasks.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | TaskList | None:
    if response.status_code == 200:
        response_200 = TaskList.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TaskList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    assignee_id: Unset | int = UNSET,
    assignee_type: Unset | TaskindexAssigneeType = UNSET,
    assigner_id: Unset | int = UNSET,
    cascading_source_id: Unset | int = UNSET,
    client_id: Unset | int = UNSET,
    complete: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    due_at_from: Unset | str = UNSET,
    due_at_present: Unset | bool = UNSET,
    due_at_to: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | TaskindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    permission: Unset | TaskindexPermission = UNSET,
    priority: Unset | TaskindexPriority = UNSET,
    query: Unset | str = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    status: Unset | TaskindexStatus = UNSET,
    statuses: Unset | TaskindexStatuses = UNSET,
    statute_of_limitations: Unset | bool = UNSET,
    task_type_id: Unset | int = UNSET,
    time_entries_present: Unset | bool = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | TaskList]:
    """Return the data for all Tasks

     Outlines the parameters, optional and required, used when requesting the data for all Tasks

    Args:
        assignee_id (Union[Unset, int]):
        assignee_type (Union[Unset, TaskindexAssigneeType]):
        assigner_id (Union[Unset, int]):
        cascading_source_id (Union[Unset, int]):
        client_id (Union[Unset, int]):
        complete (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        due_at_from (Union[Unset, str]):
        due_at_present (Union[Unset, bool]):
        due_at_to (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, TaskindexOrder]):
        page_token (Union[Unset, str]):
        permission (Union[Unset, TaskindexPermission]):
        priority (Union[Unset, TaskindexPriority]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        status (Union[Unset, TaskindexStatus]):
        statuses (Union[Unset, TaskindexStatuses]):
        statute_of_limitations (Union[Unset, bool]):
        task_type_id (Union[Unset, int]):
        time_entries_present (Union[Unset, bool]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TaskList]]
    """

    kwargs = _get_kwargs(
        assignee_id=assignee_id,
        assignee_type=assignee_type,
        assigner_id=assigner_id,
        cascading_source_id=cascading_source_id,
        client_id=client_id,
        complete=complete,
        created_since=created_since,
        due_at_from=due_at_from,
        due_at_present=due_at_present,
        due_at_to=due_at_to,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        permission=permission,
        priority=priority,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        status=status,
        statuses=statuses,
        statute_of_limitations=statute_of_limitations,
        task_type_id=task_type_id,
        time_entries_present=time_entries_present,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    assignee_id: Unset | int = UNSET,
    assignee_type: Unset | TaskindexAssigneeType = UNSET,
    assigner_id: Unset | int = UNSET,
    cascading_source_id: Unset | int = UNSET,
    client_id: Unset | int = UNSET,
    complete: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    due_at_from: Unset | str = UNSET,
    due_at_present: Unset | bool = UNSET,
    due_at_to: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | TaskindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    permission: Unset | TaskindexPermission = UNSET,
    priority: Unset | TaskindexPriority = UNSET,
    query: Unset | str = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    status: Unset | TaskindexStatus = UNSET,
    statuses: Unset | TaskindexStatuses = UNSET,
    statute_of_limitations: Unset | bool = UNSET,
    task_type_id: Unset | int = UNSET,
    time_entries_present: Unset | bool = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | TaskList | None:
    """Return the data for all Tasks

     Outlines the parameters, optional and required, used when requesting the data for all Tasks

    Args:
        assignee_id (Union[Unset, int]):
        assignee_type (Union[Unset, TaskindexAssigneeType]):
        assigner_id (Union[Unset, int]):
        cascading_source_id (Union[Unset, int]):
        client_id (Union[Unset, int]):
        complete (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        due_at_from (Union[Unset, str]):
        due_at_present (Union[Unset, bool]):
        due_at_to (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, TaskindexOrder]):
        page_token (Union[Unset, str]):
        permission (Union[Unset, TaskindexPermission]):
        priority (Union[Unset, TaskindexPriority]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        status (Union[Unset, TaskindexStatus]):
        statuses (Union[Unset, TaskindexStatuses]):
        statute_of_limitations (Union[Unset, bool]):
        task_type_id (Union[Unset, int]):
        time_entries_present (Union[Unset, bool]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, TaskList]
    """

    return sync_detailed(
        client=client,
        assignee_id=assignee_id,
        assignee_type=assignee_type,
        assigner_id=assigner_id,
        cascading_source_id=cascading_source_id,
        client_id=client_id,
        complete=complete,
        created_since=created_since,
        due_at_from=due_at_from,
        due_at_present=due_at_present,
        due_at_to=due_at_to,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        permission=permission,
        priority=priority,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        status=status,
        statuses=statuses,
        statute_of_limitations=statute_of_limitations,
        task_type_id=task_type_id,
        time_entries_present=time_entries_present,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    assignee_id: Unset | int = UNSET,
    assignee_type: Unset | TaskindexAssigneeType = UNSET,
    assigner_id: Unset | int = UNSET,
    cascading_source_id: Unset | int = UNSET,
    client_id: Unset | int = UNSET,
    complete: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    due_at_from: Unset | str = UNSET,
    due_at_present: Unset | bool = UNSET,
    due_at_to: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | TaskindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    permission: Unset | TaskindexPermission = UNSET,
    priority: Unset | TaskindexPriority = UNSET,
    query: Unset | str = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    status: Unset | TaskindexStatus = UNSET,
    statuses: Unset | TaskindexStatuses = UNSET,
    statute_of_limitations: Unset | bool = UNSET,
    task_type_id: Unset | int = UNSET,
    time_entries_present: Unset | bool = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | TaskList]:
    """Return the data for all Tasks

     Outlines the parameters, optional and required, used when requesting the data for all Tasks

    Args:
        assignee_id (Union[Unset, int]):
        assignee_type (Union[Unset, TaskindexAssigneeType]):
        assigner_id (Union[Unset, int]):
        cascading_source_id (Union[Unset, int]):
        client_id (Union[Unset, int]):
        complete (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        due_at_from (Union[Unset, str]):
        due_at_present (Union[Unset, bool]):
        due_at_to (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, TaskindexOrder]):
        page_token (Union[Unset, str]):
        permission (Union[Unset, TaskindexPermission]):
        priority (Union[Unset, TaskindexPriority]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        status (Union[Unset, TaskindexStatus]):
        statuses (Union[Unset, TaskindexStatuses]):
        statute_of_limitations (Union[Unset, bool]):
        task_type_id (Union[Unset, int]):
        time_entries_present (Union[Unset, bool]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TaskList]]
    """

    kwargs = _get_kwargs(
        assignee_id=assignee_id,
        assignee_type=assignee_type,
        assigner_id=assigner_id,
        cascading_source_id=cascading_source_id,
        client_id=client_id,
        complete=complete,
        created_since=created_since,
        due_at_from=due_at_from,
        due_at_present=due_at_present,
        due_at_to=due_at_to,
        fields=fields,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        permission=permission,
        priority=priority,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        status=status,
        statuses=statuses,
        statute_of_limitations=statute_of_limitations,
        task_type_id=task_type_id,
        time_entries_present=time_entries_present,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    assignee_id: Unset | int = UNSET,
    assignee_type: Unset | TaskindexAssigneeType = UNSET,
    assigner_id: Unset | int = UNSET,
    cascading_source_id: Unset | int = UNSET,
    client_id: Unset | int = UNSET,
    complete: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    due_at_from: Unset | str = UNSET,
    due_at_present: Unset | bool = UNSET,
    due_at_to: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | TaskindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    permission: Unset | TaskindexPermission = UNSET,
    priority: Unset | TaskindexPriority = UNSET,
    query: Unset | str = UNSET,
    responsible_attorney_id: Unset | int = UNSET,
    status: Unset | TaskindexStatus = UNSET,
    statuses: Unset | TaskindexStatuses = UNSET,
    statute_of_limitations: Unset | bool = UNSET,
    task_type_id: Unset | int = UNSET,
    time_entries_present: Unset | bool = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | TaskList | None:
    """Return the data for all Tasks

     Outlines the parameters, optional and required, used when requesting the data for all Tasks

    Args:
        assignee_id (Union[Unset, int]):
        assignee_type (Union[Unset, TaskindexAssigneeType]):
        assigner_id (Union[Unset, int]):
        cascading_source_id (Union[Unset, int]):
        client_id (Union[Unset, int]):
        complete (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        due_at_from (Union[Unset, str]):
        due_at_present (Union[Unset, bool]):
        due_at_to (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, TaskindexOrder]):
        page_token (Union[Unset, str]):
        permission (Union[Unset, TaskindexPermission]):
        priority (Union[Unset, TaskindexPriority]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        status (Union[Unset, TaskindexStatus]):
        statuses (Union[Unset, TaskindexStatuses]):
        statute_of_limitations (Union[Unset, bool]):
        task_type_id (Union[Unset, int]):
        time_entries_present (Union[Unset, bool]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, TaskList]
    """

    return (
        await asyncio_detailed(
            client=client,
            assignee_id=assignee_id,
            assignee_type=assignee_type,
            assigner_id=assigner_id,
            cascading_source_id=cascading_source_id,
            client_id=client_id,
            complete=complete,
            created_since=created_since,
            due_at_from=due_at_from,
            due_at_present=due_at_present,
            due_at_to=due_at_to,
            fields=fields,
            ids=ids,
            limit=limit,
            matter_id=matter_id,
            order=order,
            page_token=page_token,
            permission=permission,
            priority=priority,
            query=query,
            responsible_attorney_id=responsible_attorney_id,
            status=status,
            statuses=statuses,
            statute_of_limitations=statute_of_limitations,
            task_type_id=task_type_id,
            time_entries_present=time_entries_present,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
